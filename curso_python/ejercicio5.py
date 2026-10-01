"""1. Registrar los ingresos mensuales de un cliente durante 6 meses usando un bucle
while para solicitar el ingreso de cada mes. Validar que los ingresos sean números
positivos. Si se ingresa un valor negativo, mostrá un mensaje indicando que el
valor no es válido y volvé a pedir el dato.
2. Calcular el total acumulado durante los 6 meses y el promedio mensual. Mostrá
este resultado al final del programa."""

counter = 1
ingreso_acumulado = 0
while counter<7:
    ingreso = input(f"Ingrese el monto del mes ¨{counter}: ")
    if not ingreso.isdigit() or int(ingreso) < 0:
        print("Valor no válido. Por favor vuelva a intentarlo")
        continue
    ingreso_acumulado += int(ingreso)
    counter += 1

ingreso_promedio = ingreso_acumulado / counter
print("\n--- Datos Procesados ---")
print(f"Ingresos acumulados: {ingreso_acumulado}")
print(f"Ingreso promedio: {ingreso_promedio:.2f}")
counter += 1
