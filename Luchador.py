class Luchador:
    def __init__(self, nombre, poder):
        self.nombre = nombre
        self.poder = poder
        self.vida = 100
        
    def golpear(self, oponente):
        oponente.vida -= int(oponente.vida * 0.3)
        print("{} ha golpeado a {}!").format(self.nombre,oponente.nombre)
        print("{} tiene {} puntos de vida restantes.").format(oponente.nombre,oponente.vida)
        
        if oponente.vida <= 0:
            print("¡{} ha ganado!").format(self.nombre)
            return True
        else:
            return False
