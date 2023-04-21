#primeiro passo gerar uma key em fernet

import os

from cryptography.fernet import Fernet

#gerar a chave

key = #sua chave de criptografia
c = Fernet.generate_key()
print(c)


#apos gerar a chave a reserve pois apos sua perda nao tem como recuperar os dispositivos

#a chave sera gerada no console