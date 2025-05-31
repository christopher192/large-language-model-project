from .deepseek_wrapper import ChatDeepSeekWrapper
from .openai_wrapper import ChatOpenAIWrapper

class LLMFactory:
    def __init__(self, provider: str, framework: str, model: str, api_key: str,  temperature: float = 0.7):
        self.provider = provider
        self.framework = framework
        self.model = model
        self.api_key = api_key
        self.temperature = temperature
    
    def get_llm(self):
        if self.provider == "openai":
            return ChatOpenAIWrapper(
                framework=self.framework,
                model=self.model,
                api_key=self.api_key,
                temperature=self.temperature
            )
        elif self.provider == "deepseek":
            return ChatDeepSeekWrapper(
                framework=self.framework,
                model=self.model,
                api_key=self.api_key,
                temperature=self.temperature
            )
        else:
            raise ValueError(f"Unsupported provider: {self.provider}")