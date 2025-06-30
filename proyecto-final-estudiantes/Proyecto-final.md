# Proyecto Final: Sistema de Gestión de Inventario Empresarial
## DistribuTech Solutions

### 📖 Historia del Proyecto

**DistribuTech Solutions** es una empresa mediana de distribución de productos tecnológicos que maneja un catálogo de más de 1,000 productos (laptops, smartphones, tablets, etc.). La empresa ha crecido rápidamente y necesita modernizar su infraestructura tecnológica para:

- Permitir que **clientes externos** consulten el catálogo público de productos
- Proporcionar a **empleados internos** una herramienta para gestionar inventario
- Tener una **API centralizada** que maneje toda la lógica de negocio
- Mantener **datos consistentes** en una base de datos centralizada
- Usar un **reverse proxy** para enrutar eficientemente las peticiones

### 🏗️ Arquitectura del Sistema

```
Internet → nginx (Reverse Proxy) → {
                                   ├── Web Pública (Puerto 3001)
                                   ├── Web Administrativa (Puerto 3002)  
                                   └── API REST (Puerto 3003)
                                 }
                                   ↓
                              Base de Datos MySQL (Puerto 3306)
```

### 🎯 Componentes del Proyecto

#### 1. **Nginx - Reverse Proxy**
- **Puerto externo**: 80
- **Función**: Enrutar peticiones según la URL
  - `/` → Web Pública (catálogo de productos)
  - `/admin` → Web Administrativa (gestión de inventario)
  - `/api` → API REST

#### 2. **Web Pública - Catálogo de Productos**
- **Tecnología**: HTML/CSS/JavaScript vanilla
- **Puerto interno**: 3001
- **Usuarios**: Clientes externos
- **Funcionalidades**:
  - Ver catálogo de productos disponibles
  - Buscar productos por categoría
  - Ver detalles de productos (precio, stock disponible)

#### 3. **Web Administrativa - Gestión de Inventario**
- **Tecnología**: HTML/CSS/JavaScript vanilla
- **Puerto interno**: 3002
- **Usuarios**: Empleados de la empresa
- **Funcionalidades**:
  - Dashboard con estadísticas de inventario
  - Agregar nuevos productos
  - Actualizar stock y precios
  - Ver productos con stock bajo

#### 4. **API REST - Lógica de Negocio**
- **Tecnología**: Python Flask
- **Puerto interno**: 3003
- **Funcionalidades**:
  - `GET /api/productos` - Obtener lista de productos
  - `GET /api/productos/{id}` - Obtener producto específico
  - `POST /api/productos` - Crear nuevo producto
  - `PUT /api/productos/{id}` - Actualizar producto
  - `GET /api/estadisticas` - Obtener estadísticas de inventario

#### 5. **Base de Datos MySQL**
- **Puerto interno**: 3306
- **Esquema**:
  ```sql
  productos (
    id INT PRIMARY KEY,
    nombre VARCHAR(100),
    categoria VARCHAR(50),
    precio DECIMAL(10,2),
    stock INT,
    descripcion TEXT,
    fecha_actualizacion TIMESTAMP
  )
  ```

### 📁 Estructura del Proyecto (Código Fuente Proporcionado)

```
proyecto-final/
├── nginx/
│   └── nginx.conf                 # ✅ Configuración del reverse proxy
├── web-publica/
│   └── index.html                 # ✅ Aplicación web pública completa
├── web-admin/
│   └── index.html                 # ✅ Panel administrativo completo
├── api/
│   ├── app.py                     # ✅ API REST en Python Flask
│   └── requirements.txt           # ✅ Dependencias de Python
└── database/
    └── init.sql                   # ✅ Script de inicialización de BD
```

### 📦 **TU TAREA: Contenerizar las Aplicaciones**

El equipo de desarrollo de DistribuTech ya ha creado todas las aplicaciones, pero necesitas **contenerizar** cada componente para poder desplegarlo. Debes crear:

```
proyecto-final/
├── docker-compose.yml             # ❌ Por crear
├── nginx/
│   ├── Dockerfile                 # ❌ Por crear  
│   └── nginx.conf                 # ✅ Ya existe
├── web-publica/
│   ├── Dockerfile                 # ❌ Por crear
│   └── index.html                 # ✅ Ya existe
├── web-admin/
│   ├── Dockerfile                 # ❌ Por crear
│   └── index.html                 # ✅ Ya existe
├── api/
│   ├── Dockerfile                 # ❌ Por crear
│   ├── app.py                     # ✅ Ya existe
│   └── requirements.txt           # ✅ Ya existe
└── database/
    └── init.sql                   # ✅ Ya existe
```

### 🚀 Objetivos de Aprendizaje

1. **Docker**: Crear Dockerfiles para diferentes tipos de aplicaciones
2. **Docker Compose**: Orquestar múltiples contenedores
3. **Networking**: Comunicación entre contenedores
4. **Reverse Proxy**: Configuración de nginx
5. **Persistencia**: Manejo de volúmenes para base de datos
6. **Arquitectura de Microservicios**: Separación de responsabilidades

### 🔍 **Cómo Funcionan las Aplicaciones (Código Ya Desarrollado)**

#### 1. **API REST (Python Flask)** - `api/app.py`
```python
# La API ya está completamente desarrollada e incluye:
from flask import Flask, jsonify, request

# Endpoints disponibles:
# GET /api/productos - Lista todos los productos
# GET /api/productos/<id> - Obtiene un producto específico  
# POST /api/productos - Crea un nuevo producto
# PUT /api/productos/<id> - Actualiza un producto
# GET /api/estadisticas - Obtiene estadísticas del inventario

# La aplicación usa variables de entorno para conectarse a MySQL:
# DATABASE_HOST, DATABASE_USER, DATABASE_PASSWORD, DATABASE_NAME
```

**📋 Para contenerizar necesitas:**
- Una imagen base de Python
- Instalar las dependencias de `requirements.txt`
- Exponer el puerto 5000 (Flask default)
- Configurar las variables de entorno de la base de datos

#### 2. **Web Pública** - `web-publica/index.html`
```html
<!-- Aplicación web estática que consume la API -->
<!-- Funcionalidades ya implementadas: -->
<!-- - Catálogo de productos con filtros -->
<!-- - Búsqueda por categoría -->
<!-- - Interfaz responsive y moderna -->
<!-- - Consume endpoints: /api/productos -->
```

**📋 Para contenerizar necesitas:**
- Un servidor web (nginx, apache, etc.)
- Servir archivos estáticos
- Exponer puerto 80

#### 3. **Web Administrativa** - `web-admin/index.html`
```html
<!-- Panel administrativo completo que incluye: -->
<!-- - Dashboard con estadísticas -->
<!-- - Formularios para agregar/editar productos -->
<!-- - Tabla de productos con filtros -->
<!-- - Alertas de stock bajo -->
<!-- - Consume todos los endpoints de la API -->
```

**📋 Para contenerizar necesitas:**
- Un servidor web (nginx, apache, etc.)
- Servir archivos estáticos
- Exponer puerto 80

#### 4. **Nginx Reverse Proxy** - `nginx/nginx.conf`
```nginx
# Configuración ya definida para enrutar:
# / → web-publica:80
# /admin → web-admin:80  
# /api → api:5000
```

**📋 Para contenerizar necesitas:**
- Imagen base de nginx
- Copiar el archivo de configuración
- Exponer puerto 80

#### 5. **Base de Datos MySQL** - `database/init.sql`
```sql
-- Script de inicialización con:
-- - Creación de tabla 'productos'
-- - Datos de prueba (laptops, smartphones, tablets)
-- - Configuración de usuario 'distributec'
```

**📋 Para contenerizar necesitas:**
- Imagen oficial de MySQL
- Ejecutar el script de inicialización
- Configurar variables de entorno (usuario, contraseña)
- Exponer puerto 3306
- Configurar volumen para persistencia

### 📋 Tareas para los Estudiantes

#### Fase 1: Análisis del Código Fuente
- [ ] Revisar cada aplicación y entender su funcionamiento
- [ ] Identificar las dependencias y puertos de cada servicio
- [ ] Analizar la configuración de nginx y la estructura de la API

#### Fase 2: Creación de Dockerfiles
- [ ] **Dockerfile para la API** (`api/Dockerfile`)
  - Imagen base de Python
  - Instalación de dependencias
  - Configuración del puerto 5000
- [ ] **Dockerfile para Web Pública** (`web-publica/Dockerfile`)
  - Servidor web para archivos estáticos
  - Puerto 80
- [ ] **Dockerfile para Web Admin** (`web-admin/Dockerfile`)
  - Servidor web para archivos estáticos
  - Puerto 80
- [ ] **Dockerfile para Nginx** (`nginx/Dockerfile`)
  - Imagen base de nginx
  - Configuración personalizada

#### Fase 3: Configuración de Docker Compose
- [ ] Crear `docker-compose.yml` con todos los servicios
- [ ] Configurar redes entre contenedores
- [ ] Definir variables de entorno para la base de datos
- [ ] Configurar volúmenes para persistencia de datos
- [ ] Establecer dependencias entre servicios

#### Fase 4: Pruebas y Validación
- [ ] Levantar todos los servicios con `docker-compose up`
- [ ] Verificar que nginx enrute correctamente las peticiones
- [ ] Probar la funcionalidad de la web pública (catálogo)
- [ ] Probar la funcionalidad del panel admin (CRUD de productos)
- [ ] Verificar la persistencia de datos en MySQL

### 💡 **Pistas y Consejos Técnicos**

#### Para la API (Python Flask):
```dockerfile
# Usa una imagen base como python:3.9-slim
# No olvides copiar requirements.txt primero
# pip install -r requirements.txt
# El comando para ejecutar: python app.py
```

#### Para las aplicaciones web estáticas:
```dockerfile
# Puedes usar nginx:alpine
# Copia los archivos HTML al directorio /usr/share/nginx/html/
# Nginx automáticamente sirve archivos estáticos
```

#### Para el docker-compose.yml:
```yaml
# Define una red personalizada
# Usa nombres de servicios para la comunicación interna
# MySQL necesita variables: MYSQL_ROOT_PASSWORD, MYSQL_DATABASE, etc.
# No olvides el volumen para persistir los datos de MySQL
```

#### Variables de entorno importantes:
- **API**: `DATABASE_HOST=database`, `DATABASE_USER=distributec`
- **MySQL**: `MYSQL_ROOT_PASSWORD`, `MYSQL_DATABASE=inventario`
- **Puertos**: nginx(80), api(5000), mysql(3306)

### 🎓 Criterios de Evaluación

| Criterio | Puntos | Descripción |
|----------|--------|-------------|
| Dockerfiles | 30% | Dockerfiles correctos para cada servicio |
| Docker Compose | 25% | Configuración completa y funcional |
| Networking | 15% | Comunicación correcta entre contenedores |
| Reverse Proxy | 15% | Nginx enrutando correctamente |
| Persistencia | 10% | Volúmenes de base de datos funcionando |
| Documentación | 5% | README con instrucciones de ejecución |

### ✅ **Validación del Proyecto**

Tu proyecto estará completo cuando puedas ejecutar:

```bash
docker-compose up -d
```

Y todas estas URLs funcionen correctamente:
- `http://localhost` → **Catálogo público** (productos visibles)
- `http://localhost/admin` → **Panel administrativo** (gestión de inventario)  
- `http://localhost/api/productos` → **API REST** (JSON con productos)

### 🎯 **Funcionalidades que Deben Funcionar**

#### Web Pública (`http://localhost`):
- ✅ Ver catálogo completo de productos
- ✅ Filtrar por categorías (Laptops, Smartphones, Tablets, Accesorios)
- ✅ Buscar productos por nombre
- ✅ Ver precios y stock disponible

#### Web Administrativa (`http://localhost/admin`):
- ✅ Dashboard con estadísticas (total productos, valor inventario)
- ✅ Agregar nuevos productos al catálogo
- ✅ Editar productos existentes (precio, stock)
- ✅ Ver alertas de productos con stock bajo

#### API REST (`http://localhost/api`):
- ✅ `GET /api/productos` - Lista de productos
- ✅ `GET /api/productos/{id}` - Producto específico
- ✅ `POST /api/productos` - Crear producto
- ✅ `PUT /api/productos/{id}` - Actualizar producto
- ✅ `GET /api/estadisticas` - Estadísticas del inventario




