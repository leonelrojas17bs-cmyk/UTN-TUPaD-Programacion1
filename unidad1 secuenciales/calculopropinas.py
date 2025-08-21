#Calculadora de propinas de restaurante
monto = float(input("ingrese el monto total:"))
propinasugerida10 = monto * 0.10
propinasugerida15 = monto * 0.15
print(f"propina al 10%: {propinasugerida10}")
print(f"propina al 15%: {propinasugerida15}")
print(f"total con propina al 10%: {monto+propinasugerida10}")
print(f"total con propina al 15%: {monto+propinasugerida15}")