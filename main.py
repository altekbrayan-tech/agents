from agents import backend_agent, frontend_agent, qa_agent, docs_agent
from crewai import Task, Crew

# FASE 1: DESARROLLO DE LA API (Back-End)
task_backend = Task(
    description=(
        "Crea el esquema de una API de Autenticación en .NET 10 usando C#. "
        "Debe incluir JWT, manejo de roles y conexión a PostgreSQL."
    ),
    expected_output="Código completo de los Controllers, Models y el Program.cs en .NET 10.",
    agent=backend_agent
)

# FASE 2: DESARROLLO DE LA INTERFAZ (Front-End)
task_frontend = Task(
    description=(
        "Basado en la API del Backend, crea un formulario de Login en React. "
        "Usa Tailwind CSS para el diseño y maneja el estado del token con Hooks."
    ),
    expected_output="Componente Login.jsx y lógica de consumo de API en Node/React.",
    agent=frontend_agent,
    context=[task_backend] # El Front sabe qué endpoints creó el Back
)

# FASE 3: CONTROL DE CALIDAD (QA)
task_qa = Task(
    description="Escribe las pruebas unitarias en xUnit para el Backend y en Jest para el Frontend.",
    expected_output="Scripts de testeo y reporte de posibles errores detectados.",
    agent=qa_agent,
    context=[task_backend, task_frontend]
)

# FASE 4: DOCUMENTACIÓN TÉCNICA
task_docs = Task(
    description="Genera el archivo README.md del proyecto y la especificación OpenAPI (Swagger).",
    expected_output="Documentación técnica completa lista para el equipo de desarrollo.",
    agent=docs_agent,
    context=[task_backend, task_frontend, task_qa]
)

# ORQUESTACIÓN DEL EQUIPO
squad_desarrollo = Crew(
    agents=[backend_agent, frontend_agent, qa_agent, docs_agent],
    tasks=[task_backend, task_frontend, task_qa, task_docs],
    verbose=True # Para que veas en consola cómo razona cada agente
)

# ¡A TRABAJAR!
print("--- Iniciando proceso de desarrollo autónomo ---")
resultado_final = squad_desarrollo.kickoff()

print("\n\n################################################")
print("RESULTADO DEL SPRINT:")
print(resultado_final)