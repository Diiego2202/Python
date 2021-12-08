n = int(input(""))
print(n)

resto = int(n/100)
print(f'{resto} nota(s) de R$ 100,00')
n = n - (resto*100)

resto = int(n/50)
print(f'{resto} nota(s) de R$ 50,00')
n = n - (resto*50)

resto = int(n/20)
print(f'{resto} nota(s) de R$ 20,00')
n = n - (resto*20)

resto = int(n/10)
print(f'{resto} nota(s) de R$ 10,00')
n = n - (resto*10)

resto = int(n/5)
print(f'{resto} nota(s) de R$ 5,00')
n = n - (resto*5)

resto = int(n/2)
print(f'{resto} nota(s) de R$ 2,00')
n = n - (resto*2)

resto = int(n/1)
print(f'{resto} nota(s) de R$ 1,00')
n = n - (resto*1)
