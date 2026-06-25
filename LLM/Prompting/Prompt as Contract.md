# Prompt as Contract

Хороший prompt — это не магическая фраза, а контракт между пользователем и моделью.

## Contract Structure

```text
goal -> context -> constraints -> output format -> uncertainty rules
```

## Key Parts

- goal: что нужно сделать
- context: на какие данные опираться
- constraints: чего избегать
- output format: как должен выглядеть ответ
- uncertainty rules: что делать, если данных не хватает

## Why It Matters

[[LLM (Large Language Model)]] предсказывает следующий токен на основе контекста. Чем яснее контракт, тем меньше пространства для нежелательных продолжений: лишних допущений, неправильного формата или выдуманных фактов.

## Example

Weak prompt:

```text
Explain this document.
```

Stronger prompt:

```text
Summarize the document for a technical reader.
Use 5 bullet points.
Only use facts from the provided context.
If the context is insufficient, say what is missing.
```

## Related

- [[Prompt Engineering]]
- [[System Prompt]]
- [[Hallucinations]]
- [[No Ground Truth]]
