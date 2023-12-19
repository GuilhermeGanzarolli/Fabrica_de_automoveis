class Veiculo:

    def __init__(self, marca, ligado=False, velocidade = 0, n_de_rodas = None):
        self.marca = marca
        self.ligado = ligado
        self.velocidade = velocidade
        self.n_de_rodas = n_de_rodas

    def __str__(self):
        return f"{self.__class__.__name__} -> {' | '.join([f'{chave} = {valor}' for chave, valor in self.__dict__.items()])}"


    def ligar(self):
        self.ligado = True
        print("=== Veículo ligado ===")

    
    def desligar(self):
        if(self.velocidade == 0):
            self.ligado = False
            print("### Veículo desligado ###")
        else:
            print("Veículo em movimento! Pare para desligar!")

    
    def acelerar(self):
        self.velocidade += 10
        print(f"--> {self.velocidade} KM/H")


    def freiar(self):
        if self.velocidade > 0:
            self.velocidade -= 10
            print(f"--> {self.velocidade} KM/H")
        else:
            print("### O veículo já está parado ###")


class Carro(Veiculo):
    def __init__(self, cor, marca, ligado=False, velocidade=0, n_de_rodas = 4):
        super().__init__(marca, ligado, velocidade, n_de_rodas)
        self.cor = cor
    
    


class Motocicleta(Veiculo):  
    def __init__(self, cor, marca, ligado=False, velocidade=0, n_de_rodas = 2):
        super().__init__(marca, ligado, velocidade, n_de_rodas)
        self.cor = cor



moto1 = Motocicleta("Preta", "Honda")

print(moto1)

moto1.ligar()

moto1.acelerar()
moto1.acelerar()
moto1.desligar()
moto1.freiar()
moto1.desligar()
moto1.freiar()
moto1.desligar()


