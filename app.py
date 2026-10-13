

from flask import Flask, render_template, request, redirect, session
import sqlite3

app = Flask(__name__)
app.secret_key = "1114-musica-clave"


def conectar_db():
    conexion = sqlite3.connect("database/musica.db")
    conexion.row_factory = sqlite3.Row
    return conexion


def crear_base_datos():
    conexion = conectar_db()

    conexion.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            correo TEXT NOT NULL UNIQUE,
            usuario TEXT NOT NULL UNIQUE,
            contrasena TEXT NOT NULL
        )
    """)

    conexion.execute("""
        CREATE TABLE IF NOT EXISTS generos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL UNIQUE
        )
    """)

    conexion.execute("""
        CREATE TABLE IF NOT EXISTS usuario_genero (
            usuario_id INTEGER,
            genero_id INTEGER,
            PRIMARY KEY (usuario_id, genero_id),
            FOREIGN KEY (usuario_id) REFERENCES usuarios(id),
            FOREIGN KEY (genero_id) REFERENCES generos(id)
        )
    """)

    conexion.execute("""
        CREATE TABLE IF NOT EXISTS artistas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL UNIQUE
        )
    """)

    conexion.execute("""
        CREATE TABLE IF NOT EXISTS usuario_artista (
            usuario_id INTEGER,
            artista_id INTEGER,
            PRIMARY KEY (usuario_id, artista_id),
            FOREIGN KEY (usuario_id) REFERENCES usuarios(id),
            FOREIGN KEY (artista_id) REFERENCES artistas(id)
        )
    """)

    generos = [
        "Reguetón", "Trap", "Hip Hop", "Rap", "Pop", "Rock",
        "Electrónica", "Salsa", "Bachata", "Vallenato", "R&B",
        "Corridos", "Jazz", "Música clásica"
    ]

    for genero in generos:
        conexion.execute(
            "INSERT OR IGNORE INTO generos (nombre) VALUES (?)",
            (genero,)
        )

    conexion.commit()
    conexion.close()


@app.route("/")
def inicio():
    return render_template("cuenta.html")


@app.route("/cuenta", methods=["POST"])
def registro():
    nombre = request.form.get("nombre", "").strip()
    correo = request.form.get("correo", "").strip()
    usuario = request.form.get("usuario", "").strip()
    contrasena = request.form.get("contrasena", "")

    if not nombre or not correo or not usuario or not contrasena:
        return """
        <script>
            alert("Completa todos los campos.");
            window.location.href = "/";
        </script>
        """

    conexion = conectar_db()

    try:
        cursor = conexion.execute("""
            INSERT INTO usuarios (nombre, correo, usuario, contrasena)
            VALUES (?, ?, ?, ?)
        """, (nombre, correo, usuario, contrasena))

        conexion.commit()
        usuario_id = cursor.lastrowid

        session.clear()
        session["usuario_id"] = usuario_id
        session["nombre"] = nombre

    except sqlite3.IntegrityError:
        conexion.close()
        return """
        <script>
            alert("El correo o nombre de usuario ya existe.");
            window.location.href = "/";
        </script>
        """

    conexion.close()
    return redirect("/generos")


@app.route("/login", methods=["POST"])
def login():
    correo = request.form.get("correo", "").strip()
    contrasena = request.form.get("contrasena", "")

    conexion = conectar_db()

    usuario = conexion.execute("""
        SELECT id, nombre
        FROM usuarios
        WHERE correo = ? AND contrasena = ?
    """, (correo, contrasena)).fetchone()

    conexion.close()

    if usuario:
        session.clear()
        session["usuario_id"] = usuario["id"]
        session["nombre"] = usuario["nombre"]

        return redirect("/inicio")

    return """
    <script>
        alert("El correo o la contraseña son incorrectos.");
        window.location.href = "/";
    </script>
    """


@app.route("/generos", methods=["GET", "POST"])
def generos():
    if "usuario_id" not in session:
        return redirect("/")

    conexion = conectar_db()

    if request.method == "POST":
        generos_seleccionados = request.form.getlist("generos")
        usuario_id = session["usuario_id"]

        conexion.execute(
            "DELETE FROM usuario_genero WHERE usuario_id = ?",
            (usuario_id,)
        )

        for genero in generos_seleccionados:
            resultado = conexion.execute(
                "SELECT id FROM generos WHERE nombre = ?",
                (genero,)
            ).fetchone()

            if resultado:
                conexion.execute("""
                    INSERT OR IGNORE INTO usuario_genero
                    (usuario_id, genero_id)
                    VALUES (?, ?)
                """, (usuario_id, resultado["id"]))

        conexion.commit()
        conexion.close()

        session["generos"] = generos_seleccionados

        return redirect("/artistas")

    lista_generos = conexion.execute("""
        SELECT nombre
        FROM generos
        ORDER BY nombre
    """).fetchall()

    conexion.close()

    nombres_generos = [genero["nombre"] for genero in lista_generos]

    return render_template(
        "generos.html",
        generos=nombres_generos
    )


@app.route("/artistas", methods=["GET", "POST"])
def artistas():
    if "usuario_id" not in session:
        return redirect("/")

    conexion = conectar_db()
    usuario_id = session["usuario_id"]

    if request.method == "POST":
        artistas_seleccionados = request.form.getlist("artistas")

        for nombre_artista in artistas_seleccionados:
            nombre_artista = nombre_artista.strip()

            if nombre_artista:
                conexion.execute(
                    "INSERT OR IGNORE INTO artistas (nombre) VALUES (?)",
                    (nombre_artista,)
                )

                resultado = conexion.execute(
                    "SELECT id FROM artistas WHERE nombre = ?",
                    (nombre_artista,)
                ).fetchone()

                if resultado:
                    conexion.execute("""
                        INSERT OR IGNORE INTO usuario_artista
                        (usuario_id, artista_id)
                        VALUES (?, ?)
                    """, (usuario_id, resultado["id"]))

        conexion.commit()
        conexion.close()

        return redirect("/inicio")

    generos_seleccionados = conexion.execute("""
        SELECT g.nombre
        FROM generos g
        INNER JOIN usuario_genero ug ON g.id = ug.genero_id
        WHERE ug.usuario_id = ?
        ORDER BY g.nombre
    """, (usuario_id,)).fetchall()

    conexion.close()

    nombres_generos = [fila["nombre"] for fila in generos_seleccionados]

    return render_template(
        "artistas.html",
        generos=nombres_generos
    )


@app.route("/inicio")
def pagina_inicio():
    if "usuario_id" not in session:
        return redirect("/")

    conexion = conectar_db()
    usuario_id = session["usuario_id"]

    resultados_generos = conexion.execute("""
        SELECT g.nombre
        FROM generos g
        INNER JOIN usuario_genero ug ON g.id = ug.genero_id
        WHERE ug.usuario_id = ?
        ORDER BY g.nombre
    """, (usuario_id,)).fetchall()

    resultados_artistas = conexion.execute("""
        SELECT a.nombre
        FROM artistas a
        INNER JOIN usuario_artista ua ON a.id = ua.artista_id
        WHERE ua.usuario_id = ?
        ORDER BY a.nombre
    """, (usuario_id,)).fetchall()

    conexion.close()

    generos_usuario = [fila["nombre"] for fila in resultados_generos]
    artistas_usuario = [fila["nombre"] for fila in resultados_artistas]

    return render_template(
        "inicio.html",
        nombre=session.get("nombre", "Usuario"),
        generos=generos_usuario,
        artistas=artistas_usuario
    )


@app.route("/cerrar-sesion")
def cerrar_sesion():
    session.clear()
    return redirect("/")


if __name__ == "__main__":
    crear_base_datos()
    app.run(debug=True)
