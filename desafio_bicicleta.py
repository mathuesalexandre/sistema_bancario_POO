class Bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
    def buzinar(self):
        print('Plim plim')

    def parar(self):
        print('Parando Bicicleta')
        print('Bicicleta parada')

    def correr(self):
        print('Vrummmmm ...')

b1 = Bicicleta('vermelha', 'caloi', 2022, 600)
b1.buzinar()
b1.correr()
b1.parar()