# Prompt Failure Modes

Prompt failure mode — повторяющийся способ, которым [[LLM (Large Language Model)]] даёт плохой ответ из-за слабой инструкции, плохого контекста или неясных критериев успеха.

## Common Failure Modes

- wrong format: ответ не соответствует нужной структуре
- hallucination: модель придумывает факты
- vague answer: ответ слишком общий
- ignored constraints: модель пропускает часть ограничений
- context mixing: модель смешивает разные источники
- over-answering: модель добавляет лишнее
- under-answering: модель не раскрывает важные детали
- hidden assumptions: модель делает неявные допущения
- unstable answers: ответы меняются из-за высокой случайности или плавающего контекста
- source leakage: модель использует внешние знания, хотя должна отвечать только по контексту

## Common Causes

- "model is bad" часто означает слабую инструкцию, плохой контекст или неподходящие параметры
- уверенная ложь часто возникает без правила "if not found, say so"
- разные ответы часто связаны с высокой [[Sampling Parameters|temperature]] или меняющимся retrieved-контекстом
- высокий temperature не делает модель умнее, а делает генерацию менее предсказуемой

## How To Debug

1. Проверить, есть ли явная цель.
2. Проверить, есть ли нужный контекст.
3. Проверить, указан ли формат ответа.
4. Проверить, есть ли ограничения.
5. Проверить, сказано ли, что делать при нехватке данных.
6. Проверить [[Sampling Parameters]].

## Practical Exercise

Взять один плохой prompt и переписать его в двух вариантах:

- short and vague
- explicit contract: goal, context, constraints, format, uncertainty rules

Сравнить ответы по заранее заданным success criteria.

## Related

- [[Prompt Engineering]]
- [[Prompt as Contract]]
- [[Sampling Parameters]]
- [[Hallucinations]]
- [[Pattern Conflict]]
