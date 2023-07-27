var link = document.getElementById("link");
link.addEventListener("click", function(event) {
    event.preventDefault();
    var button = document.createElement("button");
    button.innerHTML = "Cargando...";
    link.style.display = "none";
    button.disabled = true;
    link.parentNode.replaceChild(button, link);
    setTimeout(function(){
    window.location = link.href;
    },2000);
});


