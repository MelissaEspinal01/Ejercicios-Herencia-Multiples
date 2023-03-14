from Jugador1 import Jugador1
from Jugador2 import Jugador2
class Juego:
    def __init__(self, nombre_luchador1, nombre_luchador2):
        self.Jugador1 = Jugador1(nombre_luchador1)
        self.Jugador2 = Jugador2(nombre_luchador2)
        
    def comenzar_juego(self):
        while self.Jugador1.vida > 0 and self.Jugador2.vida > 0:
            golpea_primero = input("¿Quién golpea primero? Jugador1 o Jugador2? ")
            if golpea_primero == "Jugador1":
                if self.Jugador1.golpear(self.Jugador2):
                    break
                if self.Jugador2.golpear(self.Jugador1):
                    break
            elif golpea_primero == "Jugador2":
                if self.Jugador2.golpear(self.Jugador1):
                    break
                if self.Jugador1.golpear(self.Jugador2):
                    break
            else:
                print("Opción no válida. Inténtalo de nuevo.")
        else:
            print("¡El juego ha terminado en empate!")
