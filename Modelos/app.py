from modelos.cachorro import Cachorro

def main():  
    cachorro1 = Cachorro("Bidu", "Schnauzer")
    cachorro2 = Cachorro("Rex", "Pastor-alemão")
    pitbull_marrom = Cachorro('Pantera', 'Pitbull - Red Nose')

    print(cachorro1.nome)
    print(cachorro2.nome)

if __name__ == '__main__':
    main()