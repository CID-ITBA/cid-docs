# CID-DOCS

[![Documentation Status](https://readthedocs.org/projects/cid-docs/badge/?version=latest)](https://cid-docs.readthedocs.io/en/latest/?badge=latest)

## Bienvenidos al sitio de documentación del <b>Centro de investigación Digitial</b> del Instituto Tecnologico de Buenos Aires

Hemos armado un tutorial que les enseñara paso a paso como auto-documentar un proyecto con [Sphinx](https://www.sphinx-doc.org) y publicar la documentación de su proyecto en [Read the Docs](https://readthedocs.org).

Una vez alcanzado este objetivo ahondaremos en como publicar nuestro paquete en PYPI para poder instalarlo mediante pip.

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

Para que [Sphinx](<[https://link](https://www.sphinx-doc.org)>) pueda rastrear la versión en la que actualmente estamos trabajando, como así conocer las dependencias de nuestro proyecto, es necesario generar un archivo `setup.py`.

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

Para poder generar nuestra documentación vamos a requerir instalar [Sphinx](<[https://link](https://www.sphinx-doc.org)>).

```python
pip install sphinx
```

y para generar nuestro archivo de requerimientos

```python
pip install pipresq
```

Una vez instalados corremos desde el directorio raiz de nuestro proyecto

```
>\MyProject sphinxquickstart docs -ext-autodoc
```

Recomendamos seguir las opciones por defecto que nos ofrece la CLI de [Sphinx](<[https://link](https://www.sphinx-doc.org)>).

Una vez terminado deberiaos tener la siguiente estructura:

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
En este caso se utiliza RestructuredText como lenguaje. Dada su complejidad nos limitaremos a mencionar las caracteristicas basicas que debe tener.

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

La indentación es vital en al

## :construction: conf.py :construction:

Work in progress

## :construction: .requirements.yml :construction:

## :construction: requirements.txt :construction:

<!-- pipreqs                        -->
<!-- El objetivo de utilizar [Sphinx]([https://link](https://www.sphinx-doc.org)) es el de auto-generar la documentación de nuestro paquete de Python. Para e
Generar un paquete distribuible de Python incluyendo __init__.py vacío y el correspondiente archivo setup.py
```shell
pip install sphinx
"""
Correr en el directorio raiz de nuestro paquete, es decir un nivel arriba de la carpeta de donde esta el paquete
"""
sphinx-quickstart docs
```

El comando nos guiara a traves de una serie de pasos. Se recomienda dejar todo en default salvo *nombres* y números de *version*.

Una vez hecho esto tendremos el siguiente árbol

root
 -paquete
 -docs -->
