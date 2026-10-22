import contextlib
import importlib.util
import io
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import twir_promotion_candidates as promotion
import recover_twir_sources as recovery
from vault_utils import title_from_target

class PromotionTests(unittest.TestCase):
    def test_raw_references_never_become_themes_and_dotted_titles_survive(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / 'TWIR 1.md'
            path.write_text('[[../../raw/twir/1/articles/01 - Next.js case|Article]]\n'
                            '[[../../raw/twir/1/2026-01-01-TWIR-1]]\n'
                            '[[../tools/Next.js|Next.js]]\n[[TWIR 2]]\n[[React DevTools]]')
            with patch.object(promotion, 'WIKI_SOURCES', Path(tmp)):
                self.assertEqual(promotion.wiki_digest_links(1), {'Next.js','React DevTools'})
        self.assertEqual(title_from_target('../tools/Next.js.md'), 'Next.js')

    def test_devtools_alias_reuses_existing_hub(self):
        for value in ['Devtools', 'react-devtools', 'React DevTools']:
            name = promotion.normalize_theme(value)
            self.assertEqual(name, 'React DevTools')
            self.assertEqual(promotion.coverage_for(name, {'reactdevtools':'React DevTools'}), 'React DevTools')

class RecoveryTests(unittest.TestCase):
    def test_body_detection_distinguishes_summary_and_article(self):
        self.assertTrue(recovery.missing_body('Summary:\nUseful summary\nContent:\nContent not available.'))
        self.assertTrue(recovery.missing_body('Summary:\nSummary not available.'))
        self.assertFalse(recovery.missing_body('Summary:\nMissing full text in an old note.\nContent:\n# Full article\nActual text'))

    def test_failed_worker_does_not_create_snapshot(self):
        row={'issue':1,'item':2,'path':'frontend/raw/twir/1/articles/02 - Note.md','url':'https://example.com','title':'Note'}
        with tempfile.TemporaryDirectory() as tmp:
            with patch.object(recovery.subprocess, 'run') as run:
                run.return_value.returncode=1
                run.return_value.stdout=json.dumps({'ok':False,'error':'403 Forbidden'})
                result=recovery.recover(row,Path('clipper.py'),'python3',Path(tmp))
            self.assertEqual(result['result'],'failed')
            self.assertEqual(list(Path(tmp).rglob('*.md')),[])

    def test_snapshot_preserves_original_and_is_not_overwritten(self):
        row={'issue':1,'item':2,'path':'frontend/raw/twir/1/articles/02 - Note.md','url':'https://example.com','title':'Note'}
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp);original=root/'1/articles/02 - Note.md'
            original.parent.mkdir(parents=True);original.write_text('Original extraction failure')
            with patch.object(recovery.subprocess, 'run') as run:
                run.return_value.returncode=0
                run.return_value.stdout=json.dumps({'ok':True,'markdown':'# Article\n'+'Actual article text. '*30})
                self.assertEqual(recovery.recover(row,Path('clipper.py'),'python3',root)['result'],'saved')
                self.assertEqual(recovery.recover(row,Path('clipper.py'),'python3',root)['result'],'exists')
                self.assertEqual(run.call_count,1)
            self.assertEqual(original.read_text(),'Original extraction failure')
            self.assertIn('editorial_review: "pending"',(root/'1/recovered/02 - Note.md').read_text())


class EvidenceTests(unittest.TestCase):
    def test_invalid_evidence_is_rejected_without_requiring_legacy_metadata(self):
        import wiki_lint
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp);note=root/'Example.md'
            base='---\ntype: concept\nstatus: active\nupdated: 2026-10-22\n'
            with patch.object(wiki_lint,'wiki_pages',return_value=[note]),patch.object(wiki_lint,'rel',side_effect=lambda p:p.name):
                note.write_text(base+'---\n')
                self.assertEqual(wiki_lint.check_frontmatter(),[])
                note.write_text(base+'evidence: guaranteed\n---\n')
                self.assertTrue(any('invalid evidence' in error for error in wiki_lint.check_frontmatter()))
                note.write_text(base+'evidence: mixed\n---\n')
                self.assertEqual(wiki_lint.check_frontmatter(),[])

    def test_omitted_evidence_is_unassessed_and_a_snapshot_is_not_automatic_review(self):
        import source_evidence_status
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp);wiki=root/'wiki';wiki.mkdir()
            (wiki/'Example.md').write_text('---\ntype: concept\nstatus: active\n---\n')
            row={'snapshot':'frontend/raw/twir/1/recovered/Note.md','recovered':True}
            with patch.object(source_evidence_status,'FRONTEND',root),patch.object(source_evidence_status,'WIKI',wiki),patch.object(source_evidence_status,'rel',side_effect=lambda p:p.name),patch.object(source_evidence_status,'candidates',return_value=[row]):
                data=source_evidence_status.status(1,1)
            self.assertEqual(data['wiki_evidence'],{'unassessed':1})
            self.assertEqual(data['articles'][0]['review'],'pending')

if __name__ == "__main__":
    unittest.main()
