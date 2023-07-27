var eliminar = document.getElementById("eliminar-btn");
eliminar.addEventListener("click", function(event){
    event.preventDefault();
    let confirmar = confirm("Estas Seguro?");
    if (confirmar) {
        window.location.href = rutaEnlace;
    }
})