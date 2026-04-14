from crewai import LLM

# Configuración para usar tu modelo local de Ollama
local_llm = LLM(
    model="ollama/deepseek-coder-v2:lite",
    base_url="http://192.168.0.177:11434", # Asegúrate de que Ollama esté abierto
    config={
        "num_predict": 4096, # Esto le da permiso de escribir respuestas mucho más largas
        "temperature": 0.2    # Menos creatividad, más precisión técnica
    }
)