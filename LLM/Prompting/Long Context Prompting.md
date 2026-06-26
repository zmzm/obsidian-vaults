# Long Context Prompting

Long context prompting — это проектирование prompt для задач, где модель получает большой объём документов, chunk'ов или истории.

## Core Pattern

Для длинного контекста часто полезен порядок:

```text
context -> instructions -> question
```

Идея: сначала дать модели материалы, затем правила обработки, затем конкретный вопрос.

## For RAG

В [[RAG]] retrieved-контекст лучше передавать явно структурированными блоками:

```text
<document id="source-1" title="...">
...
</document>

<document id="source-2" title="...">
...
</document>
```

Каждый chunk должен иметь источник:

- filename
- section
- URL или document id
- timestamp, если важна актуальность

## Why It Matters

Без явной структуры модель может смешивать документы, терять источники или отвечать слишком общо. Хорошая разметка снижает риск [[Hallucinations]] и улучшает цитирование.

## Checklist

- контекст расположен выше вопроса
- chunks отделены друг от друга
- у каждого chunk есть source id
- инструкции явно говорят, можно ли использовать внешние знания
- есть правило для случая, когда контекст не содержит ответа

## RAG Prompt Template

System:

```text
You are an AI engineering assistant.

Rules:
- Use only the provided context.
- If the answer is not present in the context, say so explicitly.
- Do not guess or fill missing information.
- Provide sources for factual claims.
```

User:

```text
Context:
[doc_id=1 | file=README.md]
...

[doc_id=2 | file=ADR.md]
...

Task:
Answer the question using only the context above.

Question:
<user question>
```

## Related

- [[Context Window]]
- [[RAG]]
- [[Prompt Engineering]]
- [[Sampling Parameters]]
- [[Hallucinations]]
