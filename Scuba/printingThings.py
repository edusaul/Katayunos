from Scuba.Scuba_class import *

diver = ScubaDiver()
daughter = ScubaDaughter()

print("Diver oxigen is " + str(diver.get_oxigen()))
print("Daughter oxigen is " + str(daughter.get_oxigen()))
print("Daughter nueva cosa is " + str(daughter.get_cosa_nueva()))

# la siguiente línea no funciona porque no existe ese método en la clase madre
# print("Diver nueva cosa is " + str(Diver.get_cosa_nueva()))

