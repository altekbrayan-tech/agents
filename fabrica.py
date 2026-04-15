import os
from crewai import Task, Crew
from agentes_libreria import obtener_arquitecto, obtener_desarrollador

def ejecutar_mision_desde_archivo():
    print("\n--- 🚀 INICIANDO FÁBRICA DE SOFTWARE ---")
    
    nombre_archivo = "prompt_crm.txt"
    proyecto = "CRM_Soluciones_Hidraulicas"
    
    if not os.path.exists(nombre_archivo):
        print(f"❌ Error: No encuentro el archivo {nombre_archivo}")
        return

    # 1. Leer el prompt completo
    with open(nombre_archivo, "r", encoding="utf-8") as f:
        instruccion_completa = f.read()

    # 2. Crear carpeta del proyecto si no existe
    if not os.path.exists(proyecto):
        os.makedirs(proyecto)

    # 3. Cargar agentes
    arq = obtener_arquitecto()
    dev = obtener_desarrollador()

    # 4. Definir Tareas con salida a archivos individuales
    t1 = Task(
        description=f"Escribir el script SQL para PostgreSQL y las Entidades en C# (.NET 10) basadas en: {instruccion_completa}",
        expected_output="Contenido completo de Database.sql y Models.cs sin omisiones.",
        agent=arq,
        output_file=f"{proyecto}/Infraestructura.cs"
    )
    
    t2 = Task(
        description="Escribir el ApplicationDbContext.cs y el ConjuntosController.cs con la lógica de IPC completa.",
        expected_output="Código C# funcional, incluyendo el endpoint de incremento de IPC.",
        agent=dev,
        context=[t1],
        output_file=f"{proyecto}/Controladores.cs"
    )

    # 5. Configurar el equipo (Crew)
    equipo = Crew(
        agents=[arq, dev], 
        tasks=[t1, t2], 
        verbose=True
    )
    
    print(f"⏳ Procesando requerimiento extenso en el servidor...")
    resultado = equipo.kickoff()

    # 6. Guardar resumen final
    ruta_resultado = f"{proyecto}/diseño_final.md"
    with open(ruta_resultado, "w", encoding="utf-8") as f:
        f.write(str(resultado))
    
    print(f"\n✅ ¡Éxito! Todo el diseño se ha guardado en: {ruta_resultado}")

# 7. Ejecución principal (asegúrate de que esté pegado al margen izquierdo)
if __name__ == "__main__":
    ejecutar_mision_desde_archivo()