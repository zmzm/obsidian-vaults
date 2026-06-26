# Embeddings

Embeddings — это преобразование текста, токенов или других объектов в векторное пространство.

Позволяет:
- измерять "смысловую близость"
- работать с текстом математически
- искать похожие документы через similarity search
- строить [[RAG]] и semantic search

## Intuition

Модель embedding превращает объект в список чисел. Если два объекта близки по смыслу, их vectors должны находиться близко друг к другу в vector space.

Для текста это позволяет искать не только по точному совпадению слов, но и по смысловой близости.

## In RAG

В [[RAG]] embeddings используются дважды:

1. документы разбиваются на chunks и превращаются в vectors
2. пользовательский query тоже превращается в vector

Затем [[Vector Database]] ищет chunks, чьи vectors ближе всего к query vector.

## Limitations

- semantic similarity не равна истинности
- похожий chunk не всегда содержит ответ
- embedding model может плохо работать с доменными терминами
- смена embedding model может изменить результаты retrieval

## Related

- [[Tokenization]]
- [[Transformer]]
- [[Vector Database]]
- [[RAG]]
- [[RAG Failure Modes]]

## Sources

- Pinecone: [What are Vector Embeddings](https://www.pinecone.io/learn/vector-embeddings/)
