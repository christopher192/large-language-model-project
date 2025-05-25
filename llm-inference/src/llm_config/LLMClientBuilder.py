import os
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI, AzureChatOpenAI, BedrockChat, ChatAnyscale

load_dotenv()

class LLMClientBuilder:
    @staticmethod
    def initialize(llm_type: str = "gpt-35", llm_provider: str = "azure", streaming: bool = False) -> str:
        return 'test'