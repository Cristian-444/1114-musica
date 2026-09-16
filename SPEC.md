# SPEC - 1114 Música

## 1. Información del proyecto

**Nombre:** 1114 Música

**Tipo:** Aplicación web de biblioteca musical

**Versión:** 1.0

**Estado:** En desarrollo

**Objetivo:** Crear una plataforma web para consultar, organizar y reproducir música mediante un sistema conectado a un servidor y una base de datos.

---

## 2. Arquitectura del sistema

La aplicación estará dividida en tres partes principales:

~~~text
USUARIO
   ↓
FRONTEND
HTML + CSS + JavaScript
   ↓
BACKEND
Node.js + Express.js
   ↓
API REST
   ↓
BASE DE DATOS
MySQL
~~~

---

## 3. Tecnologías

El proyecto utilizará:

- HTML5
- CSS3
- JavaScript
- Node.js
- Express.js
- MySQL
- Git
- GitHub

---

## 4. Frontend

El frontend será la parte visual de la aplicación.

Se desarrollará utilizando:

- HTML para la estructura.
- CSS para los estilos.
- JavaScript para la interacción.

El frontend permitirá al usuario interactuar con las diferentes funciones de la biblioteca musical.

---

## 5. Backend

El backend será desarrollado con Node.js y Express.js.

Sus funciones principales serán:

- Recibir solicitudes del frontend.
- Procesar información.
- Conectarse con MySQL.
- Consultar información.
- Registrar información.
- Actualizar información.
- Eliminar información.
- Controlar la autenticación.
- Proporcionar una API REST.

---

## 6. Base de datos

La base de datos será desarrollada utilizando MySQL.

La base de datos almacenará información relacionada con:

- Usuarios.
- Canciones.
- Artistas.
- Álbumes.
- Géneros.
- Playlists.
- Favoritos.
- Historial de reproducción.

---

## 7. Usuarios

El sistema tendrá dos tipos principales de usuarios.

### Usuario normal

Podrá:

- Registrarse.
- Iniciar sesión.
- Cerrar sesión.
- Buscar canciones.
- Buscar artistas.
- Buscar álbumes.
- Reproducir canciones.
- Crear playlists.
- Guardar canciones favoritas.
- Consultar su historial.

### Administrador

Podrá:

- Gestionar usuarios.
- Gestionar canciones.
- Gestionar artistas.
- Gestionar álbumes.
- Gestionar géneros.

---

## 8. Registro de usuarios

El sistema permitirá crear una cuenta mediante un formulario.

Los datos principales serán:

- Nombre de usuario.
- Correo electrónico.
- Contraseña.

El sistema deberá comprobar que los datos sean válidos antes de registrar al usuario.

---

## 9. Inicio de sesión

Los usuarios podrán ingresar al sistema utilizando:

- Correo electrónico.
- Contraseña.

El sistema verificará los datos y permitirá el acceso si son correctos.

---

## 10. Canciones

Cada canción tendrá información como:

- ID.
- Nombre.
- Artista.
- Álbum.
- Género.
- Duración.
- Imagen.
- Archivo o recurso de reproducción.

Las canciones podrán ser consultadas desde el sistema.

---

## 11. Artistas

Cada artista tendrá:

- ID.
- Nombre.
- Imagen.
- Descripción.

También se podrán consultar las canciones y álbumes relacionados con cada artista.

---

## 12. Álbumes

Cada álbum tendrá:

- ID.
- Nombre.
- Artista.
- Imagen.
- Año de lanzamiento.

Cada álbum podrá contener varias canciones.

---

## 13. Géneros musicales

El sistema permitirá clasificar las canciones por género.

Algunos ejemplos son:

- Reguetón.
- Rap.
- Trap.
- Rock.
- Pop.
- Electrónica.
- Salsa.
- Vallenato.

---

## 14. Playlists

Los usuarios podrán crear sus propias playlists.

Las funciones serán:

- Crear playlist.
- Cambiar nombre.
- Agregar canciones.
- Eliminar canciones.
- Eliminar playlist.

Cada playlist pertenecerá a un usuario.

---

## 15. Favoritos

El sistema permitirá guardar canciones como favoritas.

El usuario podrá:

- Agregar una canción a favoritos.
- Eliminar una canción de favoritos.
- Consultar sus canciones favoritas.

---

## 16. Historial

El sistema registrará las canciones reproducidas por cada usuario.

El historial permitirá consultar:

- Canción reproducida.
- Fecha de reproducción.
- Usuario.

---

## 17. Buscador

La aplicación contará con una barra de búsqueda.

El usuario podrá buscar:

- Canciones.
- Artistas.
- Álbumes.
- Géneros.

Los resultados se mostrarán de acuerdo con la búsqueda realizada.

---

## 18. Reproductor musical

La aplicación contará con un reproductor.

El reproductor permitirá:

- Reproducir.
- Pausar.
- Cambiar de canción.
- Canción anterior.
- Canción siguiente.
- Controlar el volumen.
- Mostrar progreso.
- Mostrar duración.

---

## 19. Página principal

La página principal tendrá una interfaz moderna y organizada.

Contará con:

- Menú lateral.
- Logo.
- Barra de búsqueda.
- Perfil del usuario.
- Playlists recientes.
- Artistas populares.
- Canciones recientes.
- Reproductor musical.

---

## 20. Diseño visual

El diseño utilizará un tema oscuro.

Colores principales:

- Negro.
- Gris oscuro.
- Morado.
- Violeta.

La interfaz tendrá:

- Tarjetas.
- Bordes redondeados.
- Botones.
- Imágenes de artistas.
- Imágenes de álbumes.
- Animaciones sencillas.
- Efectos al pasar el mouse.

---

## 21. Diseño responsive

La aplicación deberá adaptarse a diferentes tamaños de pantalla.

Deberá funcionar correctamente en:

- Computadores.
- Portátiles.
- Tablets.
- Celulares.

Los elementos de la página deberán reorganizarse dependiendo del tamaño de pantalla.

---

## 22. API REST

El backend proporcionará una API REST para comunicar el frontend con la base de datos.

### Usuarios

~~~text
GET /api/usuarios
POST /api/usuarios
POST /api/login
~~~

### Canciones

~~~text
GET /api/canciones
POST /api/canciones
PUT /api/canciones/:id
DELETE /api/canciones/:id
~~~

### Artistas

~~~text
GET /api/artistas
POST /api/artistas
PUT /api/artistas/:id
DELETE /api/artistas/:id
~~~

### Álbumes

~~~text
GET /api/albumes
POST /api/albumes
PUT /api/albumes/:id
DELETE /api/albumes/:id
~~~

### Playlists

~~~text
GET /api/playlists
POST /api/playlists
PUT /api/playlists/:id
DELETE /api/playlists/:id
~~~

---

## 23. Estructura de carpetas

La estructura principal del proyecto será:

~~~text
1114-musica/
│
├── public/
│   ├── css/
│   ├── js/
│   ├── img/
│   └── audio/
│
├── servidor/
│   ├── server.js
│   ├── conexion.js
│   └── rutas/
│
├── database/
│   └── biblioteca.sql
│
├── README.md
├── PRD.md
└── SPEC.md
~~~

---

## 24. Seguridad

El sistema deberá proteger la información de los usuarios.

Se deberán tener en cuenta:

- Validación de datos.
- Contraseñas protegidas.
- Control de acceso.
- Validación de solicitudes.
- Protección de las rutas administrativas.

Las credenciales de conexión y claves privadas no deberán guardarse directamente en el código ni subirse al repositorio.

---

## 25. Validaciones

El sistema deberá validar los datos ingresados por los usuarios.

Por ejemplo:

- El correo debe tener un formato válido.
- Los campos obligatorios no deben estar vacíos.
- Las contraseñas deben coincidir durante el registro.
- Los identificadores deben existir antes de modificar o eliminar información.

---

## 26. Administración

El administrador tendrá acceso a funciones para gestionar el contenido.

Podrá administrar:

- Usuarios.
- Canciones.
- Artistas.
- Álbumes.
- Géneros.

Las opciones principales serán:

- Crear.
- Consultar.
- Editar.
- Eliminar.

---

## 27. Requisitos funcionales

El sistema deberá:

1. Registrar usuarios.
2. Permitir iniciar sesión.
3. Permitir cerrar sesión.
4. Buscar canciones.
5. Buscar artistas.
6. Buscar álbumes.
7. Mostrar información musical.
8. Reproducir canciones.
9. Crear playlists.
10. Editar playlists.
11. Eliminar playlists.
12. Agregar canciones a playlists.
13. Eliminar canciones de playlists.
14. Guardar canciones favoritas.
15. Eliminar favoritos.
16. Registrar historial.
17. Administrar contenido.
18. Conectarse con MySQL.

---

## 28. Requisitos no funcionales

El sistema deberá cumplir con:

- Buena velocidad de respuesta.
- Diseño organizado.
- Interfaz fácil de utilizar.
- Compatibilidad con diferentes dispositivos.
- Código organizado.
- Base de datos estructurada.
- Comunicación mediante API REST.
- Seguridad básica de los datos.
- Mantenimiento sencillo.

---

## 29. Resultado esperado

Al finalizar el proyecto se espera obtener una aplicación web de biblioteca musical funcional.

La aplicación deberá permitir a los usuarios:

- Crear una cuenta.
- Iniciar sesión.
- Buscar música.
- Consultar artistas.
- Consultar álbumes.
- Reproducir canciones.
- Crear playlists.
- Guardar favoritos.
- Consultar su historial.

El sistema estará conectado a un servidor Node.js, una API REST y una base de datos MySQL.

---

## 30. Estado del proyecto

Actualmente el proyecto se encuentra en etapa de desarrollo.

Documentos iniciales:

- README.md
- PRD.md
- SPEC.md

Las siguientes etapas serán:

1. Configuración del proyecto.
2. Instalación de dependencias.
3. Creación del servidor.
4. Creación de la base de datos.
5. Desarrollo del backend.
6. Desarrollo del frontend.
7. Conexión entre frontend y backend.
8. Pruebas.
9. Corrección de errores.
10. Publicación del proyecto.