import re
with open ("regex_sum_991800.txt", "r") as file:
    texto = file.read()
    soma=0
    for item in re.findall("[0-9]+", texto):
        soma+=int(item)
print (soma)
