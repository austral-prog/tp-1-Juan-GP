def grades():
    """
    Ejercicio 11 - Promedio de Calificaciones

    Dadas tres notas, calcular e imprimir:
    1. El promedio de las tres notas
    2. La nota máxima
    3. La nota mínima
    4. Cuántos puntos faltan del promedio a 10
    """
    nota1 = 8
    nota2 = 7
    nota3 = 9

    nota=(nota1+nota2+nota3)/3
    print(nota)
    
    Max=max(nota1,nota2,nota3)
    print(Max)
    
    Min=min(nota1,nota2,nota3)
    print(Min)
    
    falta=10-nota
    print(falta)

grades()
