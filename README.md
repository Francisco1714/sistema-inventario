# 📦 Sistema de Inventario

Sistema de inventario desarrollado como proyecto práctico para evolucionar progresivamente desde una aplicación CLI hacia una aplicación web.

El proyecto se está construyendo priorizando:

* Aprendizaje práctico.
* Evolución progresiva de la arquitectura.
* Problemas y funcionalidades aplicables a sistemas reales.
* Uso de Git y GitHub durante todo el desarrollo.
* Refactorización solo cuando existe una necesidad concreta.
* Evitar sobreingeniería durante las primeras etapas.

---

## 🏗️ Estado actual

Actualmente el proyecto se encuentra en su **primera versión funcional como aplicación CLI**.

### Tecnologías

* Python
* SQLite
* Git
* GitHub

---

## 📂 Estructura actual

```text
sistema-inventario/
│
├── cli/
│   ├── __init__.py
│   └── menu.py
│
├── database/
│   ├── conexion.py
│   └── tablas.py
│
├── productos/
│   └── crud/
│       ├── __init__.py
│       ├── crear.py
│       ├── listar.py
│       ├── modificar.py
│       └── eliminar.py
│
├── main.py
├── inventario.db
└── .gitignore
```

---

## 🧩 Arquitectura actual

La aplicación está separada por responsabilidades.

```text
main.py
   │
   ▼
cli/menu.py
   │
   ▼
productos/crud/
   │
   ▼
database/
   │
   ▼
SQLite
```

### `main.py`

Funciona como **punto de entrada y orquestador**.

No contiene la lógica del menú ni las operaciones CRUD.

Su responsabilidad es iniciar los componentes principales de la aplicación.

### `cli/`

Contiene la interfaz de línea de comandos.

`menu.py` contiene el menú principal y decide qué operación ejecutar según la opción seleccionada.

### `productos/crud/`

Contiene las operaciones relacionadas con productos:

* Crear
* Listar
* Modificar
* Eliminar

El archivo `__init__.py` funciona como punto de acceso al CRUD y permite importar las operaciones desde:

```python
from productos.crud import agregar_producto
```

en lugar de importar cada módulo individualmente.

### `database/`

Contiene la conexión y estructura de la base de datos.

* `conexion.py` → conexión con SQLite.
* `tablas.py` → creación de tablas.

---

## 🗃️ Modelo actual

La aplicación utiliza una tabla `productos`.

```text
productos
├── id
├── nombre
├── descripcion
├── precio
└── stock
```

### Reglas actuales

#### Nombre

* No puede estar vacío.
* Se permiten nombres como:

  * `PC i7`
  * `K129Q`
  * `Laptop ThinkPad E14`

No se agregan restricciones artificiales sobre el contenido.

#### Descripción

* No puede estar vacía.
* Puede contener texto descriptivo, modelos, códigos, etc.

#### Precio

* Debe ser un número válido.
* Debe ser mayor que `0`.
* Se trabaja en USD.

#### Stock

* Debe ser un número entero.
* Puede ser `0`.
* No puede ser negativo.

El stock `0` representa un producto que sigue registrado pero que actualmente no tiene unidades disponibles.

#### ID

En modificar y eliminar se comprueba que corresponda a un producto existente.

---

## 🔧 Funcionalidades actuales

* [x] Crear conexión SQLite.
* [x] Crear tabla de productos.
* [x] Agregar productos.
* [x] Listar productos.
* [x] Modificar productos.
* [x] Eliminar productos.
* [x] Confirmación antes de eliminar.
* [x] Validaciones básicas.
* [x] Interfaz CLI.
* [x] Modularización del CRUD.
* [x] Separación de la CLI respecto de `main.py`.
* [x] `main.py` como orquestador.

---

## 🌱 Flujo Git

Cada bloque importante de trabajo se desarrolla mediante una rama independiente.

```text
main
 │
 ├── crear rama
 │
 ├── desarrollar
 │
 ├── probar
 │
 ├── commit
 │
 ├── merge → main
 │
 ├── probar nuevamente
 │
 ├── push
 │
 └── eliminar rama
```

`main` representa siempre la versión estable del proyecto.

---

# 🚀 Próxima evolución

La siguiente etapa será una desviación intencional del roadmap CLI.

En lugar de continuar agregando funcionalidades menores al prototipo, el mismo Sistema de Inventario será **escalado hacia una aplicación web**.

La idea es reutilizar el conocimiento y dominio construido hasta ahora y evolucionarlo progresivamente.

## Objetivo

Pasar de:

```text
Python
   +
CLI
   +
SQLite
```

a:

```text
Python
   +
Web
   +
Framework web
   +
Base de datos relacional
```

### Framework

La primera opción considerada es:

**Flask**

La razón es utilizar el proyecto existente para aprender directamente conceptos web fundamentales:

```text
Navegador
    ↓
HTTP Request
    ↓
Flask
    ↓
Ruta
    ↓
Lógica de aplicación
    ↓
Base de datos
    ↓
Respuesta
    ↓
HTML
```

Django podrá incorporarse posteriormente como comparación/evolución, pero no es necesario introducir ambos frameworks simultáneamente.

### Base de datos

Se reemplazará SQLite por:

**PostgreSQL**

Esto permitirá comenzar a trabajar con una base de datos más adecuada para una aplicación web y posteriormente introducir conceptos como:

* conexiones externas;
* configuración mediante variables de entorno;
* ORM;
* migraciones;
* relaciones;
* PostgreSQL en desarrollo y producción.

---

# 🧭 Próxima etapa de desarrollo

La evolución propuesta es:

```text
VERSIÓN 1
CLI + SQLite
     │
     ▼
VERSIÓN 2
Flask + PostgreSQL
     │
     ▼
Templates HTML
     │
     ▼
CRUD Web
     │
     ▼
SQLAlchemy
     │
     ▼
Migraciones
     │
     ▼
Validaciones web
     │
     ▼
Autenticación
     │
     ▼
API REST
     │
     ▼
Tests
     │
     ▼
Docker
     │
     ▼
Despliegue
```

Los componentes se introducirán **cuando exista una necesidad real dentro del proyecto**, evitando agregar tecnologías solamente por agregarlas.

---

## 🎯 Principio del proyecto

Este proyecto no busca simplemente construir un CRUD.

Busca demostrar una evolución progresiva:

```text
prototipo
   ↓
refactorización
   ↓
aplicación web
   ↓
persistencia profesional
   ↓
API
   ↓
testing
   ↓
contenedorización
   ↓
despliegue
```

La aplicación de inventario será utilizada como **proyecto base para aprender y demostrar el proceso completo de desarrollo de software**.
