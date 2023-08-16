from random import randrange

nome = input("Qual seu nome? ")

token = randrange(1000,9998,step=2)

comprimento = f"Olá {nome}, o seu token de acesso é {token}"

print(comprimento)