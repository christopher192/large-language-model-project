import openai
from langchain_deepseek import ChatDeepSeek

class ChatDeepSeekWrapper():
    def __init__(self, framework: str, api_key: str, model: str = "deepseek-chat", temperature: float = 0.7):
        self.framework = framework
        self.api_key = api_key
        self.model = model
        self.temperature = temperature
    
    def langchain_deekseek(self):
        # Create an instance of ChatDeepSeek from langchain_deepseek
        return ChatDeepSeek(
            model=self.model,
            api_key=self.api_key,
            temperature=self.temperature
        )

    def chat(self, system_prompt: str, user_prompt: str) -> str:
        if self.framework == "langchain":
             # Create an instance of ChatDeepSeek from langchain_deepseek
            deekseek_llm = self.langchain_deekseek()
            # Define the system and human prompts
            messages = [
                (
                    "system",
                    system_prompt,
                ),
                ("human", user_prompt),
            ]
            ai_msg = deekseek_llm.invoke(messages)
            response_content = ai_msg.content
            return response_content

        # Fallback return statement if the provider is not "langchain"
        return "Invalid provider type."