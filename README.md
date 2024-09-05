# Aplicación de Agencia de Autos

## Descripción

Esta es una aplicación web para la gestión de una agencia de autos. Permite a los usuarios crear, buscar, editar y eliminar registros de autos, así como acceder a información sobre la agencia.

## Integrantes

- **Alexis Borsato**
- **Axel Godoy**

## Funcionalidades

- **Crear auto**: Permite añadir nuevos autos a la base de datos.
- **Buscar**: Permite buscar autos por diferentes criterios.
- **Editar**: Permite modificar la información de autos existentes.
- **Eliminar**: Permite eliminar autos de la base de datos.
- **Sobre nosotros**: Proporciona información sobre la agencia y el equipo.

## Capturas de Pantalla

A continuación, se muestran algunas capturas de pantalla de la aplicación en funcionamiento:

### Página Principal

![Página Principal](/Entrega1--GodoyBorsato/imgs/Principal.png)

Descripción: Muestra la interfaz principal donde los usuarios pueden ver la lista de autos y acceder a las funcionalidades básicas.

### Crear Auto

![Crear Auto](/Entrega1--GodoyBorsato/imgs/Crear.png)

Descripción: Interfaz para añadir un nuevo auto a la base de datos. Aquí se ingresan los detalles del auto.

### Buscar Auto

![Buscar Auto](/Entrega1--GodoyBorsato/imgs/Buscar.png)

Descripción: Permite a los usuarios buscar autos por diferentes criterios, como marca, modelo, etc.

### Editar Auto

![Editar Auto](/Entrega1--GodoyBorsato/imgs/Editar.png)

Descripción: Pantalla para modificar la información de un auto existente.

### Eliminar Auto

![Eliminar Auto](/Entrega1--GodoyBorsato/imgs/EditarEliminar.png)

Descripción: Confirmación para eliminar un auto de la base de datos.

### Sobre Nosotros

![Sobre Nosotros](/Entrega1--GodoyBorsato/imgs/SobreNosotros.png)

Descripción: Página con información sobre la agencia y el equipo de desarrollo.

## Requisitos Previos

Antes de comenzar, asegúrate de tener instalado Python y pip en tu sistema.

## Instalación y Configuración

1. **Clonar el Repositorio**

   ```bash
   git clone <URL_DEL_REPOSITORIO>
   cd <NOMBRE_DEL_REPOSITORIO>
   Crear Entorno Virtual
   ```

## Crear Entorno Virtual

Instalar `virtualenv` si no lo tienes:

```bash
pip install virtualenv
```

Crear un entorno virtual:

```bash
python -m venv venv
```

Activar el entorno virtual:
En sistemas Unix/Linux/Mac:

```bash
source venv/bin/activate
```

En sistemas Windows:

```bash
.\venv\Scripts\activate
```

Instalar Dependencias
Instala las dependencias del proyecto especificadas en el archivo requirements.txt:

```bash
pip install -r requirements.txt
```

Realizar Migraciones
Crea y aplica las migraciones para la base de datos:

```bash
python manage.py makemigrations
python manage.py migrate
```

Levantar el Servidor
Inicia el servidor de desarrollo:

```bash
python manage.py runserver

```

Accede a la aplicación desde tu navegador en http://127.0.0.1:8000.
