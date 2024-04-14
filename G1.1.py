
import math

class DadosPessoais:
    def __init__(self, arquivo):
        self.arquivo = arquivo
        self.ids = []
        self.sexos = []
        self.pesos = []
        self.idades = []

    def carregar_dados(self):
        with open(self.arquivo, 'r') as file:

            next(file)
            for linha in file:
                dados = linha.strip().split(',')
                self.ids.append(int(dados[0]))
                self.sexos.append(dados[1])
                self.pesos.append(float(dados[2]))
                self.idades.append(int(dados[3]))

    def retornar_dados(self):
        return {
            'IDs': self.ids,
            'Sexos': self.sexos,
            'Pesos': self.pesos,
            'Idades': self.idades
        }
    

class Calcular_oncas:
    def __init__(self, sexo, peso, idade) -> None:
        self.sexo = sexo
        self.peso = peso
        self.idade = idade
        self.dic_media_peso = {}
        self.dic_media_idade = {}
        self.Media_Idade_Masculino = 0
        self.Media_Peso_Masculino = 0
        self.Media_Idade_Feminino = 0
        self.Media_Peso_Feminino = 0

    def cal_media(self):
        for sexo, peso, idade in zip(self.sexo, self.peso, self.idade):
            if sexo not in self.dic_media_peso:
                self.dic_media_peso[sexo] = [peso]  
                self.dic_media_idade[sexo] = [idade]  
            else:
                self.dic_media_peso[sexo].append(peso)  
                self.dic_media_idade[sexo].append(idade) 

        total_Idade_Masculino = 0
        total_Idade_Feminino = 0
        total_Peso_Masculino = 0
        total_Peso_Feminino = 0

        Lista_Idade_Masculino = self.dic_media_idade['M']
        Lista_Idade_Feminino = self.dic_media_idade['F']
        Lista_Peso_Masculino = self.dic_media_peso['M']
        Lista_Peso_Feminino = self.dic_media_peso['F']

        for MI,MP,FI,FP in zip(Lista_Idade_Masculino,Lista_Peso_Masculino,Lista_Idade_Feminino,Lista_Peso_Feminino):
            total_Idade_Masculino += MI
            total_Peso_Masculino += MP
            total_Idade_Feminino += FI
            total_Peso_Feminino += FP
        
        Media_Idade_Masculino = total_Idade_Masculino/len(Lista_Idade_Masculino)
        Media_Peso_Masculino = total_Peso_Masculino/len(Lista_Peso_Masculino)
        Media_Idade_Feminino = total_Idade_Feminino/len(Lista_Idade_Feminino)
        Media_Peso_Feminino = total_Peso_Feminino/len(Lista_Peso_Feminino)
        

        return Media_Idade_Masculino,Media_Peso_Masculino,Media_Idade_Feminino,Media_Peso_Feminino

    def calcular_desvio_padrao(self):
        Lista_Idade_Masculino = self.dic_media_idade['M']
        Lista_Idade_Feminino = self.dic_media_idade['F']
        Lista_Peso_Masculino = self.dic_media_peso['M']
        Lista_Peso_Feminino = self.dic_media_peso['F']

        soma_diferencas_quadradas_Idade_Masculino = 0
        soma_diferencas_quadradas_Peso_Masculino = 0
        soma_diferencas_quadradas_Idade_Feminino = 0
        soma_diferencas_quadradas_Peso_Feminino = 0

        for VIM, VPM, VIF, VPF in zip(Lista_Idade_Masculino,Lista_Peso_Masculino,Lista_Idade_Feminino,Lista_Peso_Feminino):

            soma_diferencas_quadradas_Idade_Masculino += (VIM - self.Media_Idade_Masculino) ** 2
            soma_diferencas_quadradas_Peso_Masculino += (VPM - self.Media_Peso_Masculino) ** 2
            soma_diferencas_quadradas_Idade_Feminino += (VIF - self.Media_Idade_Feminino) ** 2
            soma_diferencas_quadradas_Peso_Feminino += (VPF - self.Media_Peso_Feminino) ** 2

        variancia_Idade_Masculino = soma_diferencas_quadradas_Idade_Masculino/len(Lista_Idade_Masculino)
        variancia_Peso_Masculino = soma_diferencas_quadradas_Peso_Masculino/len(Lista_Peso_Masculino)
        variancia_Idade_Feminino = soma_diferencas_quadradas_Idade_Feminino/len(Lista_Idade_Feminino)
        variancia_Peso_Feminino = soma_diferencas_quadradas_Peso_Feminino/len(Lista_Peso_Feminino)


        desvio_padrao_Idade_Masculino = math.sqrt(variancia_Idade_Masculino)
        desvio_padrao_Peso_Masculino = math.sqrt(variancia_Peso_Masculino)
        desvio_padrao_Idade_Feminino = math.sqrt(variancia_Idade_Feminino)
        desvio_padrao_Peso_Feminino = math.sqrt(variancia_Peso_Feminino)


        
        return desvio_padrao_Idade_Masculino,desvio_padrao_Peso_Masculino,desvio_padrao_Idade_Feminino,desvio_padrao_Peso_Feminino

    def Porcentagem(self):
        countM = 0
        countF = 0
        for n in self.sexo:
            if n == 'M':
                countM += 1
            else:
                countF += 1

        porcentagemM = (countM / len(self.sexo)) * 100
        porcentagemF = (countF / len(self.sexo)) * 100

        return porcentagemM,porcentagemF
    
    def Mais_Menos(self):
        Mais_Velha_Masculina = 0
        Mais_Velha_Feminina = 0
        Mais_Pesada_Masculina = 0
        Mais_Pesada_Feminina = 0

        Menos_Velha_Masculina = 10
        Menos_Velha_Feminina = 10
        Menos_Pesada_Masculina = 100
        Menos_Pesada_Feminina = 100

        Lista_Idade_Masculino = self.dic_media_idade['M']
        Lista_Idade_Feminino = self.dic_media_idade['F']
        Lista_Peso_Masculino = self.dic_media_peso['M']
        Lista_Peso_Feminino = self.dic_media_peso['F']

        for IM, IF, PM, PF in zip(Lista_Idade_Masculino,Lista_Idade_Feminino,Lista_Peso_Masculino,Lista_Peso_Feminino):
            if IM < Menos_Velha_Masculina:
                Menos_Velha_Masculina = IM

            elif IM > Mais_Velha_Masculina:
                Mais_Velha_Masculina = IM

            if IF < Menos_Velha_Feminina:
                Menos_Velha_Feminina = IF

            elif IF > Mais_Velha_Feminina:
                Mais_Velha_Feminina = IF

            if PM < Menos_Pesada_Masculina:
                Menos_Pesada_Masculina = PM

            elif PM > Mais_Pesada_Masculina:
               Mais_Pesada_Masculina = PM

            if PF < Menos_Pesada_Feminina:
                Menos_Pesada_Feminina = PF

            elif PF > Mais_Pesada_Feminina:
               Mais_Pesada_Feminina = PF

        return Mais_Velha_Masculina, Menos_Velha_Masculina, Mais_Velha_Feminina, Menos_Velha_Feminina,Mais_Pesada_Masculina, Menos_Pesada_Masculina,Mais_Pesada_Feminina,Menos_Pesada_Feminina  

def Start():
    if __name__ == "__main__":
        arquivo = "oncas_pintadas.txt"
        dados = DadosPessoais(arquivo)
        dados.carregar_dados()
        dados_separados = dados.retornar_dados()
        calcular = Calcular_oncas(dados.sexos,dados.pesos,dados.idades)

        while True:
            print('1 - Mostrar lista de Onças')
            print('2 - Mostrar Calculos das Onças')
            print('3 - Sair')
            opc = input(':')

            if opc == '1':
                print(f'Lista Ids:{dados.ids}\nListas Sexos:{dados.sexos}\nLista Idades:{dados.idades}\nLista Pesos:{dados.pesos}')

            elif opc == '2':
                print(f"Medias\n{calcular.cal_media()}")
                print(f"Desvios Padrôes\n{calcular.calcular_desvio_padrao()}")
                print(f"Porcentagens\n{calcular.Porcentagem()}")
                print(f"Mais e menos\n{calcular.Mais_Menos()}")

            elif opc == '3':
                break

Start()


