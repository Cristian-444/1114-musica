const botonBuscar = document.getElementById("boton-buscar");
const busqueda = document.getElementById("busqueda");

botonBuscar.addEventListener("click", function () {

    const texto = busqueda.value.trim();

    if (texto === "") {
        alert("Escribe algo para buscar.");
    } else {
        alert("Buscando: " + texto);
    }

});


const botonesReproducir = document.querySelectorAll(".boton-reproducir");

const nombreCancion = document.getElementById("nombre-cancion");
const nombreArtista = document.getElementById("nombre-artista");
const botonPrincipal = document.getElementById("reproducir");

let reproduciendo = false;


botonesReproducir.forEach(function (boton) {

    boton.addEventListener("click", function () {

        const tarjeta = boton.parentElement;

        const titulo = tarjeta.querySelector("h3").textContent;
        const artista = tarjeta.querySelector("p").textContent;

        nombreCancion.textContent = titulo;
        nombreArtista.textContent = artista;

        reproduciendo = true;
        botonPrincipal.textContent = "⏸";

    });

});


botonPrincipal.addEventListener("click", function () {

    if (reproduciendo) {

        reproduciendo = false;
        botonPrincipal.textContent = "▶";

    } else {

        reproduciendo = true;
        botonPrincipal.textContent = "⏸";

    }

});


const volumen = document.getElementById("control-volumen");

volumen.addEventListener("input", function () {

    console.log("Volumen: " + volumen.value);

});