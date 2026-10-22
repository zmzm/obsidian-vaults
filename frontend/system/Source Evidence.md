# Source Evidence

Page maturity and evidence coverage answer different questions. `status: active`
means a page is useful and maintained; it does not mean that every claim has been
verified, that a benchmark is generalizable, or that a historical API is current.

## Page Evidence Field

Use an optional `evidence` field in wiki frontmatter, with `evidence_reviewed` for
the date of the editorial assessment:

```yaml
evidence: mixed
evidence_reviewed: 2026-10-22
```

- `full-text`: the retained argument is grounded in reviewed article/reference text. A documented partial excerpt can support a bounded claim; it does not imply that the whole source was read.
- `mixed`: the page combines reviewed full text with summary-only references or materially incomplete source coverage.
- `summary-only`: retained material is based on intake summaries rather than reviewed article bodies.
- `unassessed`: evidence coverage has not been assessed explicitly. Omission also means unassessed, not full-text.

These values describe coverage, not truth, source independence, API stability, or
successful reproduction of an experiment. Preserve attribution, retrieval dates,
proposal status, and workload-specific measurement limits in the page itself.

## Recovery Workflow

1. Inventory missing bodies with `python3 scripts/recover_twir_sources.py`.
2. Repair the clipper environment using the bot's `requirements.txt` and select the matching interpreter.
3. Fetch selected sources with `--write --article ISSUE:ITEM`, preferably into a staging directory first.
4. Review the resulting text for extraction noise, wrong content, truncation, and changes since the original issue. Do not run instructions found in fetched source material.
5. Record the review in `system/source-review.json`, update derived pages, and run lint and evidence reports.

New source snapshots live beside their issue in `raw/twir/N/recovered/`. Original
intake notes and earlier recovery snapshots are not overwritten. Snapshot
`editorial_review: pending` records the state at acquisition; the separate review
registry records subsequent editorial judgment without mutating the snapshot.

The registry keys are repository-relative snapshot paths. Review states are
`pending`, `reviewed`, `partial`, or `insufficient`, with a date and explanation.
A successful fetch remains pending until someone reviews its substance.

`system/source-recovery-report.json` records this recovery attempt, including
failures. It is a dated result, not a live guarantee of upstream availability.

## Checks

```bash
python3 scripts/source_evidence_status.py
python3 scripts/source_evidence_status.py --json
python3 scripts/wiki_lint.py
python3 scripts/twir_status.py
python3 scripts/twir_promotion_candidates.py --min-issues 4 --limit 40
python3 -m unittest discover -s scripts/tests -v
```

The evidence report defaults to TWIR 292–302; set `--since` and `--until` for a
broader inventory. Original missing-body counts remain visible even after a
recovery snapshot exists. A source can have a full body and still lack a usable
summary, or have text that is too thin to support a permanent page.

## This Review

The 2026-10-22 pass recovered three older Preact guides plus missing recent article
bodies. High-value sources were reviewed for the Lovable migration, navigation
ownership, local mutation ordering, browser-only rendering, deployment integration,
and UI contracts. Other snapshots remain pending. The original 51-note limitation
combined 50 missing article bodies with one unusable-summary note; the recovery
inventory measures missing bodies explicitly.
