# Proyecto-final-CI5437

Este proyecto es un solucionador de nonogramas que utiliza una interfaz gráfica para cargar y resolver nonogramas.

## Requisitos

Para ejecutar este proyecto necesitas tener instalado Python 3 y las siguientes bibliotecas:

- pysat
- tkinter

Puedes instalar estas bibliotecas con pip:

```
pip install python-sat
pip install tk
```

## Clonar el Repositorio

Para obtener una copia del código fuente, puedes clonar el repositorio de GitHub usando git:

```
git clone git@github.com:dxniela/Proyecto-final-CI5437.git
```

## Ejecución

Para ejecutar el proyecto, navega hasta el directorio del proyecto y ejecuta el script principal con Python 3:

```
cd Proyecto-final-CI5437
python3 main.py
```

Al ejecutarse la interfaz, debes cargar un archivo de prueba, por ejemplo el test6.txt, en el botón _Cargar nonograma_ y luego darle al botón _Resolver nonograma_ para que el programa resuelva el nonograma y muestre el resultado.

## Archivo de entrada

Se utiliza un archivo de texto plano para describir el problema. El archivo contiene un solo objeto con los siguientes campos:

```
<nro_columnas> <nro_filas>
<fila_1>
<fila_2>
...
<columna_1>
<columna_2>
...
```

donde cada fila y columna se describe como una lista de números separados por un espacio, que representan la cantidad de casillas consecutivas que deben estar coloreadas en esa fila o columna.
