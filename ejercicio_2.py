import sys
from clases import Dinosaur, Alert
from lista import Lista
from cola import Cola
from jurassic_park import dinosaurs

# Claire Dearing: Ok, encárgate urgente de conseguir a la persona que necesitas, no me importa de
# dónde lo saques. Necesito que proceses urgente este archivo con información del parque y esté
# disponible en mi monitor de informes. Y no olvide determinar cual de nuestro dinosaurios fuel el
# ultimo en ser descubierto y quien lo hizo. [actividad para resolver]
alertsClaire = Lista()
alertsOrdenDino = Lista()
dinosaursLista = Lista()

for dinosaur in dinosaurs:
    dinosaursLista.insertar(
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
dinosaursLista.barrido()
ultimo_descubierto = dinosaursLista.ultimo_descubierto().info;
descubridor = ultimo_descubierto.named_by.split(',')[0]
anio =  ultimo_descubierto.named_by.split(',')[-1]
print('')
print('El ultimo dinosaurio descubierto es el', ultimo_descubierto.name, 'en', anio)
print('Y fue descubierto por', descubridor)

# Lowery Cruthers: Hola new developer, lamento que no te podamos hacer un presentación formal,
# pero necesito que resuelvas esto de inmediato. Por favor debes hacer un scripts que procese el
# archivo en esta USB llamado “alerts.txt”, necesito los datos ordenados por fecha para Claire y otro
# ordenado por nombre de dinosaurio para cruzarlo con los datos del sistema de incidentes. Por favor
# date prisa lo necesito urgente poder listar esta información. Recuerda agregar el nombre del
# dinosaurio de acuerdo a su número. [actividad para resolver]
file = open('alerts.txt')
lines = file.readlines()
lines.pop(0)
for alert in lines:
    a = alert.split(';')
    dino = dinosaursLista.busqueda(int(a[2]), 'number').info
    dino.name

    alertsClaire.insertar(
        Alert(
            a[0],
            a[1],
            a[2],
            a[3].rstrip('\n'),
            dino.name,
            dino.type,
        ),
        'time'
    )


    alertsOrdenDino.insertar(
        Alert(
            a[0],
            a[1],
            a[2],
            a[3].rstrip('\n'),
            dino.name,
            dino.type,
        ),
        'dino_name'
    )
print('')
print('Listado ordenado para Claire')
alertsClaire.barrido()
print('')
print('Listado ordenado por nombre de Dino')
alertsOrdenDino.barrido()

# Dr. Wu: Les dije explícitamente que debemos mantener anónima toda la información respecto de las
# zonas WYG075, SXH966 y LYF010 por favor eliminen en este momento toda esa información de los
# datos procesados previamente. Ah casi me olvidaba de decirles modifiquen el registro de la zona
# HYD195 el nombre correcto del dinosaurio es Mosasaurus. [actividad para resolver]

alertsClaire.eliminar('WYG075', 'zone_code')
alertsOrdenDino.eliminar('WYG075', 'zone_code')
alertsClaire.eliminar('SXH966', 'zone_code')
alertsOrdenDino.eliminar('SXH966', 'zone_code')
alertsClaire.eliminar('LYF010', 'zone_code')
alertsOrdenDino.eliminar('LYF010', 'zone_code')

alertsClaire.busqueda('HYD195', 'zone_code').info.dino_name = 'Mosasaurus'
alertsOrdenDino.busqueda('HYD195', 'zone_code').info.dino_name = 'Mosasaurus'

# Simon Masrani: Oigan donde rayos se encuentra Claire, necesito que se encargue de la presentación
# de la nueva atracción del parque, además el teléfono de emergencias no para de sonar. Oye tu amigo,
# si tú el developer no recuerdo tu nombre pero debes ser el nuevo podrías atender el teléfono parece
# ser algo importante y no veo a Lowery por ningún lado. Necesito urgente un listado filtrado de los
# datos que solo incluya datos de los dinosaurios: Tyrannosaurus Rex, Spinosaurus, Giganotosaurus con
# nivel ´critical’ o ‘high’. [actividad para resolver]
print('')
print('Listado filtrado: ')
listadoFiltrado = Lista()
for i in range(alertsOrdenDino.tamanio()):
    dato = alertsOrdenDino.obtener_elemento(i)
    if((dato.dino_name in ['Tyrannosaurus Rex', 'Spinosaurus', 'Giganotosaurus'])
        & (dato.alert_level in ['critical', 'high'])):
        listadoFiltrado.insertar(dato, 'dino_name')

listadoFiltrado.barrido()

# Victor Hoskins: Pero que está pasando llevo un tiempo intentando comunicarme, las alarmas de
# incidentes están como locas, no sé a qué lugar debo ir primero con mi equipo de contención. Necesito
# que tomes toda la información de alertas, y las insertes en dos colas, una con los datos de dinosaurios
# carnívoros y otra con los herbívoros, descarten las de nivel ‘low’ y ‘medium’. [actividad para resolver]
print('')
colaHerviboros = Cola()
colaCarnivoros = Cola()
for i in range(alertsOrdenDino.tamanio()):
    dato = alertsOrdenDino.obtener_elemento(i)
    if(dato.alert_level in ['low', 'medium']):
        continue

    if(dato.dino_type.strip() == 'herbívoro'):
        colaHerviboros.arribo(dato)

    if(dato.dino_type.strip() == 'carnívoro'):
        colaCarnivoros.arribo(dato)

print('Lista Hervíboros')
for i in range(colaHerviboros.tamanio()):
    print(colaHerviboros.mover_al_final())
print('')
print('Lista Carnívoros')
for i in range(colaCarnivoros.tamanio()):
    print(colaCarnivoros.mover_al_final())

# Agente de Contención: Atención centro de monitoro no podemos acceder al sistema de colas de
# alertas por un aparente problema de conexión, atiendan las alertas en la cola de carnívoros y muestren
# en la pantalla (para que se publiquen en el canal de alerta de banda segura) la información pero
# descarten las provenientes de la zona EPC944, ya se encuentra una unidad de respaldo ahí. [actividad
# para resolver]
print('')
print('Atencion de cola carnivoros')
while(not colaCarnivoros.cola_vacia()):
    dato = colaCarnivoros.atencion()
    if(dato.zone_code != 'EPC944'):
        print(dato)


# Owen Grady: Oigan perdón que los molestes, pero no consigo que el sistema me funcione en mi
# notebook, podrían pasarme un listado de toda la información que tienen procesada del archivo, pero
# solo de los dinosaurios Raptors y Carnotaurus; y los códigos de las zonas donde puedo encontrar
# dinosaurios Compsognathus. Que sea lo antes posible hoy es un día muy agitado. [actividad para 
print('')
listaProces = Lista()
listaZones = Lista()
for i in range(alertsOrdenDino.tamanio()):
    dato = alertsOrdenDino.obtener_elemento(i)
    if(dato.dino_name in ['Raptors (Dromaeosauridae)', 'Carnotaurus']):
        listaProces.insertar(dato, 'dino_name')
    if(dato.dino_name == 'Compsognathus'):
        listaZones.insertar(dato.zone_code, 'dino_name')

print('Listado dinosaurios Raptors y Carnotaurus')
listaProces.barrido()
print('')
print('Listado códigos de zonas de Compsognathus')
listaZones.barrido()

# Dennis Nedry (anotaciones): desde que Jurassic Park arranco la calve a ha sido ‘mosquito’ pero que
# significa esto realmente, si lo consideramos como si fueran números estas serian las situaciones:
# 1. si el número está entre 33 y 47 su valor alfanumérico esta ok.
# 2. caso contrario
# si número es divisible por 3 entonces (número // 2) + 9 (es tu nuevo valor alfanumérico)
#  sino número -14 (es tu nuevo valor alfanumérico)
# en cualquiera de los casos debes continuar procesandolo, es una solución parcial.
# 3. al final obtendrás la clave si sabes cómo hacer las cosas, pero recuerda ‘mosquito’ es la clave
# de todo.
# Suerte intentado descifrar la contraseña. [actividad para resolver]
print('')
def clave(number):
    if((number > 33) & (number < 47)):
        return 'ok'
    if((number % 3) == 0):
        return clave((number // 2) + 9)
    else:
        return clave(-14)

print(clave(37))