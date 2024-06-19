# verificação de ano bissexto

ano = int(input('digite um ano: '))
if ano % 4 == 0:
    print ('o ano é BISSEXTO')
else:
    print('o ano não é BISSEXTO')