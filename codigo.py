import time

print('='*40)
print('\033[36mBem vindo ao nosso sistema de banco.')
print('='*40)

print('\033[31mAguarde o sistema iniciar...')
time.sleep(5)

vcasa = float(input('Qual é o valor da casa? '))
vsalario = float(input('Qual é o seu salário? '))
vtempo = int(input('Enquanto tempo vai pagar? '))

print('\033[31mAguarde...')
time.sleep(3)

prestação = vcasa / (vtempo * 12)
minimo = vsalario * 30 / 100
print('\033[31mrecolhendo informações; Aguarde')
print('='*40)
print('Casa: {:.0f} reais' .format(vcasa))
print('Salário: {:.0f} reais'.format(vsalario))
print('Anos: {} anos' .format(vtempo))
print('='*40)
verif = str(input('\033[31mEssas informações estão corretas? ')).strip().upper()
if verif in 'SIM':
    print('\033[31mAguarde um instante...')
    time.sleep(3)
else:
    print('\033[35mReveja suas informações.')
    exit()
while True:
    print('Veja abaixo: ')
    if prestação <= minimo:
        print('Empréstimo pode ser CONCEDIDO!')
        exit()
    else:
        print('Lamento, mas seu empréstimo foi negado.')
        break
