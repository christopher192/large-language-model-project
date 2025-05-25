.txt file → nodes → Weaviate vector store → query and retrieve

Retrieval-Augmented Generation (RAG) don`t work well with large blocks of text, need to split documents into smaller overlapping pieces (called nodes) before:
- Embedding them into vectors
- Indexing them in a vector store (Weaviate, Pinecone, Chroma)
- Retrieving the best chunks to answer user queries

Without Chunking
Retrieval is vague
Context is too big to process
Search is slow and inaccurate

Use Case	chunk_size	chunk_overlap
General text documents	512	50
FAQs / Short entries	256	30
Long form articles	1024	100

