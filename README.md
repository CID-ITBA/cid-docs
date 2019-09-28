# cid-docs

## Pasos para generar la documentación

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
 -docs
