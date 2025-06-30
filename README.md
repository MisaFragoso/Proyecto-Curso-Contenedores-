# Proyecto Final Curso Contenedores

## Instrucciones de ejecucion

1. Desde una terminal, clona el repositorio

```
git clone https://github.com/MisaFragoso/Proyecto-Curso-Contenedores-.git
```

2. Accede a la carpeta `proyecto-final-estudiantes` desde tu editor de código de preferencia o terminal.

3. Ejecuta el comando: 
```
docker compose up --build
```
4. Una vez levantada la aplicacion, accede a los siguientes enlaces para comprobar el funcionamiento:

- `http://localhost` → **Catálogo público** (productos visibles)
- `http://localhost/admin` → **Panel administrativo** (gestión de inventario)  
- `http://localhost/api/productos` → **API REST** (JSON con productos)
