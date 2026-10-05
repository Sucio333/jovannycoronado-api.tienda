# Tienda Online – API REST

API REST para una tienda online, construida con **Django** y **Django REST Framework**, con base de datos **MariaDB/MySQL** y una página de inicio en HTML y CSS que consume la API.

## Tecnologías

- Python 3
- Django 6.1
- Django REST Framework 3.18
- MariaDB / MySQL (conector PyMySQL)
- python-decouple (variables de entorno)
- HTML, CSS y JavaScript (página de inicio)

## Estructura del proyecto

```
API_BACKEND/
├── manage.py
├── requirements.txt
├── .env                  # variables de entorno (no se sube a Git)
├── scripts/
│   └── mariadb.sql       # script de la base de datos
├── tienda_online/        # configuración del proyecto
│   ├── settings.py
│   └── urls.py
└── tienda/               # aplicación principal
    ├── models.py
    ├── serializers.py
    ├── views.py
    ├── urls.py
    ├── templates/tienda/index.html
    └── static/tienda/css/style.css
```

## Modelos

| Modelo | Descripción |
|---|---|
| **Categoria** | Agrupa los productos (nombre único, descripción). |
| **Producto** | Pertenece a una categoría. Tiene precio, stock y estado activo. |
| **Cliente** | Nombre, apellido, email único, teléfono y dirección. |
| **Pedido** | Pertenece a un cliente. Estados: Pendiente, Pagado, Enviado, Entregado, Cancelado. |
| **DetallePedido** | Línea de un pedido: producto, cantidad y precio unitario (se copia desde el producto al crearlo). |

Todos incluyen `created_at` y `updated_at`, que se llenan automáticamente y son de solo lectura en la API.

## Instalación

### 1. Clonar el repositorio y entrar a la carpeta

```bash
git clone https://github.com/Sucio333/Back-end-Django
cd Back-end-Django
```

### 2. Crear y activar el entorno virtual

Windows (PowerShell):

```powershell
python -m venv venv
Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
.\venv\Scripts\Activate.ps1
```

Linux / macOS:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. Configurar la base de datos

Crea la base de datos y el usuario en MariaDB/MySQL. La forma más simple es ejecutar el script `scripts/mariadb.sql` como administrador (por ejemplo, desde la consola `mysql -u root -p`). Ese script crea la base `tienda_online_db` y el usuario `tienda_user` con la clave **`CambiaEstaClave_2026!`**; esa misma clave debe ir en `DB_PASSWORD` del archivo `.env` (paso 5).

Si prefieres hacerlo a mano, usa tu propia clave:

```sql
CREATE DATABASE tienda_online_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
CREATE USER 'tienda_user'@'localhost' IDENTIFIED BY 'TU_CLAVE_AQUI';
CREATE USER 'tienda_user'@'127.0.0.1' IDENTIFIED BY 'TU_CLAVE_AQUI';
GRANT ALL PRIVILEGES ON tienda_online_db.* TO 'tienda_user'@'localhost';
GRANT ALL PRIVILEGES ON tienda_online_db.* TO 'tienda_user'@'127.0.0.1';
FLUSH PRIVILEGES;
```

### 5. Crear el archivo `.env`

En la raíz del proyecto (junto a `manage.py`), copia el archivo de ejemplo y rellena `SECRET_KEY` y `DB_PASSWORD`:

```powershell
copy .env.example .env
```

Luego abre el `.env` y deja estos valores, usando los tuyos:

```env
SECRET_KEY='una-clave-secreta-larga-y-unica'
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost

DB_ENGINE=django.db.backends.mysql
DB_NAME=tienda_online_db
DB_USER=tienda_user
DB_PASSWORD=TU_CLAVE_AQUI
DB_HOST=127.0.0.1
DB_PORT=3306
```

Si creaste la base con `scripts/mariadb.sql`, `DB_PASSWORD` debe ser `CambiaEstaClave_2026!`.

> El archivo `.env` está en el `.gitignore`. No lo subas al repositorio ni lo compartas.

### 6. Aplicar migraciones

```bash
python manage.py migrate
```

### 7. Crear un superusuario (opcional, para el panel de administración)

```bash
python manage.py createsuperuser
```

### 8. Iniciar el servidor

```bash
python manage.py runserver
```

## Uso

| Dirección | Qué es |
|---|---|
| `http://127.0.0.1:8000/` | Página de inicio de la tienda |
| `http://127.0.0.1:8000/api/` | Raíz de la API (navegable) |
| `http://127.0.0.1:8000/admin/` | Panel de administración |

## Endpoints de la API

Todos los recursos soportan los métodos estándar de un `ModelViewSet`.

| Recurso | Ruta |
|---|---|
| Categorías | `/api/categorias/` |
| Productos | `/api/productos/` |
| Clientes | `/api/clientes/` |
| Pedidos | `/api/pedidos/` |
| Detalles de pedido | `/api/detalles-pedido/` |

| Método | Ruta | Acción |
|---|---|---|
| GET | `/api/<recurso>/` | Listar (con paginación) |
| POST | `/api/<recurso>/` | Crear |
| GET | `/api/<recurso>/<id>/` | Ver un registro |
| PUT / PATCH | `/api/<recurso>/<id>/` | Modificar |
| DELETE | `/api/<recurso>/<id>/` | Eliminar |

### Ejemplo: crear una categoría

```http
POST /api/categorias/
Content-Type: application/json

{
  "nombre": "Poleras",
  "descripcion": "Poleras vintage"
}
```

Respuesta `201 Created`:

```json
{
  "id": 1,
  "nombre": "Poleras",
  "descripcion": "Poleras vintage",
  "created_at": "2026-10-04T21:50:00Z",
  "updated_at": "2026-10-04T21:50:00Z"
}
```

### Orden recomendado para cargar datos

1. Categorías
2. Productos (requieren una categoría existente)
3. Clientes
4. Pedidos (requieren un cliente existente)
5. Detalles de pedido (requieren un pedido y un producto existentes)

## Validaciones y reglas

- El precio de un producto debe ser mayor que 0.
- La cantidad de un detalle de pedido debe ser al menos 1.
- `precio_unitario` no se envía: se copia desde el precio actual del producto al crear el detalle.
- Las categorías, clientes y productos con pedidos asociados no se pueden eliminar (`on_delete=PROTECT`).

## Autor

Jovanny Coronado Salas – INACAP Temuco.
