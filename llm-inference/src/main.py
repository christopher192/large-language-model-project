import os
from dotenv import load_dotenv
from llama_index.core import Settings
from llama_index.core.schema import TextNode
from llama_index.core.storage import StorageContext
from llama_index.core.node_parser import LangchainNodeParser
from langchain.text_splitter import RecursiveCharacterTextSplitter
from llama_index.core.indices.vector_store import VectorStoreIndex
from rag_config.weaviate import WeaviateVectorStoreManager
from llm_config import EmbeddingModelBuilder

def main():
    load_dotenv()

    config = {
        "weaviate_url": os.getenv('WEAVIATE_URL'),
        "api_key": os.getenv('WEAVIATE_API_KEY')
    }

    knowledge_base_path = "../data/chatbot_knowledge_base/" 

    manager = WeaviateVectorStoreManager(config=config)
    manager.load_vector_store()

    documents = manager.get_knowledge_base_document(knowledge_base_path)
    print(f"loaded {len(documents)} documents.")

    storage_context = StorageContext.from_defaults(vector_store=manager.llama_vector_store)
    
    embedding_model_manager = EmbeddingModelBuilder(config)
    embedding_model = embedding_model_manager.initialize("huggingface")

    # replace ServiceContext with llama_index.core.Settings
    Settings.embedding_model = embedding_model
    
    parser = LangchainNodeParser(
        RecursiveCharacterTextSplitter(
            is_separator_regex=True, separators=['\n\n', '(?<=[.!?])'], 
            chunk_size=1000, 
            chunk_overlap=0
        )
    )

    node = []

    for id, document in enumerate(documents):
        chunk = parser.get_nodes_from_documents([document])
        filename = document.metadata['file_name']

        for idx, chunk in enumerate(chunk):
            chunk_metadata = chunk.metadata or {}
            chunk_metadata.update({'file_name': filename})

            text_node = TextNode(
                text=chunk.text,
                metadata=chunk_metadata
            )

            node.append(text_node)
    
    print('total node:', len(node))
    index = VectorStoreIndex([], storage_context=storage_context)
    # manager.insert_documents(documents)

    batch_size = 5000

    for i in range(0, len(node), batch_size):
        batch = node[i : i + batch_size]
        index.insert_nodes(batch)

    manager.close()
    
if __name__ == "__main__":
    main()