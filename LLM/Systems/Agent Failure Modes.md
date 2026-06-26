# Agent Failure Modes

Agent failure mode — способ, которым агентная система ломается из-за слабых инструкций, плохих tools, чрезмерной автономии, отсутствия guardrails или плохой observability.

## Common Failure Modes

- tool confusion: агент выбирает неправильный tool
- tool overuse: агент вызывает tools без необходимости
- tool underuse: агент отвечает из головы, хотя должен был проверить данные
- loop drift: агент уходит в длинную цепочку без прогресса
- weak exit condition: агент не понимает, когда остановиться
- context loss: важная информация теряется между шагами
- bad handoff: multi-agent система передаёт задачу не тому агенту
- action risk: агент выполняет действие без подтверждения
- hidden failure: финальный ответ выглядит нормально, но intermediate steps были плохими
- cost/latency explosion: слишком много LLM calls, tool calls или reranking steps

## Causes

- слишком общий [[System Prompt]]
- tools плохо описаны
- нет строгих schemas
- нет tracing
- нет evals
- слишком рано построена multi-agent architecture
- нет human approval для опасных действий
- нет лимита turns, tool calls или cost

## Fixes

- начинать с single-agent или workflow
- писать tools как стабильный API для модели
- добавлять clear exit conditions
- ограничивать risky actions через approval
- логировать raw transcripts и tool calls
- измерять accuracy, latency, tool errors, token usage
- разделять data tools и action tools
- использовать guardrails на input, tool use и output

## Debug Checklist

1. Понятна ли agent goal?
2. Есть ли у agent нужный context?
3. Не слишком ли много похожих tools?
4. Видно ли в trace, почему был выбран tool?
5. Есть ли лимит шагов?
6. Есть ли правило остановки?
7. Нужен ли здесь agent, или хватит workflow?

## Related

- [[Agents]]
- [[Agent Tool Use]]
- [[Prompt Failure Modes]]
- [[RAG Failure Modes]]
- [[System Prompt]]

## Sources

- OpenAI: [A practical guide to building agents](https://openai.com/business/guides-and-resources/a-practical-guide-to-building-ai-agents/)
- Anthropic: [Building effective agents](https://www.anthropic.com/engineering/building-effective-agents)
- Anthropic: [Writing effective tools for AI agents](https://www.anthropic.com/engineering/writing-tools-for-agents)
