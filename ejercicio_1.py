# Claire Dearing: Ok, encárgate urgente de conseguir a la persona que necesitas, no me importa de
# dónde lo saques. Necesito que proceses urgente este archivo con información del parque y esté
# disponible en mi monitor de informes. Y no olvide determinar cual de nuestro dinosaurios fuel el
# ultimo en ser descubierto y quien lo hizo. [actividad para resolver]

from jurassic_park import dinosaurs
from clases import Dinosaur
from lista import Lista

lista = Lista()

for dinosaur in dinosaurs:
    lista.insertar(
        Dinosaur(
            dinosaur['name'],
            dinosaur['type'],
            dinosaur['number'],
            dinosaur['period'],
            dinosaur['named_by'],
        ),
        'name'
    )

print('Monitor de dinosaurios: ')
ultimo_descubierto = lista.ultimo_descubierto().info;
descubridor = ultimo_descubierto.named_by.split(',')[0]
anio =  ultimo_descubierto.named_by.split(',')[-1]
print('El ultimo dinosaurio descubierto es el', ultimo_descubierto.name, 'en', anio)
print('Y fue descubierto por', descubridor)
