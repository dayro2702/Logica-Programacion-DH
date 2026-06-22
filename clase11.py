def sumar(num1, num2):
    resultado = num1 + num2
    print("Resultado:", resultado)
    return resultado

numero1 = int(input("Ingrese el primer valor: "))
numero2 = int(input("Ingrese el segundo valor: "))

valor = sumar(5, 7)
print(valor)

#======================================================================================
impuesto_iva = 0.19 #19%

pago_total = int(input("Ingrese el valor total de las compras: "))

def calcular_impuestos(valor):
    precio_sin_impuesto = 0
    valor_impuesto = valor * impuesto_iva / 1
    precio_sin_impuesto = valor - valor_impuesto
    return valor_impuesto, precio_sin_impuesto

print("Pago total ", pago_total)
print("Impuesto IVA: 19%")
resultado, valor_sin_impuesto = calcular_impuestos(pago_total)
print("El valor pagado de IVA es de: ", resultado)
print("El valor sin IVA es: ", valor_sin_impuesto)
