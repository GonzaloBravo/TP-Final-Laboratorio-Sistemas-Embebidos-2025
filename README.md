# TP Final - Laboratorio de Sistemas Embebidos - *Ingeniería en Computación - 2025 -*  :computer: :robot:
- *Alumnos:* Juan Avilés, Gonzalo Ezequiel Bravo, Sandy Pérez Rosa
  
## - Plataforma de Atención Automatizada/Interactiva para la Optimización de Servicios mediante una Red de Área Local -

 Los sistemas embebidos están presentes en la mayoría de los dispositivos con los que interactuamos en la vida cotidiana: teléfonos celulares, electrodomésticos, juguetes, aplicaciones aeroespaciales, industriales, instrumental médico, equipamiento de automóviles, etc. Por la naturaleza de las aplicaciones y sus inherentes ventajas, existe un creciente interés en utilizar redes inalámbricas para la comunicación en redes de sistemas embebidos. Este proyecto presenta una plataforma modular de atención automatizada, desarrollada mediante sistemas embebidos interconectados mediante una red WiFi local.

## :clipboard: Descripción del proyecto:

 El sistema integra una botonera física, una aplicación web para la gestión de pedidos, un robot móvil con navegación autónoma, y un servidor. La comunicación se realiza de manera asincrónica basada en protocolos UDP/IP y TCP/IP. Su arquitectura distribuida y escalable lo posiciona como una solución adaptable a diferentes entornos. Los sistemas embebidos y la conectividad en red permiten automatizar procesos simples de atención al cliente. El objetivo principal es aplicar conocimientos de hardware, redes y programación para desarrollar un entorno funcional simulado que combine interacción física (botonera) y digital (aplicación web), coordinada por un robot móvil.

 El desarrollo del sistema se realizó mediante un enfoque iterativo y modular, combinando etapas de diseño, implementación y prueba en entornos reales simulados. Se abordaron tanto aspectos de hardware como de software embebido, priorizando la comunicación en red y la integración funcional entre componentes. Para la construcción del hardware se utilizaron dos placas Raspberry Pi, protoboard, LEDs y botones pulsadores, kit del robot con tracción diferencial, un dispositivo móvil y una notebook. El software fue desarrollado en Python, HTML, CSS y JavaScript, librerías y frameworks Flask, Rpi.GPIO, Socket y HTTP (TCP/UDP). El desarrollo se dividió en diferentes etapas: 
 - Diseño de arquitectura distribuida 
 - Integración de hardware 
 - Programación de módulos 
 - Comunicación en red 
 - Pruebas en entorno simulado

 El desarrollo de este proyecto permitió aplicar de manera integral los conocimientos adquiridos sobre sistemas embebidos, microcontroladores, redes de comunicación, lenguajes de programación y diseño de interfaces web. La propuesta de una plataforma de atención automatizada/interactiva demostró ser viable en entornos simulados, mostrando tiempos de respuesta adecuados y una correcta interacción entre los distintos módulos distribuidos en red.
 
## :file_folder: Carpetas 

- ***src:*** contiene el código fuente del proyecto :hammer_and_wrench:
  - Cliente
  - Servidor
  - App Web
  - Robot
    
- ***docs:*** cotiene la documentación del proyecto :clipboard:
    - Informe
    - Documento de planificación
    - Póster
