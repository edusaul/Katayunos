import unittest
from Bowling import Bolera

class MyTestCase(unittest.TestCase):
    def test_contar_partida_sin_tirar_ningun_bolo(self):

        tiradas = "-- -- -- -- -- -- -- -- -- --"

        bolera = Bolera()
        puntuacion = bolera.calcular_puntuacion(tiradas)

        self.assertEqual(0, puntuacion)

    def test_contar_partida_tirando_un_bolo(self):

        tiradas = "1- -- -- -- -- -- -- -- -- --"

        bolera = Bolera()
        puntuacion = bolera.calcular_puntuacion(tiradas)

        self.assertEqual(1, puntuacion)

    def test_contar_partida_tirando_10_bolos_repartidos_en_varios_lanzamientos(self):

        tiradas = "1- -- -4 -- -- 3- -- 2- -- --"

        bolera = Bolera()
        puntuacion = bolera.calcular_puntuacion(tiradas)

        self.assertEqual(10, puntuacion)

    def test_contar_partida_haciendo_un_semipleno_sin_bonus(self):

        tiradas = "5/ -- -- -- -- -- -- -- -- --"

        bolera = Bolera()
        puntuacion = bolera.calcular_puntuacion(tiradas)

        self.assertEqual(10, puntuacion)


if __name__ == '__main__':
    unittest.main()
