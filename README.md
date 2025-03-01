<h1 align="center"> Proyecto Final Sistemas Operacionales </h1>
  
<p>Simulador del funcionamiento de un Sistema Operativo,donde se implementa las funcionalidades de procesos,gestión de memoria y uso de un sistema multihilo</p>

<p align="center">
  <img src ="https://cursos.clavijero.edu.mx/cursos/182_so/modulo2/imagenes/imagen3.jpg" width="800" height="300"></img>
</p>

<h2>Conceptos</h2>
<ul>
  <li><b>Proceso: </b>Unidad básica de trabajo que maneja un sistema operativo (SO),es la instancia de un programa en ejecución</li>
  <li><b>BCP: </b>Bloque de Control de Procesos,estructura de datos utilizada por el sistema operativo para gestionar y controlar los procesos en el sistema</li>
  <li><b>Memoria: </b>Parte fisica y lógica que permite almacenar datos e instrucciones que los procesos necesitan para ejecutarse,aqui encontramos a la memoria RAM y la memoria virtual</li>
  <li><b>Página: </b>Bloques de memoria del mismo tamaño,utilizados en la gestión de memoria virtual</li>
  <li><b>Preeminencia: </b>Prioridad que se le asigna a un proceso para determinar en que orden debe ser atendido</li>
</ul>

<h2>Funcionalidades</h2>
<h4>Creación de procesos</h4>
<ul>
  <li>ID proceso</li>
  <li>Tamaño</li>
  <li>Recursos</li>
  <li>Preminencia</li>
  <li>Número de hilos</li>
</ul>

<h4>Estados de los procesos</h4>
<ul>
  <li>Nuevo</li>
  <li>Listo</li>
  <li>Ejecucion</li>
  <li>Terminado</li>
  <li>Bloqueado</li>
</ul>

<h4>Gestión de memoria</h4>
<ul>
  <li>Memoria Principal: RAM</li>
  <li>Virtual</li>
</ul>

<h4>Mutlihilos</h4>
<ul>
  <li>Simulación de múltiples procesadores</li>
</ul>
  
<h2>Herramientas usadas</h2>
<ul>
  <li><b>Lenguaje de programación: </b>Python 3.12.5</li>
  <li><b>IDE: </b>Visual Studio Code</li>
 <!-- <li>Listo</li>
  <li>Ejecucion</li>
  <li>Terminado</li>
  <li>Bloqueado</li>-->
</ul>

<h2>Modulos Usados</h2>
<ul>
  <li>Math</li>
  <li>Random</li>
  <li>Flask</li>
  <li>Flask-Bootstrap</li>
  <li>Flask-WTF</li>

</ul>

<h2>Como ejecutar el proyecto</h2>

- Crear entorno virtual para evitar conflictos

  ```
      python -m venv venv
  ```
- Activar entorno virtual para evitar conflictos
  
  ```
    venv\Scripts\activate
  ```
- Instalar dependencias necesarias para usar Flask en este proyecto
  
  ```
    pip install -r requirements.txt
  ```
- Confirmar que todo se instalo correctamente

  ```
    pip list
  ```
- Ejecutar la aplicación 
  ```
    python app.py
  ```
