# RAG

RAG, Retrieval-Augmented Generation, — это паттерн, где [[LLM (Large Language Model)]] отвечает не только из своих весов, а получает внешний контекст из документов, базы знаний или поиска.

## Core Idea

LLM сама по себе не знает актуальные или приватные данные. RAG добавляет шаг retrieval: сначала система находит релевантные фрагменты, затем модель генерирует ответ на их основе.

## Basic Pipeline

```text
documents -> chunks -> embeddings -> vector database
user query -> query embedding -> retrieval -> context -> LLM answer
```

## Components

- documents: исходные файлы, страницы, заметки, тикеты или записи
- chunks: небольшие фрагменты документов
- [[Embeddings]]: числовое представление текста
- [[Vector Database]]: хранилище и поиск похожих векторов
- retriever: выбирает релевантные chunks
- reranker: переупорядочивает кандидатов по качеству
- generator: LLM формирует ответ по найденному контексту

## Why It Helps

- даёт модели доступ к внешним знаниям
- снижает риск [[Hallucinations]]
- позволяет ссылаться на источники
- помогает работать с приватными и обновляемыми данными
- дешевле и гибче, чем fine-tuning для часто меняющейся базы знаний

## Important Limitation

RAG не делает ответ автоматически правильным. Если retrieval нашёл плохие, старые или неполные chunks, LLM может дать слабый ответ даже при хорошем prompt.

## Good RAG Answer

Хороший RAG-ответ должен:

- быть основан на retrieved-контексте
- ссылаться на источники
- признавать нехватку данных
- не смешивать внешние знания с документами, если это запрещено
- не превращать слабые evidence в уверенный ответ

## Related

- [[RAG Failure Modes]]
- [[Long Context Prompting]]
- [[Prompt as Contract]]
- [[Sampling Parameters]]
- [[Context Window]]
- [[Hallucinations]]

## Sources

- Pinecone: [What are Vector Embeddings](https://www.pinecone.io/learn/vector-embeddings/)
- DigitalOcean: [Why RAG Systems Fail in Production](https://www.digitalocean.com/community/conceptual-articles/why-rag-systems-fail-in-production)
- arXiv: [Seven Failure Points When Engineering a Retrieval Augmented Generation System](https://arxiv.org/abs/2401.05856)
