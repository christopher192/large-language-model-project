from langchain.chat_models import ChatOpenAI

def get_openai_llm(api_key: str, model: str = "gpt-3.5-turbo", temperature: float = 0.7):
    return ChatOpenAI(
        model=model,
        temperature=temperature,
        api_key=api_key,
    )

def get_original_openai_llm_with_context(api_key: str, context: str, model: str = "gpt-3.5-turbo"):
    return ""