import json 


json_string = "{}"
dic = {"chave" : 'valor', "numero" : 10}
print(dic["numero"])
with open(file = "o.json", mode = 'w' ) as file:
    file.write(json_string)