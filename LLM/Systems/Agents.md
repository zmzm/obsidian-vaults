# Agents

Agent — это LLM-система, которая может выполнять многошаговую задачу с некоторой степенью самостоятельности: читать контекст, выбирать tools, делать действия, проверять результат и продолжать до exit condition.

## Core Idea

Обычный prompt обычно даёт один ответ. Agent работает как loop:

```text
goal -> plan -> tool call -> observation -> next step -> final answer
```

Ключевое отличие не в том, что модель "умнее", а в том, что она получает:

- инструкции
- tools
- память или контекст
- возможность делать несколько шагов
- правила остановки
- guardrails

## Agent vs Workflow

Workflow:

- путь заранее задан кодом
- шаги предсказуемы
- проще тестировать
- лучше для стабильных бизнес-процессов

Agent:

- модель сама выбирает часть пути
- полезен для неоднозначных задач
- может выбирать tools динамически
- сложнее контролировать и отлаживать

Практическое правило: сначала пробовать простой workflow или single-agent. Multi-agent нужен только если сложность действительно оправдана.

## Basic Components

- [[System Prompt]]: роль, правила, ограничения
- tools: функции, API, поиск, файлы, browser, database
- [[RAG]]: внешний контекст и знания
- memory: сохранённое состояние или история
- planner: выбор следующих шагов
- executor: выполнение tool calls
- evaluator: проверка результата
- guardrails: ограничения и проверки безопасности
- tracing: запись шагов, tool calls и ошибок

## When Agents Help

- задача многошаговая
- нужна работа с tools
- нужна адаптация к промежуточным результатам
- входные данные неструктурированы
- невозможно заранее прописать все ветки workflow
- нужен research, debugging, coding или operations assistant

## When Not To Use Agents

- задача решается одним LLM call
- можно написать простой deterministic workflow
- latency и стоимость критичны
- нельзя допускать самостоятельные действия
- нет evals, logs или human approval для рискованных операций

## Single-Agent First

Single-agent system часто проще и надёжнее:

```text
user task -> one agent with tools -> loop until final answer
```

Multi-agent стоит рассматривать, если:

- один prompt стал слишком сложным
- tools пересекаются и модель путается
- нужны разные роли или политики
- есть явные независимые подзадачи
- нужен manager-worker или handoff pattern

## Related

- [[Agent Tool Use]]
- [[Agent Failure Modes]]
- [[System Prompt]]
- [[Prompt as Contract]]
- [[RAG]]
- [[Sampling Parameters]]

## Sources

- OpenAI: [A practical guide to building agents](https://openai.com/business/guides-and-resources/a-practical-guide-to-building-ai-agents/)
- Anthropic: [Building effective agents](https://www.anthropic.com/engineering/building-effective-agents)
