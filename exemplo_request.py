import requests


url="https://jsonplaceholder.typicode.com/users"
passar=200

chamada = requests.get(url)

if chamada.status_code == passar:
    print("passou")
else:
    print("não passou")


if chamada.status_code == passar:
    dados = chamada.json()

    print(f"Nome: {dados[0]['name']}")
    print(f"Email: {dados[0]['email']}")
else:
    print(f"Erro: {chamada.status_code}")

nome="cr"
achado=False
for i in dados:
    if nome.lower() in i['name'].lower():
        print(i)
        achado=True
if achado == False:
    print("não encontrado")