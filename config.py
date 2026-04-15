from crewai import LLM

# Configuración corregida para tu modelo local en el Xeon
local_llm = LLM(
    model="ollama/deepseek-coder-v2:lite",
    base_url="http://192.168.0.177:11434",
    temperature=0.2, # Menos creatividad, más precisión
    max_tokens=8000, # Asegúrate de que tu modelo soporte esto
)