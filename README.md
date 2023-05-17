<div align="center" id="top"> 


  <!-- <a href="https://prueba_chr.netlify.app">Demo</a> -->
</div>

<h1 align="center">Prueba_Chr</h1>



## Sobre el proyecto ##

Prueba tecnica para cargo desarrollador backend en CHR.

## Tecnologias ##

Las siguientes herramientas fueron utilizadas en este proyecto:

- [Django]()
- [Selenium]()
- [PostgreSQL]()

## Requerimientos ##

Antes de empezar, necesitas tener instalado [PostgreSQL](https://www.postgresql.org/download/) instalado y haber creado una base de datos dentro llamada 'apidata' o como gustes. Tendra que coincidir luego en el archivo settings.py

## Empezamos ##

```bash
# Clona el proyecto en una carpeta
$ git clone https://github.com/PDePanchito/Prueba_Chr.git

# Navega al directorio del proyecto
$ cd prueba

# Instala los paquetes necesarios
# Instalara las librerias usadas en el proyecto. Si falta alguna, habra error
$ pip install -r libraries.txt

```
En este punto necesitas configurar la base de datos:

1. Abre el archivo settings.py ubicado en 'prueba'.
2. Navega hasta 'DATABASES' y configura los campos acorde a tu informacion personal.
3. Asegurate de que el puerto a usar no este ocupado.

Luego

```bash
# Levantar el proyecto
$ python manage.py runserver

# El servidor iniciara en http://127.0.0.1:8000/
```
4. Ejecuta lo siguiente para crear las tablas en la base de datos:

```bash 
$ python manage.py makemigrations
$ python manage.py migrate
```

Con esto, las tablas deberian crearse de forma exitosa en tu base de datos si es que la conexion fue correcta.


Una vez este levantado el proyecto:

## Tarea 1 ##

1. Navega hasta http://127.0.0.1:8000/, veras una lista de posibles rutas para navegar.
2. Navega hasta http://127.0.0.1:8000/api/ para visualizar informacion directamente desde la API.
3. Navega hasta http://127.0.0.1:8000/api-store/ para guardar informacion de la API en la base de datos. De haberse guardado bien, deberias ver un JSON conteniendo 'success'.
4. Navega hasta http://127.0.0.1:8000/bootstrapview/ para visualizar la informacion proveniente de la API, pero esta vez utilizando como fuente la base de datos y los datos almacenados. Ademas, veras tarjetas hechas con Bootstrap5.

## Tarea 2 ##
1. Ejecuta el siguiente comando:

```bash
# Inicia el script que obtiene informacion de la tabla, recorriendo todas las  paginas existentes

$ python manage.py scraping_command

```
Una vez listo, veras un mensaje en verde de exito que contiene lo siguiente:
``` bash
  Scraping completed successfully
```

Lo que hizo fue, en segundo plano, hacer un recorrido por el sitio web mientras obtiene la informacion de las tablas. Luego, almacena esta informacion en un archivo llamado 'data.json' ubicado en la raiz del proyecto.

2. Navega hasta http://127.0.0.1:8000/scrape-data/ para visualizar la informacion obtenida previamente.
3. Navega hasta http://127.0.0.1:8000/scrape-view/ para visualizar la informacion pero esta vez construida con Bootstrap5 utilizando una tabla.


Creado por <a href="https://www.linkedin.com/in/franciscomartinez410/" target="_blank">Francisco Martinez</a>


<a href="#top">Back to top</a>
