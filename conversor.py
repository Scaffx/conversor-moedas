import requests

def converter_moeda(valor, de, para):
    url = f"https://api.exchangerate.host/convert?from={de}&to={para}&amount={valor}"
    resposta = requests.get(url)

    if resposta.status_code != 200:
        return "Erro ao acessar a API."

    dados = resposta.json()
    resultado = dados.get("result", None)

    if resultado is not None:
        return f"{valor} {de} = {resultado:.2f} {para}"
    else:
        return "Erro ao converter moedas."

if __name__ == "__main__":
    try:
        valor = float(input("Digite o valor a ser convertido: "))
        moeda_origem = input("Moeda de origem (ex: USD): ").strip().upper()
        moeda_destino = input("Moeda de destino (ex: BRL): ").strip().upper()

        resultado = converter_moeda(valor, moeda_origem, moeda_destino)
        print(resultado)
    except ValueError:
        print("Por favor, insira um número válido.")