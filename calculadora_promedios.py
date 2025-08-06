def ingresar_calificaciones():
    
    nombres_materias = []
    calificaciones_materias = []
    
    while True:
        materia = input("Ingrese el nombre de la materia: ")
        
        while True:
            try:
                calificacion = float(input(f"Ingrese la calificación para {materia} (0-10): "))
                if 0 <= calificacion <= 10:
                    break
                else:
                    print("Error: La calificación debe estar entre 0 y 10.")
            except ValueError:
                print("Error: Por favor, ingrese un número válido.")
                
        nombres_materias.append(materia)
        calificaciones_materias.append(calificacion)
        
        continuar = input("¿Desea ingresar otra materia? (s/n): ").lower()
        if continuar != 's':
            break
            
    return nombres_materias, calificaciones_materias

def calcular_promedio(calificaciones):
    
    if not calificaciones:
        return 0
    return sum(calificaciones) / len(calificaciones)

def determinar_estado(calificaciones, umbral=5.0):
    
    aprobados_indices = []
    reprobados_indices = []

    if not calificaciones:
        return aprobados_indices, reprobados_indices

    for indice, calificacion in enumerate(calificaciones):
        if calificacion >= umbral:
            aprobados_indices.append(indice)
        else:
            reprobados_indices.append(indice)
            
    return aprobados_indices, reprobados_indices

def encontrar_extremos(calificaciones):
    
    if not calificaciones:
        return None, None
    
    calificacion_maxima = max(calificaciones)
    calificacion_minima = min(calificaciones)

    indice_maximo = calificaciones.index(calificacion_maxima)
    indice_minimo = calificaciones.index(calificacion_minima)

    return indice_maximo, indice_minimo

def main():
    
    nombres_materias, calificaciones_materias = ingresar_calificaciones()

    if not nombres_materias:
        print("\nNo se ingresaron calificaciones.")
        return

    promedio = calcular_promedio(calificaciones_materias)
    aprobados_indices, reprobados_indices = determinar_estado(calificaciones_materias)
    indice_max, indice_min = encontrar_extremos(calificaciones_materias)

    print("\n--- Resumen de Calificaciones ---")
    
    for i, nombre in enumerate(nombres_materias):
        print(f"- {nombre}: {calificaciones_materias[i]}")

    print(f"\nPromedio general: {promedio:.2f}")

    print("\nMaterias aprobadas:")
    if not aprobados_indices:
        print("- Ninguna.")
    else:
        for i in aprobados_indices:
            print(f"- {nombres_materias[i]} ({calificaciones_materias[i]})")

    print("\nMaterias suspensas:")
    if not reprobados_indices:
        print("- Ninguna.")
    else:
        for i in reprobados_indices:
            print(f"- {nombres_materias[i]} ({calificaciones_materias[i]})")

    if indice_max is not None:
        print(f"\nMejor calificación: {nombres_materias[indice_max]} con un {calificaciones_materias[indice_max]}")
    if indice_min is not None:
        print(f"Peor calificación: {nombres_materias[indice_min]} con un {calificaciones_materias[indice_min]}")
        
# --- Punto de Entrada del Programa ---
if __name__ == "__main__":
    main()
