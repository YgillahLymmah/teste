listDistancia = list()
asteroide = {
    "asteroide0": 0,
    "asteroide1": 0,
    "asteroide2": 0,
    "asteroide3": 0,
    "asteroide4": 0
}
soma = []

for i in range(0, 5):
    item = int(input("Coloca a distancia do negocio:\n "))

    listDistancia.append(item)
    asteroide["asteroide" + str(i)] = item
    soma.append(item)

media = (sum(soma) / len(soma))
asteroide["asteroide0"] = listDistancia[0]

print(asteroide, "\n", media)