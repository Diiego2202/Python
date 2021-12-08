n = float(input(""))

print("NOTAS:")

resto = int(n/100)
print(f'{resto} nota(s) de R$ 100.00')
n = n - (resto*100)

resto = int(n/50)
print(f'{resto} nota(s) de R$ 50.00')
n = n - (resto*50)

resto = int(n/20)
print(f'{resto} nota(s) de R$ 20.00')
n = n - (resto*20)

resto = int(n/10)
print(f'{resto} nota(s) de R$ 10.00')
n = n - (resto*10)

resto = int(n/5)
print(f'{resto} nota(s) de R$ 5.00')
n = n - (resto*5)

resto = int(n/2)
print(f'{resto} nota(s) de R$ 2.00')
n = n - (resto*2)

print("MOEDAS:")
resto = int(n/1)
print(f'{resto} moeda(s) de R$ 1.00')
n = n - (resto*1)

resto = int(n/0.5)
print(f'{resto} moeda(s) de R$ 0.50')
n = n - (resto*0.5)

resto = int(n/0.25)
print(f'{resto} moeda(s) de R$ 0.25')
n = n - (resto*0.25)

resto = int(n/0.10)
print(f'{resto} moeda(s) de R$ 0.10')
n = n - (resto*0.10)

resto = int(n/0.05)
print(f'{resto} moeda(s) de R$ 0.05')
n = n - (resto*0.05)

resto = int(n/0.01)
print(f'{resto} moeda(s) de R$ 0.01')
n = n - (resto*0.01)