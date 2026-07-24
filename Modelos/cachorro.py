from modelo.avaliacao import avaliacao

class Cachorro:
    cachorros = []
def __init__(self, nome, raca):
    self._nome = nome.title()
    self._raca = raca.upper()
    self._disponibilidade = True
    
Cachorro.cachorros.append(self)
def __str__(self):
    return f'{self._nome} | {self._raca}'
# ... (outros métodos e propriedades)

@classmethod
def listar_cachorro(cls):
    print(f" {'Nome'.1just(25)} | {'Raça'.1just(25)} |{'Disponibilidade'}")
    print('-'* 70)
    for cachorro in cls.cachorro
    
    c1 = Cachorro("Rex", "Labrador")
c2 = Cachorro("Mel", "Poodle")
c3 = Cachorro("Thor", "Pastor Alemão")

Cachorro.listar_cachorros()

  
c1 = Cachorro("Rex", "Labrador")
c2 = Cachorro("Mel", "Poodle")
c3 = Cachorro("Thor", "Pastor Alemão")

Cachorro.listar_cachorros()

