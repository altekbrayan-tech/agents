import os
from crewai import Task, Crew
from agentes_libreria import obtener_arquitecto, obtener_desarrollador

def ejecutar_mision_desde_archivo():
    print("\n--- 🚀 INICIANDO FÁBRICA DE SOFTWARE ---")
    
    nombre_archivo = "prompt_crm.txt"
    
    if not os.path.exists(nombre_archivo):
        print(f"❌ Error: No encuentro el archivo {nombre_archivo}")
        return

    # Leer el prompt completo desde el archivo
    with open(nombre_archivo, "r", encoding="utf-8") as f:
        instruccion_completa = f.read()

    proyecto = "CRM_Soluciones_Hidraulicas"
    if not os.path.exists(proyecto):
        os.makedirs(proyecto)

    # Cargar agentes desde tu librería
    arq = obtener_arquitecto()
    dev = obtener_desarrollador()

   # Modificación en fabrica.py para mayor detalle
    t1 = Task(
        description=f"Diseñar ÚNICAMENTE el modelo de datos PostgreSQL y la lógica de incremento IPC en C# para: {instruccion_completa}",
        expected_output="Código SQL de tablas y Clase C# de cálculo IPC.",
        agent=arq
    )
    
    t2 = Task(
        description="Crear los Controllers de .NET 10 para la gestión de tareas, bitácoras y carga de fotos.",
        expected_output="Archivos .cs completos con endpoints de Swagger.",
        agent=dev,
        context=[t1]
    )

    t3 = Task(
        description="Diseñar el flujo de n8n (JSON) para las alertas de 15 días y el brochure mensual.",
        expected_output="Archivo JSON compatible con n8n.",
        agent=dev, # O puedes crear un agente experto en n8n
        context=[t1]
    )

    # El Crew ejecutando en tu servidor Xeon
    equipo = Crew(agents=[arq, dev], tasks=[t1, t2], verbose=True)
    
    print(f"⏳ Procesando requerimiento extenso en el servidor...")
    resultado = equipo.kickoff()

    # Guardar en la carpeta del proyecto
    ruta_resultado = f"{proyecto}/diseño_final.md"
    with open(ruta_resultado, "w", encoding="utf-8") as f:
        f.write(str(resultado))
    
    print(f"\n✅ ¡Éxito! Todo el diseño se ha guardado en: {ruta_resultado}")

if __name__ == "__main__":
    ejecutar_mision_desde_archivo()