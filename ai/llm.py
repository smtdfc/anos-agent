from langchain_google_genai import ChatGoogleGenerativeAI

providers ={
  "google":[
    "gemini-2.5-flash"
  ]
}

def get_llm_model(provider:str,model_name:str)-> any:
  if not providers.get(provider, None):
    raise Exception(f'Unsupport provider {provider}')
  
  if model_name not in providers.get(provider, None):
    raise Exception(f'Provider {provider} unsupported model {model_name} !')

  if provider == 'google':
    return ChatGoogleGenerativeAI(model=model_name, temperature=0.7)
