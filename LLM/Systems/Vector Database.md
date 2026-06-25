# Vector Database

Vector database — это база данных для хранения и поиска [[Embeddings|vector embeddings]].

## Why It Exists

Обычная база данных хорошо ищет по точным значениям. Vector database нужна для similarity search: найти объекты, которые близки по смыслу, даже если слова не совпадают буквально.

## In RAG

В [[RAG]] vector database обычно хранит embeddings для chunks документов.

Query flow:

```text
user query -> query embedding -> nearest neighbor search -> relevant chunks
```

## What It Stores

- vector: числовое представление chunk
- text: исходный фрагмент
- metadata: file, section, URL, timestamp, permissions, tags
- ids: стабильные идентификаторы документов и chunks

## Why Metadata Matters

Metadata помогает:

- фильтровать документы по пользователю, проекту или дате
- показывать источники в ответе
- переиндексировать документы
- отлаживать плохой retrieval
- соблюдать permissions

## Related

- [[RAG]]
- [[Embeddings]]
- [[RAG Failure Modes]]
- [[Context Window]]

## Sources

- Pinecone: [What are Vector Embeddings](https://www.pinecone.io/learn/vector-embeddings/)
