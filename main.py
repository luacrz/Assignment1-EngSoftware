import pyqrcode
import png
import os
##
aula = "Matemática I"
qr = pyqrcode.create(aula)
qr.png("aula.png", scale=6)

input("Por favor, leia o QR Code para registrar sua presença: ")

aluno = "João"
arquivo = aula + ".txt"
if not os.path.exists(arquivo):
    with open(arquivo, "w") as f:
        f.write("Alunos presentes na aula de " + aula + ":\n")
with open(arquivo, "a") as f:
    f.write(aluno + "\n")
    print("Presença registrada.")