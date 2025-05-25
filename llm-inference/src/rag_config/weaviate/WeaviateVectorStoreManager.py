import re
import os
import glob
import weaviate
from weaviate.classes.init import Auth
from llama_index.core import Document
from llama_index.vector_stores.weaviate import WeaviateVectorStore
from llama_index.core.indices.vector_store import VectorStoreIndex
from llama_index.core.service_context import ServiceContext
# from llama_index.core.storage_context import StorageContext
# from llama_index.core.node_parser import SimpleNodeParser

class WeaviateVectorStoreManager:
    def __init__(self, config):
        self.config = config
        self.weaviate_client = None
        self.llama_vector_store = None

    def load_vector_store(self):
        weaviate_url = self.config.get("weaviate_url")
        api_key = self.config.get("api_key")

        self.weaviate_client = weaviate.connect_to_weaviate_cloud(
            cluster_url=weaviate_url,
            auth_credentials=Auth.api_key(api_key),
        )

        print(self.weaviate_client.is_ready())

        self.llama_vector_store = WeaviateVectorStore(
            weaviate_client=self.weaviate_client,
            index_name="LlamaIndex"
        )

    def close(self):
        if self.weaviate_client:
            self.weaviate_client.close()

    def get_knowledge_base_document(self, path: str) -> list:
        local_files = glob.glob(os.path.join(path, "**", "*.txt"), recursive=True)
        documents = []

        for file_path in local_files:
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    text = file.read().strip()
                    documents.append(Document(
                        text=text,
                        metadata={
                            "file_name": os.path.basename(file_path)
                        }
                    ))
            except Exception as e:
                print(f"Error processing {file_path}: {e}")

        return documents
    
    def insert_document(self, documents: list[Document]):
        if not self.llama_vector_store:
            return

        storage_context = StorageContext.from_defaults(vector_store=self.llama_vector_store)
        service_context = ServiceContext.from_defaults()

        parser = SimpleNodeParser()
        nodes = parser.get_nodes_from_documents(documents)

        index = VectorStoreIndex([], storage_context=storage_context, service_context=service_context)
        index.insert_nodes(nodes)
    
    def reset_weaviate_vector_store(self):
        schema = self.weaviate_client.schema.get_schema()
        classes = schema.get("classes", [])

        if not classes:
            return

        for cls in classes:
            class_name = cls["class"]
            try:
                self.weaviate_client.schema.delete_class(name=class_name)
            except Exception as e:
                print(f"failed to delete class '{class_name}': {e}")