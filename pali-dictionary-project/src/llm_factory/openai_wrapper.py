from openai import OpenAI

class ChatOpenAIWrapper():
    def __init__(self, framework: str, api_key: str, model: str = "openai", temperature: float = 0.7):
        self.framework = framework
        self.api_key = api_key
        self.model = model
        self.temperature = temperature

    def chat(self, system_prompt: str, user_prompt: str) -> str:
        if self.framework == "original":
            openai = OpenAI(
                api_key=self.api_key
            )
            response = openai.chat.completions.create(
                model=self.model,
                messages=[
                    {
                        "role": "system", 
                        "content": system_prompt
                    },
                    {
                        "role": "user", 
                        "content": user_prompt
                    }
                ],
                max_tokens=1000
            )
            response_text = response.choices[0].message.content
            return response_text

        # Fallback return statement if the provider is not recognized
        return "Invalid provider type."