import config
from groq import Groq

try:
    if hasattr(config, 'GROQ_API_KEY') and config.GROQ_API_KEY and config.GROQ_API_KEY != "your_groq_api_key_here":
        client = Groq(api_key=config.GROQ_API_KEY)
        print("Successfully connected to Groq API.")
        print("Available models:")
        models = client.models.list()
        for m in models.data:
            print(f"- {m.id}")
    else:
        print("No valid GROQ_API_KEY found in config.")
except Exception as e:
    print(f"Error listing models: {e}")
