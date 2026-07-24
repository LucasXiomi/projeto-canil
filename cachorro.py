from modelos.avaliacao import Avaliacao

class Cachorro:
    cachorros = []

    def __init__(self, nome, raca):
        self._nome = nome.title()
        self._raca = raca.upper()
        self._disponibilidade = True
        self._avaliacoes = []
        Cachorro.cachorros.append(self)

    def __str__(self):
        return f'{self._nome} | {self._raca}'

    # Properties
    @property
    def nome(self):
        return self._nome

    @property
    def raca(self):
        return self._raca

    @property
    def disponibilidade(self):
        return 'Disponível' if self._disponibilidade else 'Indisponível'

    # Método de instância
    def alternar_estado(self):
        self._disponibilidade = not self._disponibilidade

    # Método de classe
    @classmethod
    def listar_cachorros(cls):
        print(f"{'Nome'.ljust(25)} | {'Raça'.ljust(25)} | {'Avaliaçao'.ljust(25)} | {'Disponibilidade'}")
        print('-' * 100)
        for cachorro in cls.cachorros:
            print(
                f"{cachorro._nome.ljust(25)} | "
                f"{cachorro._raca.ljust(25)} | "
                f"{str(cachorro.media_avaliacoes).ljust(25)} | "
                f"{cachorro.disponibilidade}"
            )

    def receber_avaliacao(self, cuidador, nota):
        avaliacao = Avaliacao(cuidador, nota)
        self._avaliacoes.append(avaliacao)

    @property
    def media_avaliacoes(self):
        if not self._avaliacoes:
            return 0

        soma_das_avaliacoes = sum(avaliacao._nota for avaliacao in self._avaliacoes)
        quantidade = len(self._avaliacoes)
        media = soma_das_avaliacoes / quantidade
        
        return round(media,1)


