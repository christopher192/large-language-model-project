import os
from dotenv import load_dotenv
from llama_index.core import Settings
from llama_index.core.storage import StorageContext
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

    Settings.embedding_model = embedding_model
  
    # print(embedding_model.get_query_embedding('Hello world!'))

    # manager.insert_documents(documents)
    manager.close()
    
if __name__ == "__main__":
    main()