# Scraper de noticias 

Proyecto realizado en el curso Ingenieria de datos con Python en la MOOC Platzi

El proyecto consta de un pipeline ETL el cual se encarga de realizar un scraping, realizar transformaciones para limpiar los datos y por ultimo se almacenan en una base de datos SQLite

El mismo se divide en:
#### Extracción
Se realizan extracciones automatizadas de la pagina [Montevideo Portal](https://www.montevideo.com.uy/index.html) pero también admite la posibilidad de agregar nuevas paginas para realizar scraping a través de la modificación del archivo [`config.yaml`](https://github.com/leonardoacosta91/ScraperNoticias/blob/master/extract/config.yaml)

#### Transformación
El proceso consta de las diferentes transformaciones:
1) add_newspaper_uid_column - Se encarga de agregar la pagina de origen al dataframe
2) extract_host - Extrae el host de la sub pagina
3) fill_missing_titles - Genera un titulo basándose en la URL para las filas que no se pudo obtener el titulo
4) drop_rows_with_missing_values - Se eliminan columnas con valores faltantes
5) remove_duplicate_entries - Remueve filas con titulo duplicado (Quedándose con el primer registro que aparece)
6) generate_uids_for_rows - Se genera un hash MD5 con la url para tener un id único
7) remove_new_lines_from_body - Se remueven los saltos de linea
8) tokenize_column - Utilizando NLTK se tokenizan los valores y devuelve la cantidad de palabras distintas

#### Carga
Se genera una tabla de SQLite y se guardan allí los registros con el siguiente esquema:\
id - string - primary key\
body - string\
host - string\
title - string\
newspaper_uid - string\
n_tokens_body - string\
n_tokens_title - string\
url - string - unique

### Pre-requisitos 📋
Es necesario tener python 3.6 en adelante.

Las dependencias y los modulos necesarios vienen especificados en [`requirements.txt`](https://github.com/leonardoacosta91/ScraperNoticias/blob/master/requirements.txt)
Ejecutar el siguiente comando para clonar y comenzar con el proyecto

```
git clone https://github.com/leonardoacosta91/ScraperNoticias
cd ScraperNoticias
```

### Instalación 🔧

Crear un ambiente virtual y ejecutar el siguiente comando para instalar todo lo necesario.
```
pip install -r requirements.txt
```
## Despliegue 📦

Ejecutar:
```
pipeline.py MontevideoPortal
```
Y comenzara a realizarse el pipeline correspondiente al ETL

## Autores ✒️


* **Leonardo Acosta** - *Proyecto completo* - [Leonardo Acosta](https://github.com/leonardoacosta91)

## Cierre ⌨️

* Cualquier corrección o sugerencia sobre el código es bienvenida ya que este proyecto lo pensé para practicar mis habilidades
* Muchas gracias por llegar hasta aquí