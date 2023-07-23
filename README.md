# Rover-Brain

## Usage:
Para instalar en una nueva estación recomiendo eliminar los dir:

1. build/
2. install/
3. log/

Este módulo está construido para usarse en ROS2, sin embargo, los modulos del paqueta ```brain_system```, no pueden correr de la forma convencional

Por ello recomendamos seguir estos pasos:

Instalamos cualquier paquete faltante que sea necesario como ´´´std_msgs ´´´
´´´bash
rosdep install -i --from-path src --rosdistro foxy -y
´´´ 

### EN UNA NUEVA TERMINAL REALIZAR LO SIGUIENTE

Ejecuta desde la carpeta raíz rover_nuclues

´´´bash
$ source install/setup.bash
´´´

Normalmente se ejecutaría lo siguiente:

´´´bash
$ ros2 run brain_system talker

´´´
Y en otra terminal

´´´bash
$ ros2 run brain_system listener
´´´ 

Sin embargo para la versión 1.0.0 no ha podido ser ejecutado con éxito

En otro caso recomendamos realizar lo siguiente:

´´´bash
$ cd src/brain_system/
´´´

en una terminal ejecutar:

´´´bash
$ python3  publisher_member_function.py

´´´

Deberá desplegar una pantalla la serie de mensajes que son enviados

´´´bash
$ python3 subscriber_member_function.py
´´´

Deberá desplegarse una pantalla con la serie de mensajes recibidos.


###  FIN DEL INSTRUCTIVO
