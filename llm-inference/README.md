.txt file → nodes → Weaviate vector store → query and retrieve

Retrieval-Augmented Generation (RAG) don`t work well with large blocks of text, need to split documents into smaller overlapping pieces (called nodes) before:
- Embedding them into vectors
- Indexing them in a vector store (Weaviate, Pinecone, Chroma)
- Retrieving the best chunks to answer user queries

Without Chunking
Retrieval is vague
Context is too big to process
Search is slow and inaccurate