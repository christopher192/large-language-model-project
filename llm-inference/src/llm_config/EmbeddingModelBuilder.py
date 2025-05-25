from llama_index.embeddings.azure_openai import AzureOpenAIEmbedding
from llama_index.embeddings.huggingface import HuggingFaceEmbedding

class EmbeddingModelBuilder:
    def __init__(self, config):
        self.config = config

    def initialize(self, provider):
        if provider == "azure":
            return AzureOpenAIEmbedding(
                model=self.config["azure_openai_embedding_model_name"],
                deployment_name=self.config["azure_openai_embedding_deployment_name"],
                api_key=self.config["azure_openai_api_key"],
                azure_endpoint=self.config["azure_endpoint_url"],
                api_version=self.config["azure_openai_embedding_model_api_version"]
            )
        elif provider == "huggingface":
            return HuggingFaceEmbedding() # default: all-MiniLM-L6-v2
        else:
            raise ValueError(f"Unsupported embedding provider: {provider}")