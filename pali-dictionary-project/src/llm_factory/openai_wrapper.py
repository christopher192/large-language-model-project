import uuid
import datetime
from openai import OpenAI

class ChatOpenAIWrapper():
    def __init__(self, framework: str, api_key: str, model: str = "openai", temperature: float = 0.7):
        self.framework = framework
        self.api_key = api_key
        self.model = model
        self.temperature = temperature

    def generate_unique_id(user_id):
        timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S") # Format: YYYYMMDDHHMMSS
        unique_str = uuid.uuid4().hex
        return f"{user_id}-{timestamp}-{unique_str}"

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

    def batch_processing(self, system_prompt: str, user_prompt: str, batch_input: list[dict]) -> list[dict]:
        if self.framework == "original":
            # Overwrite the file with nothing
            with open(self.jsonl_filepath, "w") as f:
                # pass
                f.write("")

        # Return empty list if framework doesn't match
        return []