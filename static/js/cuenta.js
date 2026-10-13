const mostrarLogin = document.getElementById("mostrarLogin");
const mostrarCrear = document.getElementById("mostrarCrear");

const crearCuenta = document.getElementById("crearCuenta");
const iniciarSesion = document.getElementById("iniciarSesion");


mostrarLogin.addEventListener("click", function(evento) {

    evento.preventDefault();

    crearCuenta.style.display = "none";
    iniciarSesion.style.display = "block";

});


mostrarCrear.addEventListener("click", function(evento) {

    evento.preventDefault();

    iniciarSesion.style.display = "none";
    crearCuenta.style.display = "block";

});