def age():
    """
    Ejercicio 10 - Conversión de Edad a Tiempo

    Dada una edad en años, calcular e imprimir:
    1. La edad en meses (1 año = 12 meses)
    2. La edad en días (1 año = 365 días)
    3. La edad en horas (1 día = 24 horas)
    4. La edad en minutos (1 hora = 60 minutos)
    """
    edad_anos = 25

    edadm=edad_anos*12
    print(edadm)

    edadd=edad_anos*365
    print(edadd)

    edadh=edadd*24
    print(edadh)

    edadm=edadh*60
    print(edadm)

age()