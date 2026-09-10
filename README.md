# Sistema de Inventario

Aplicación web de gestión de inventario para una tienda de tecnología.

El proyecto comenzó como una aplicación de línea de comandos (CLI) desarrollada con Python y SQLite, y evolucionó progresivamente hacia una aplicación web utilizando Flask, PostgreSQL y SQLAlchemy ORM.

Actualmente incluye un CRUD completo de productos, búsqueda, paginación, validaciones, mensajes al usuario, API REST y pruebas automatizadas.

## Características

* CRUD completo de productos.
* Creación, modificación y eliminación de productos.
* Listado paginado.
* Búsqueda por nombre o descripción.
* Validaciones en backend.
* Mensajes de éxito y error mediante Flash Messages.
* Interfaz web responsive con diseño Dark Tech.
* Indicadores visuales para productos con stock bajo o agotado.
* API REST.
* Pruebas automatizadas con pytest.
* PostgreSQL como base de datos principal.
* SQLAlchemy ORM para acceso a datos.
* Aplicación CLI original conservada como código legacy.

## Tecnologías

* Python 3.12
* Flask
* PostgreSQL
* SQLAlchemy ORM
* Jinja
* HTML5
* CSS3
* pytest
* Git
* GitHub

## Arquitectura

La aplicación separa las responsabilidades principales en diferentes capas:

```text
Flask
  │
  ├── Web Routes
  │       │
  │       ▼
  │     CRUD
  │       │
  │       ▼
  │   SQLAlchemy ORM
  │       │
  │       ▼
  │   PostgreSQL
  │
  └── REST API
          │
          ▼
        CRUD
```

## Estructura

```text
inventario-web/

├── app.py
├── main.py
├── requirements.txt
├── .env
├── .gitignore
│
├── static/
│   └── css/
│       └── style.css
│
├── templates/
│   ├── inicio.html
│   ├── productos.html
│   ├── crear_producto.html
│   └── modificar_producto.html
│
├── web/
│   ├── __init__.py
│   ├── routes/
│   ├── crud/
│   └── api/
│
├── database/
│   ├── __init__.py
│   ├── conexion.py
│   ├── models.py
│   └── tablas.py
│
├── tests/
│   ├── __init__.py
│   ├── conftest.py
│   ├── test_crud.py
│   └── test_api.py
│
├── productos/
│   └── crud/
│
└── cli/
    └── menu.py
```

## Modelo de datos

La aplicación administra productos mediante la tabla `productos`:

| Campo         | Tipo             | Descripción         |
| ------------- | ---------------- | ------------------- |
| `id`          | INTEGER / SERIAL | Identificador único |
| `nombre`      | VARCHAR          | Nombre del producto |
| `descripcion` | TEXT             | Descripción         |
| `precio`      | NUMERIC          | Precio              |
| `stock`       | INTEGER          | Cantidad disponible |

## Rutas web

| Ruta                        | Método   | Descripción                |
| --------------------------- | -------- | -------------------------- |
| `/`                         | GET      | Página principal y listado |
| `/page/<page>`              | GET      | Listado paginado           |
| `/productos`                | GET      | Acceso al listado          |
| `/productos/crear`          | GET/POST | Crear producto             |
| `/productos/<id>/modificar` | GET/POST | Modificar producto         |
| `/productos/<id>/eliminar`  | POST     | Eliminar producto          |
| `/productos/buscar`         | GET      | Buscar productos           |

## API

La API está disponible bajo:

```text
/api/v1
```

Endpoint principal:

```text
/api/v1/productos
```

Soporta:

* `GET` — listar productos.
* `POST` — crear producto.
* `GET /<id>` — obtener producto.
* `PUT /<id>` — actualizar producto.
* `PATCH /<id>` — actualizar parcialmente.
* `DELETE /<id>` — eliminar producto.

Consulta `API.md` para la documentación completa.

## Pruebas

El proyecto utiliza pytest.

Actualmente existen:

* 14 pruebas para las operaciones CRUD.
* 18 pruebas para la API REST.
* 32 pruebas en total.

Para ejecutarlas:

```bash
pytest tests/ -v
```

Las pruebas utilizan SQLite en memoria, mientras que el entorno de producción utiliza PostgreSQL.

## Configuración

La aplicación utiliza variables de entorno mediante `.env`.

Entre ellas:

```text
DATABASE_URL
SECRET_KEY
```

El archivo `.env` contiene configuración sensible y no debe compartirse.

## Ejecución

Servidor web:

```bash
python app.py
```

Aplicación CLI original:

```bash
python main.py
```

## Estado del proyecto

El prototipo funcional incluye actualmente:

* Aplicación web Flask.
* PostgreSQL.
* SQLAlchemy ORM.
* CRUD web.
* API REST.
* Paginación.
* Búsqueda.
* Validaciones.
* Flash Messages.
* Tests automatizados.

El proyecto se encuentra en una etapa de aprendizaje y evolución progresiva.

# API REST

## Base

La API utiliza el prefijo:

```text
/api/v1
```

El recurso principal es:

```text
/api/v1/productos
```

La API utiliza JSON para las solicitudes y respuestas.

## Listar productos

### Request

```http
GET /api/v1/productos
```

Devuelve el listado de productos.

La API soporta paginación.

## Obtener producto

```http
GET /api/v1/productos/<id>
```

Obtiene un producto específico mediante su identificador.

Ejemplo:

```http
GET /api/v1/productos/1
```

## Crear producto

```http
POST /api/v1/productos
```

Ejemplo de cuerpo JSON:

```json
{
  "nombre": "Notebook Lenovo",
  "descripcion": "Notebook para oficina",
  "precio": 650.00,
  "stock": 5
}
```

## Actualizar producto

```http
PUT /api/v1/productos/<id>
```

Actualiza un producto existente.

Ejemplo:

```json
{
  "nombre": "Notebook Lenovo ThinkPad",
  "descripcion": "Notebook empresarial",
  "precio": 750.00,
  "stock": 8
}
```

## Actualización parcial

```http
PATCH /api/v1/productos/<id>
```

Permite actualizar parcialmente un producto.

Por ejemplo:

```json
{
  "stock": 10
}
```

## Eliminar producto

```http
DELETE /api/v1/productos/<id>
```

Ejemplo:

```http
DELETE /api/v1/productos/1
```

## Respuestas

Las respuestas utilizan una estructura JSON basada en:

```json
{
  "success": true,
  "data": {}
}
```

En caso de error:

```json
{
  "success": false,
  "error": "Descripción del error"
}
```

## Operaciones disponibles

| Método | Endpoint                 | Operación             |
| ------ | ------------------------ | --------------------- |
| GET    | `/api/v1/productos`      | Listar                |
| POST   | `/api/v1/productos`      | Crear                 |
| GET    | `/api/v1/productos/<id>` | Obtener               |
| PUT    | `/api/v1/productos/<id>` | Actualizar            |
| PATCH  | `/api/v1/productos/<id>` | Actualización parcial |
| DELETE | `/api/v1/productos/<id>` | Eliminar              |

La API forma parte de la misma aplicación y reutiliza la capa CRUD basada en SQLAlchemy ORM.

# INSTALACION

## Requisitos

Se requiere:

* Python 3.12
* PostgreSQL
* pip
* Un entorno virtual de Python

## 1. Crear entorno virtual

Desde la raíz del proyecto:

```bash
python -m venv .venv
```

Activar el entorno virtual en Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

## 2. Instalar dependencias

```bash
pip install -r requirements.txt
```

## 3. Configurar variables de entorno

Crear un archivo `.env` en la raíz del proyecto.

Debe contener la configuración necesaria para la aplicación, incluyendo:

```text
DATABASE_URL=...
SECRET_KEY=...
```

La información de conexión depende de la configuración local de PostgreSQL.

## 4. Ejecutar la aplicación

```bash
python app.py
```

La aplicación Flask iniciará el servidor web.

## 5. Ejecutar las pruebas

```bash
pytest tests/ -v
```

Las pruebas utilizan SQLite en memoria para aislarlas de la base de datos PostgreSQL utilizada por la aplicación.

---

# DESARROLLO

## Arquitectura

La aplicación está organizada por responsabilidades.

### `app.py`

Es el punto de entrada de Flask y registra los componentes principales de la aplicación.

### `web/`

Contiene la funcionalidad web.

```text
web/
├── routes/
├── crud/
└── api/
```

### `web/routes/`

Contiene las rutas de la interfaz web separadas por operación.

```text
inicio.py
crear.py
modificar.py
eliminar.py
buscar.py
```

### `web/crud/`

Contiene las operaciones de acceso y modificación de productos.

```text
base.py
listar.py
obtener.py
crear.py
modificar.py
eliminar.py
```

`base.py` proporciona el contexto de conexión mediante `get_db()`.

### `web/api/`

Contiene la API REST.

```text
api/
├── __init__.py
└── routes/
    ├── listar.py
    ├── obtener.py
    ├── crear.py
    ├── put.py
    ├── patch.py
    └── eliminar.py
```

### `database/`

Contiene la configuración de persistencia.

```text
database/
├── conexion.py
├── models.py
└── tablas.py
```

`models.py` contiene el modelo `Producto` de SQLAlchemy.

`conexion.py` administra el engine, las sesiones y `get_db()`.

`tablas.py` corresponde a código legacy y actualmente no se utiliza.

### `tests/`

Contiene las pruebas automatizadas:

```text
tests/
├── conftest.py
├── test_crud.py
└── test_api.py
```

`conftest.py` proporciona fixtures para la aplicación, sesión de base de datos, cliente de pruebas y productos de prueba.

## Flujo de datos

Una solicitud web sigue aproximadamente este flujo:

```text
Cliente
   │
   ▼
Flask Route
   │
   ▼
CRUD
   │
   ▼
SQLAlchemy
   │
   ▼
PostgreSQL
```

En la API:

```text
Cliente HTTP
   │
   ▼
API REST
   │
   ▼
CRUD
   │
   ▼
SQLAlchemy
   │
   ▼
PostgreSQL
```

## Pruebas

Actualmente existen 32 pruebas:

```text
14 → CRUD
18 → API REST
```

Las pruebas CRUD cubren operaciones como:

* crear;
* obtener;
* listar;
* buscar;
* actualizar;
* eliminar.

Las pruebas de API cubren:

* GET;
* POST;
* PUT;
* PATCH;
* DELETE;
* casos exitosos;
* casos de error.

## Evolución

El proyecto evolucionó progresivamente:

```text
CLI Python + SQLite
        │
        ▼
Aplicación Web Flask
        │
        ▼
Validaciones + Flash Messages
        │
        ▼
Refactorización
        │
        ▼
Paginación + Búsqueda
        │
        ▼
PostgreSQL
        │
        ▼
SQLAlchemy ORM
        │
        ▼
API REST
        │
        ▼
pytest
```

La aplicación mantiene actualmente el código CLI original como componente legacy.


