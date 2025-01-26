// Obtener el modal y la imagen
var modal = document.getElementById("miModal");
var img = document.getElementById("profile");
var modalImg = document.getElementById("img01");
var closeBtn = document.querySelector(".btn-close");

// Abrir el modal al hacer clic en la imagen
img.onclick = function () {
  modal.style.display = "block";
  modalImg.src = this.src; // Usar la misma imagen
};

// Cerrar el modal al hacer clic en el botón de cerrar
closeBtn.onclick = function () {
  modal.style.display = "none";
};

// Cerrar el modal si el usuario hace clic fuera del contenido
window.onclick = function (event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
};
