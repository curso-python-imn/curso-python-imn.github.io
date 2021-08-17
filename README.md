## Configuración inicial

### Creación de un ambiente Conda

```shell
# Actualización de Conda
$ conda update -n base -c defaults conda

# Creación del ambiente
$ conda create -n curso-python-imn

# Activación del ambiente
$ conda activate curso-python-imn

# Instalación de módulos
$ conda config --env --add channels conda-forge
$ conda config --env --set channel_priority strict
$ conda install jupyter-book
$ conda install ghp-import

# Desactivación del ambiente
$ conda deactivate
```

### Creación del Jupyter Book y publicación inicial del sitio web

```shell
# Creación del Jupyter Book
$ jupyter-book create curso-python-imn

# Generación de archivos HTML (en el subdirectorio _build/html)
$ jupyter-book build curso-python-imn

# En este punto, se crea en GitHub el repositorio curso-python-imn.github.io

# Configuración del repositorio local
$ cd curso-python-imn
$ git init
$ git add .
$ git commit -m "Commit inicial"
$ git branch -M main
$ git remote add origin https://github.com/curso-python-imn/curso-python-imn.github.io.git
$ git push -u origin main

# Creación del branch gh-pages
ghp-import -n -p -f _build/html

# En este punto, se configura el repositorio para buscar los archivos de GH Pages en la rama gh-pages
# El sitio debe estar disponible en https://curso-python-imn.github.io/
```

## Publicación de modificaciones

```shell
$ jupyter-book build curso-python-imn

$ cd curso-python-imn

# Branch main
$ git status
$ git add .
$ git commit -m "###Comentario###"
$ git push

# Branch gh-pages
$ ghp-import -n -p -f _build/html
```
