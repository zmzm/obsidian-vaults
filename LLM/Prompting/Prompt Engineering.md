# Prompt Engineering

Prompt engineering — это способ управлять поведением [[LLM (Large Language Model)]] через инструкции, контекст, ограничения и формат ответа.

## What It Can Improve

- формат ответа
- стиль и тон
- уровень детализации
- порядок решения задачи
- явное следование ограничениям
- отказ от ответа при нехватке данных

## What It Does Not Fix

- высокая latency
- стоимость модели
- отсутствие нужных данных
- слабая архитектура приложения
- слишком маленькое [[Context Window]]
- ограничения самой модели

Если проблема связана с доступом к данным, архитектурой или производительностью, prompt может только частично смягчить эффект. Часто нужен другой дизайн системы: [[RAG]], инструменты, кэширование, выбор другой модели или fine-tuning.

## Success Criteria

Перед улучшением prompt нужно определить, что считается хорошим ответом:

- правильность
- полнота
- формат
- стиль
- наличие источников
- способность сказать "не знаю"

Без success criteria prompt engineering превращается в субъективное перебирание формулировок.

## OpenAI Rules of Thumb

- формулировать задачу как инструкцию, а не просто вопрос
- ставить инструкции в начало prompt
- отделять инструкции от контекста явными разделителями: `###`, `"""`, XML-теги или блоки `Context / Task / Question`
- явно задавать желаемый формат ответа
- заменять расплывчатые требования измеримыми: не "short", а "3-5 sentences"
- вместо одного запрета объяснять, что делать вместо запрещённого поведения
- начинать с zero-shot, затем пробовать few-shot, и только потом думать о fine-tuning

## Debugging Heuristic

Если ответ плохой, сначала стоит проверить prompt, контекст и параметры генерации, а не сразу менять модель. Это не строгий закон, но полезный порядок диагностики.

## Sources

- OpenAI Help Center: [Best practices for prompt engineering with the OpenAI API](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-the-openai-api)

## Related

- [[Prompt as Contract]]
- [[System Prompt]]
- [[Long Context Prompting]]
- [[Sampling Parameters]]
- [[Prompt Failure Modes]]
- [[LLM Capabilities]]
- [[Hallucinations]]
