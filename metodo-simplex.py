class Simplex:

    def __init__(self):
        self.tabela = []

    def set_funcao_objetivo(self, fo):  # função que adiciona a função objetivo
        self.tabela.append(fo)

    def add_restricoes(self, lr):  # função que adiciona as restrições
        self.tabela.append(lr)

    def get_coluna_entrada(self):  # Define a coluna de entrada, pegando o menor valor da linha 0(Z)
        coluna_pivo = min(self.tabela[0])
        index = self.tabela[0].index(coluna_pivo)

        return index

    def get_linha_saida(self, coluna_entrada):  # Define a coluna de entrada, pegando o menor valor pela regra do quociente
        resultados = {}
        for linha in range(len(self.tabela)):
            if linha > 0:  # exclui linha Z do cálculo
                if self.tabela[linha][coluna_entrada] > 0:  # Eliminado resultados negativos ou 0
                    divisao = self.tabela[linha][-1] / self.tabela[linha][coluna_entrada]
                    resultados[linha] = divisao
        index = min(resultados, key=resultados.get)   # Vai achar o valor mínimo e retornar sua chave

        return index

    def calcular_nova_linha_pivo(self, coluna_entrada, linha_saida):
        linha = self.tabela[linha_saida]

        pivo = linha[coluna_entrada]

        nova_linha_pivo = [valor / pivo for valor in linha]

        return  nova_linha_pivo

    def calcular_nova_linha(self, linha, coluna_entrada, linha_pivo):  # Calcula o valor da nova linha utilizando o pivo
        pivo = linha[coluna_entrada] * -1  # Invertendo sinal do pivo
        linha_resultado = []

        for valor in linha_pivo:
            linha_resultado.append(valor*pivo)

        nova_linha = []
        for i in range(len(linha_resultado)):
            soma_valores = linha_resultado[i] + linha[i]
            nova_linha.append(soma_valores)

        return nova_linha

    def mostra_tabela(self):
        for i in range(len(self.tabela)):
            for j in range(len(self.tabela[0])):
                print(f"{self.tabela[i][j]}    ", end="")
            print()

    def eh_negativo(self):  # Verifica se a linha Z tem valores negativos
        negativo = list(filter(lambda x: x < 0, self.tabela[0]))

        if len(negativo) > 0:
            return True
        else:
            return False

    def calcular(self):
        coluna_entrada = self.get_coluna_entrada()

        primeira_linha_saida = self.get_linha_saida(coluna_entrada)

        linha_pivo = self.calcular_nova_linha_pivo(coluna_entrada, primeira_linha_saida)

        self.tabela[primeira_linha_saida] = linha_pivo  # linha pivô entra no lugar da linha que saiu

        tabela_copia = self.tabela.copy()  # Tabela cópia para não afetar a original, base de cálculo para troca de linha

        index = 0

        while index < len(self.tabela):  # Laço de repetição para novos cálculos de linha
            if index != primeira_linha_saida:  # Exclusão da linha pivô que ja foi calculada
                linha = tabela_copia[index]
                nova_linha = self.calcular_nova_linha(linha, coluna_entrada, linha_pivo)
                self.tabela[index] = nova_linha
            index += 1

    def resolve(self):
        self.calcular()

        while self.eh_negativo():
            self.calcular()

        self.mostra_tabela()


if __name__ == "__main__":
    """
    Exemplo do video:
    
    Função objetivo:
        5x+ 2y
    Restrições:
        2x + y <= 6
        10x + 12y <= 60
        x, y >= 0
    
    Normalizando as funções
    Z - 5x - 2y = 0
    2x + y + f1 = 6
    10x + 12y + f2 = 60
    
    Resultado
    1.0    0.0    0.5    2.5    0.0    15.0    
    0.0    1.0    0.5    0.5    0.0    3.0    
    0.0    0.0    7.0    -5.0    1.0    30.0
    
    variáveis básicas:
        Colunas onde possuem apenas valores 0 e 1
        nesse caso temos z, x e f2 como básicas
    variáveis não báscias:
        Valores diferentes de 0 e 1
        temos: y e f1
        valores não básicos irão valer 0
    Então:
        Z = 5x + y
        onde: z = 15 e y = 0
        15 = 5x + 0
        x = 3
    
    simplex = Simplex()

    simplex.set_funcao_objetivo([1,-5,-2,0,0,0])

    simplex.add_restricoes([0,2,1,1,0,6])
    simplex.add_restricoes([0,10,12,0,1,60])

    simplex.resolve()"""

    """
    Exemplo do pdf
    
    Função Objetivo:
        z = 3x1 + 2x2
    Restrições:
        2x1 + x2 <= 100
        x1 + x2 <= 80
        x1 <= 40
        x1,x2 >= 0
    
    Normalizando:
        z - 3x1 -2x2 = 0
        2x1 + x2 + s1 = 100
        x1 + x2 + s2 = 80
        x1 + s3 = 40
    """
    simplex = Simplex()

    simplex.set_funcao_objetivo([1,-3,-2,0,0,0,0])

    simplex.add_restricoes([0,2,1,1,0,0,100])
    simplex.add_restricoes([0,1,1,0,1,0,80])
    simplex.add_restricoes([0,1,0,0,0,1,40])

    simplex.resolve()