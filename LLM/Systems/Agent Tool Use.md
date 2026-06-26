# Agent Tool Use

Tools расширяют возможности [[Agents|agent]]: модель может не только отвечать текстом, но и искать данные, читать файлы, вызывать API, писать в базы или запускать код.

## Tool Types

- data tools: retrieval, search, database query, file reading
- action tools: send message, create ticket, update record, run command
- orchestration tools: call another agent, handoff, start workflow
- verification tools: tests, linters, validators, schema checks

## Good Tool Design

Хороший tool должен быть понятен модели:

- ясное имя
- короткое описание
- строгая schema параметров
- примеры допустимых inputs
- предсказуемый output
- понятные ошибки
- минимум скрытых side effects

## Tool Choice

Agent должен понимать:

- когда tool нужен
- когда tool не нужен
- какие параметры передать
- что делать при ошибке
- как использовать результат tool call

Если tools похожи друг на друга или плохо описаны, агент начинает выбирать неправильный tool или делать лишние вызовы.

## Observability

Для tool use нужно логировать:

- какие tools были вызваны
- с какими параметрами
- сколько занял вызов
- сколько было ошибок
- сколько токенов потрачено
- помог ли tool приблизиться к ответу

Без tracing agent трудно отлаживать: финальный ответ скрывает, где именно сломалась цепочка.

## Related

- [[Agents]]
- [[Agent Failure Modes]]
- [[RAG]]
- [[Vector Database]]

## Sources

- OpenAI: [A practical guide to building agents](https://openai.com/business/guides-and-resources/a-practical-guide-to-building-ai-agents/)
- Anthropic: [Writing effective tools for AI agents](https://www.anthropic.com/engineering/writing-tools-for-agents)
