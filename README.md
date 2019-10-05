# CID-DOCS 
[![Documentation Status](https://readthedocs.org/projects/cid-docs/badge/?version=latest)](https://cid-docs.readthedocs.io/en/latest/?badge=latest)

## Bienvenidos al sitio de documentación del <b>Centro de investigación Digitial</b> del Instituto Tecnologico de Buenos Aires

Hemos armado un tutorial que les enseñara paso a paso como auto-documentar un proyecto con [Sphinx]([https://link](https://www.sphinx-doc.org)) y publicar la documentación de su proyecto en [Read the Docs](https://[https://readthedocs.org/]) 

## Paso 1
### Prepar los Docstrings 
Se llaman docstring a un tipo especial de comentario que podemos utilizar para documentar nuetro codigo. De esta forma logramos unificar documentación y codigo en un mismo sitio.

Existen diversos formatos de doctrings compatibles con [Sphinx]([https://link](https://www.sphinx-doc.org)).
 
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
