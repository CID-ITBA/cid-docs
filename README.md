# CID-DOCS

[![Documentation Status](https://readthedocs.org/projects/cid-docs/badge/?version=latest)](https://cid-docs.readthedocs.io/en/latest/?badge=latest)

## Bienvenidos al sitio de documentación del <b>Centro de investigación Digitial</b> del Instituto Tecnologico de Buenos Aires

Hemos armado un tutorial que les enseñara paso a paso como auto-documentar un proyecto con [Sphinx](https://www.sphinx-doc.org) y publicar la documentación de su proyecto en [Read the Docs](https://readthedocs.org).

Una vez alcanzado este objetivo ahondaremos en como publicar nuestro paquete en PYPI para poder instalarlo mediante pip.

## :construction: Instalación con pip :construction:
En esta fase de prueba por favor instale con pip:
```shell
pip install SimiLab
```
Y para testear su funcionamiento
```python
>>> import SimiLab as sl
>>> test = sl.testClass()
Class instantiation succesful
>>> test.say_hello()
Hey! This seems to be working
```

## Preparando los Docstrings

Se llaman docstring a un formato especial de comentario que se utiliza para dar estructura a la documentación. Con estos podemos especificar detalladamente el funcionamiento de las clases y metodos implementados.

Existen diversos formatos de doctrings compatibles con [Sphinx](<[https://link](https://www.sphinx-doc.org)>).

 <ul>
    <li>Sphynx Style</li>
    <li>Google Style</li>
    <li>Numpy Style</li>
</ul>

Pueden aprender más acerca de estos y como utilizarlos [aquí](https://https://www.datacamp.com/community/tutorials/docstrings-python).

En nuestro caso hemos decidido utilizar Numpy Style por su simplicidad y practicidad para documentar.

```python
class Hotel:
    """
    El hotel tiene varias habitaciones

    Parameters
    --------
    nombre : str
                Nombre del hotel
    cuartos : int
                Cantidad de cuartos en el hotel
    """


    def __init__(self, nombre, cuartos):
        self.cuartos = cuartos
        self.nombre = nombre

    def make_meal(self, name, size, temperature)
        """
        Parameters
        --------
        name : str
                Type of food to prepare
        size : float
                How many kilos to prepare
        temperature : float
                    How hot it should be

        Returns
        --------
        meal : object
                Your desired meal

        Raises
        ------
        ValueError
            if 'name' is not present is not a meal.
        Examples
        --------
        >>> hotel = Hotel("PythonHotel", 400)
        >>> hotel.make_meal("Fried Chicken", 4)

        See Also
        --------
        Hotel.make_dessert : for instruction on how to make a dessert.

        """
        pass

    def make_dessert(self, name, size)
        """
        ...
        """
        pass

```

Para más ejemplos de documentación les recomendamos mirar el codigo de fuente de [SimilarityLab](https://github.com/CID-ITBA/cid-docs) o [Numpy](https://github.com/numpy/numpy)

## Empaquetando

Nuestro proyecto tiene que poder ser identificado como un paquete distribuible de Python. Para ello necesitamos dos archivos escenciales, `__init__.py` y `setup.py`. Ambos deben alojarse en el mismo directorio que nuestro modulo.

El archivo `__init__.py` solamente deber exisitir y puede estar vacio. No hay más requerimientos que esos.

Para que [Sphinx](https://www.sphinx-doc.org) pueda rastrear la versión en la que actualmente estamos trabajando, como así conocer las dependencias de nuestro proyecto, es necesario generar un archivo `setup.py`.

El mismo debe encontrarse en el mismo directorio que nuestra clase.

```python
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ProjectName",
    version="0.0.1",
    author="Example Author",
    author_email="author@example.com",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords='Cats dogs words',
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
          'numpy',
          'scipy',
          'SimiLab',
      ],
    python_requires='>=3.6',
)

```

# Sphinx

## Primeros pasos

Para poder generar nuestra documentación vamos a requerir instalar [Sphinx](https://www.sphinx-doc.org).

```python
pip install sphinx
```

y para generar nuestro archivo de requerimientos necesitaremos

```python
pip install pipreqs
```

Una vez instalados corremos desde el directorio raiz de nuestro proyecto

```shell
>\MyProject sphinxquickstart docs -ext-autodoc
```

Recomendamos seguir las opciones por defecto que nos ofrece la CLI de [Sphinx](https://www.sphinx-doc.org).

Una vez terminado deberiamos tener la siguiente estructura:

```
-MyProject
    -MyPackage
        -package.py
        -__init__.py
        -setup.py
    -docs
        -docs
        -conf.py
        -index.rst
        -make.bat
        -Makefile
```

## :construction: index.rst :construction:

Así como en HTML se trabaja con un archivo principal llamado index.html. Cuando trabajamos con sphinx vamos a tener un punto de entrada llamado index.rst. Aquí ensamblaremos la estructura de nuestra documentación.
En este caso utilizamos reStructuredText como lenguaje de markup.

```rst
Welcome to SimilarityLab's documentation!
=========================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   pages/getting-started

.. automodule:: SimiLab
   :members:

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

```

La indentación es vital para no incurrir en errores al momento de compilar.

Por ejemplo la directiva <b>automodule</b> le dice a Sphinx que tome todos los docstrings contenidos en SimiLab

## conf.py

El archivo conf.py es generado de forma automatica luego de llamar a sphinxquickstart.
Para permitir que [Sphinx](https://www.sphinx-doc.org) encuentre nuestro paquete es necesario indicarle donde se encuentra. Sugerimos utilizar de ejemplo el archivo conf.py que se encuentra [aquí](https://github.com/CID-ITBA/cid-docs/blob/master/docs/conf.py).

### Recordar configurar

<ul>
<li>Extensiones de Sphinx</li>
<li>Path</li>
<li>Tema (sugerimos 'default')</li>
</ul>

## Archivos .readthedocs.yml y requirements.txt

Ciertamene la mayoría de los proyectos requieren ciertas dependecias externas. Sin embargo, aunque sean paquetes de terceros, hay que especificar cuales son.

<ol>
    <li>En el directorio raiz crear un archivo .readthedocs.yml</li>
    <li>Copiar el archivo de <a href=https://github.com/CID-ITBA/cid-docs/blob/master/.readthedocs.yml>ejemplo</a></li>
</ol>
Luego debemos generar nuestro archivo de requerimientos

```shell
 >MyProject/MyPackage pipreqs > requirements.txt
```

Se recomienda mover el mismo a la carpeta <b>docs</b>

# :construction: make html, rdft :construction:
