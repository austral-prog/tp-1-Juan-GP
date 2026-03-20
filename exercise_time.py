def time():
    """
    Ejercicio 4 - Calculadora de Tiempo

    Dado un total de segundos, calcular e imprimir:
    1. Horas completas
    2. Minutos completos restantes
    3. Segundos restantes
    """
    total_segundos = 3665

    t=total_segundos
    Hora=(t/60)//60
    Hora=int(Hora)
    print(Hora)
    Minutos=(t/60)%60
    Minutos=int(Minutos)
    print(Minutos)
    to=((t%60)%60)%60
    to=int(to)
    print(to)

   
time()