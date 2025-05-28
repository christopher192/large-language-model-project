import os
from dotenv import load_dotenv
from rag_config.weaviate import WeaviateVectorStoreManager

def main():
    load_dotenv()

    config = {
        "weaviate_url": os.getenv('WEAVIATE_URL'),
        "api_key": os.getenv('WEAVIATE_API_KEY')
    }

    knowledge_base_path = "../data/chatbot_knowledge_base/" 

    manager = WeaviateVectorStoreManager(config=config)
    manager.load_vector_store()
    manager.reset_weaviate_vector_store()

    # documents = manager.get_knowledge_base_document(knowledge_base_path)
    # print(f"loaded {len(documents)} documents.")

    # manager.insert_document(documents)
    # manager.close()
    
if __name__ == "__main__":
    main()