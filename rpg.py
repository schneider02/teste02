import random

class Personagem:
    def __init__(self, nome, vida, ataque):
        self.nome = nome
        self.vida = vida
        self.ataque = ataque

    def atacar(self, inimigo):
        dano = random.randint(1, self.ataque)
        inimigo.vida -= dano
        print(f"{self.nome} atacou {inimigo.nome} e causou {dano} de dano!")

    def esta_vivo(self):
        return self.vida > 0

def main():
    print("Bem-vindo ao RPG!")
    
    nome = input("Digite o nome do seu personagem: ")
    jogador = Personagem(nome, vida=20, ataque=5)
    
    inimigos = [
        Personagem("Goblin", vida=10, ataque=3),
        Personagem("Orc", vida=15, ataque=4),
        Personagem("Dragão", vida=25, ataque=6)
    ]

    for inimigo in inimigos:
        print(f"\nUm {inimigo.nome} apareceu!")
        
        while jogador.esta_vivo() and inimigo.esta_vivo():
            jogador.atacar(inimigo)
            if inimigo.esta_vivo():
                inimigo.atacar(jogador)
                print(f"{jogador.nome} tem {jogador.vida} de vida restante.")
            else:
                print(f"{inimigo.nome} foi derrotado!")

        if not jogador.esta_vivo():
            print("Você foi derrotado! Fim de jogo.")
            break

    if jogador.esta_vivo():
        print("Parabéns! Você derrotou todos os inimigos!")

if __name__ == "__main__":
    main()
