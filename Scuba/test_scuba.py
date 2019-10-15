import unittest
from Scuba.Scuba_class import ScubaDiver

# Tenemos la clase Scuba_Diver, pero tenemos que hacer una instancia de ella (crear un objeto de este tipo)
# sub1 = ScubaDiver()

# Esto es una clase que deriva de una ya existente para testing
class MyTestCase(unittest.TestCase):
    def test_should_be_alive_at_beginning(self):
        diver = ScubaDiver()

        is_alive = diver.is_alive

        self.assertEqual(is_alive,True)

    def test_initial_O2(self):
        diver = ScubaDiver()

        initial_oxigen = diver.oxigen

        self.assertEqual(sub1.oxigen,150,"Initial Oxigen should be 150")

    def test_initial_depth(self):
        diver = ScubaDiver()

        is_alive = diver.alive

        self.assertEqual(sub1.depth,0,"Initial depth should be 0")


if __name__ == '__main__':
    unittest.main()
