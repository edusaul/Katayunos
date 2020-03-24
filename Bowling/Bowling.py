class Bolera:

    def calcular_puntuacion(self, tiradas):
        lista_de_tiradas = tiradas.split()
        puntuacion_total = 0

        for tirada in lista_de_tiradas:
            puntuacion_tirada = 0
            for lanzamiento in tirada:
                if lanzamiento.isdigit():
                    puntuacion_tirada += int(lanzamiento)
                else:
                    if lanzamiento == "/":
                        puntuacion_tirada = 10
            puntuacion_total += puntuacion_tirada


        return puntuacion_total