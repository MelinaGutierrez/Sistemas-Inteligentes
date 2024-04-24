# Solucionador del Cubo de Rubik

## 1. Autor
- **Nombre completo:** Melina Aylem Gutierrez Calizaya

## 2. Descripción del Proyecto
Este proyecto consiste en crear un solucionador del Cubo de Rubik utilizando técnicas aprendidas en la materia de Sistemas Inteligentes. El objetivo es implementar heurísticas y el algoritmo A* para resolver el cubo de manera eficiente.(Pd. No se logro aún).

## 3. Requerimientos del Entorno de Programación
- **Entorno de desarrollo:** Visual Studio Code
- **Lenguaje de Programación:** Python
<img src="/Mini Proyecto Cubo Rubik/src/Python-logo.png" width="100" height="100">
<img src="/Mini Proyecto Cubo Rubik/src/visual-studio-code-icon.webp" width="100" height="100">

## 4. Manual de Uso
- **Instalación:** Puedes clonar este repositorio o descargarlo como archivo ZIP.
![Git clone](/Mini%20Proyecto%20Cubo%20Rubik/src/git_clone.png)
![Zip](/Mini%20Proyecto%20Cubo%20Rubik/src/zip.png)

- **Formato de Carga del Cubo:** El archivo de texto debe contener los estados del cubo en formato de matrices.

<img src="/Mini Proyecto Cubo Rubik/src/formato_cubo.png" width="100" >

- **Instrucciones para Ejecutar el Programa:** 
    1. Descarga o clona el proyecto.
    2. Abre una terminal en la carpeta del proyecto en Visual Studio Code.
        2.1. No olvides abrir la terminal en el Mini Proyecto Cubo Rubik
        ![Terminal](/Mini%20Proyecto%20Cubo%20Rubik/src/terminal.png)
    3. Ejecuta el siguiente comando: `python resolver_cube_o.py`

## 5. Diseño e Implementación
- **Modelo del Problema:**
  El modelo del problema consiste en representar un cubo de Rubik o al menos se intento, almacenando el estado de cada una de sus caras. Cada cara del cubo se representa como una matriz 3x3, donde cada elemento de la matriz corresponde a un color. El objetivo es encontrar una secuencia de movimientos que lleven el cubo desde un estado inicial (desordenado) a un estado final (ordenado).
![cubo s](/Mini%20Proyecto%20Cubo%20Rubik/src/cubo_simulador.png)
- **Algoritmo y Heurísticas:**
  Se trato de implementar el algoritmo A* para resolver el cubo de Rubik. A* nos ayuda a encontrar el camino mas corto y eficiente para resolver un problema en este caso pense que me ayudaria a resolver el cubo, si tan solo lo hubiera logrado, talvez. Se penso en usar la distancia de Manhattan, que mide la cantidad de movimientos necesarios para llevar cada cubo a su posición objetivo.
![cubo r](/Mini%20Proyecto%20Cubo%20Rubik/src/cubo_resuelto.png)
  Digamos que queremos resolver el cubo , cada ovimiento que hagamos sea: Up, Down, Front, Back, Left y Right, es tomar un camino, algunos movimientos seran mas optimos que otros claramente(bueno la verdad no se armar el cubo, pero supongo que algunos movimientos son mejores que otros para armar el cubo o armarlo mas rapido para los que saben armarlo). Entonces en mi solucion ideal A* iba a ser el pro que logre resolver el cubo lo mas rapido posible, lo que debio hacer es medio como trampa ya que digamos que hace 2 movimientos en donde en ambos volvera a su estado inicial despues de hacer cada movimiento para analizar cual le conviene mas, y despues de 1000 años de evaluacion de movimientos posibles, A* nos diria cuales son los pasos para resolver el cubo.

Para resolver el cubo, se definen seis tipos de movimientos, donde cada movimiento implica reorganizar los colores en las caras del cubo de acuerdo con la dirección del movimiento.

## 6. Trabajo Futuro
- **Tareas Pendientes:**
 MUY IMPORTANTE: TERMINAR DE IMPLEMENTAR EL SOLUCIONADOR Y LAS HEURISTICAS; SIN COMPROMETER EL APRENDIZAJE, ADEMAS DE BUSCAR MEJORES FORMAS DE PROGRAMAR EN PY
  - Lograr que funcione y si logre mover el cubo para que analice todos los moviemientos.
  - Mejorar la eficiencia del algoritmo(Usar POO)
  - Implementar muy bien la heuristica, ya que le faltan cosas.
  - Aplicar desarrollo incremental para poder hacer un mejor seguimiento de la tarea.
  - Separa por funcionalidad y refactorizar.

  <img src="/Mini Proyecto Cubo Rubik/src/productividad.webp">

## Ejemplo de Uso
```python
# Crear una instancia del CuboRubik
cubo_resolver = CuboRubik()

# Cargar el estado inicial del cubo desde un archivo de texto
cubo_resolver.leer_cubo('cube_scramble2.txt')

# Mostrar el cubo antes de resolverlo
print("Cubo antes de resolver:")
cubo_resolver.mostrar_cubo()

# Resolver el cubo usando A*
cubo_resuelto = cubo_resolver.resolver_cubo_a_estrella()

# Mostrar el cubo después de resolverlo
if cubo_resuelto:
    print("\nCubo después de resolver:")
    cubo_resuelto.mostrar_cubo()
else:
    print("\nNo se pudo resolver el cubo.")
