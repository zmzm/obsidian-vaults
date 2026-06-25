# RAG Failure Modes

RAG failure mode — способ, которым RAG-система даёт плохой ответ из-за проблем в retrieval, chunking, контексте, генерации или evaluation.

## Core Principle

Многие RAG-ошибки начинаются до того, как [[LLM (Large Language Model)]] генерирует ответ. Если retrieved-контекст плохой, сильная модель всё равно может ответить плохо.

## Common Failure Modes

- poor retrieval: система не нашла нужные документы
- bad ranking: нужный chunk найден, но оказался слишком низко
- bad chunking: ответ разрезан между chunks
- context stuffing: в prompt добавлено слишком много нерелевантного контекста
- lost in the middle: важная информация спрятана в середине длинного контекста
- stale data: документы устарели
- embedding drift: сменился embedding model, корпус или язык запросов, и retrieval стал работать иначе
- source mismatch: модель ссылается на источник, который не поддерживает claim
- no abstention: система отвечает, даже когда evidence недостаточно
- evaluation gap: оценивается только финальный ответ, а не retrieval отдельно

## Fixes

- делать domain-aware chunking вместо случайного fixed-size splitting
- хранить metadata рядом с chunks
- использовать hybrid retrieval: dense vectors + keyword/BM25
- добавлять reranking перед передачей контекста в LLM
- измерять retrieval отдельно от generation
- version embeddings, indexes и chunking rules
- разрешить модели отвечать "не знаю по предоставленным документам"
- мониторить latency, groundedness и faithfulness

## Metrics

Retrieval:

- precision@k
- recall@k
- ranking quality
- context precision
- context recall

Generation:

- groundedness
- faithfulness
- citation correctness
- abstention quality

## Debug Checklist

1. Был ли нужный документ в corpus?
2. Попал ли нужный chunk в top-k?
3. Был ли chunk достаточно полным?
4. Не вытеснил ли релевантный chunk лишний контекст?
5. Были ли sources переданы модели явно?
6. Разрешено ли модели отказаться от ответа?
7. Измеряется ли retrieval отдельно от финального ответа?

## Related

- [[RAG]]
- [[Vector Database]]
- [[Embeddings]]
- [[Long Context Prompting]]
- [[Prompt Failure Modes]]
- [[Hallucinations]]

## Sources

- DigitalOcean: [Why RAG Systems Fail in Production](https://www.digitalocean.com/community/conceptual-articles/why-rag-systems-fail-in-production)
- arXiv: [Seven Failure Points When Engineering a Retrieval Augmented Generation System](https://arxiv.org/abs/2401.05856)
