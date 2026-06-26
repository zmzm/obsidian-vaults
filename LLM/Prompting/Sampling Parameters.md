# Sampling Parameters

Sampling parameters управляют тем, насколько предсказуемой или вариативной будет генерация [[LLM (Large Language Model)]].

## Temperature

Temperature влияет на то, как часто модель выбирает менее вероятные токены.

- low temperature: стабильнее, предсказуемее, удобнее для factual tasks
- high temperature: разнообразнее, креативнее, менее предсказуемо

Для factual QA, extraction, coding assistant и [[RAG]] обычно лучше низкая temperature.

## Intuition

| Temperature | Behavior |
| --- | --- |
| 0 | максимально детерминированно |
| 0.1-0.3 | стабильно, хорошо для фактов и RAG |
| 0.5-0.7 | баланс стабильности и вариативности |
| 1+ | больше креатива, выше риск нестабильности |

## Top-p

Top-p ограничивает выбор токенов вероятностной массой. Например, `top_p = 0.9` означает, что модель выбирает из набора токенов, которые вместе покрывают 90% вероятности.

Обычно не стоит активно менять и temperature, и top-p одновременно. Лучше выбрать один главный рычаг случайности.

## Practical Defaults

Для AI engineering copilot: RAG, факты, код.

```json
{
  "temperature": 0.2,
  "top_p": 0.9,
  "max_tokens": 500,
  "presence_penalty": 0,
  "frequency_penalty": 0
}
```

## Important Note

Низкая temperature не гарантирует истинность. Она снижает случайность, но модель всё ещё может ошибаться, если контекст неполный, prompt слабый или задача требует данных, которых нет.

## Questions

- Почему низкая temperature важна для RAG?
- Чем temperature отличается от top-p?
- Какие параметры стоит изменить для creative mode?
- Почему повторяемость ответа важна для debugging?

## Sources

- OpenAI Help Center: [Best practices for prompt engineering with the OpenAI API](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-the-openai-api)

## Related

- [[Prompt Engineering]]
- [[Long Context Prompting]]
- [[RAG]]
- [[Hallucinations]]
- [[Prompt Failure Modes]]
