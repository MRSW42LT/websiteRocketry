function adicionarIngrediente(){
    var ing = document.getElementById("ingredientes").value;
    var lista = document.getElementById("lista").innerHTML;

    lista = lista +"<li class=\"list-group-item\">" + ing + "</li>";

    document.getElementById("lista").innerHTML = lista;
}

function soma(){
    var campo1 = parseInt(document.getElementById("campo1").value);
    var campo2 = parseInt(document.getElementById("campo2").value);

    total = campo1 + campo2;
    document.getElementById('total').innerHTML = total;
    //soma = campo1 + "Resultado: " + campo2;
    //alert(soma);
}

function deleteNote(noteId){
    fetch('/delete-note', {
        method: 'POST',
        body: JSON.stringify({ noteId: noteId })
    }).then((_res) => {
        window.location.href = "/escola";
    } )
}

//Get the button
let mybutton = document.getElementById("btn-back-to-top");

// When the user scrolls down 20px from the top of the document, show the button
window.onscroll = function () {
  scrollFunction();
};

function scrollFunction() {
  if (
    document.body.scrollTop > 20 ||
    document.documentElement.scrollTop > 20
  ) {
    mybutton.style.display = "block";
  } else {
    mybutton.style.display = "none";
  }
}
// When the user clicks on the button, scroll to the top of the document
mybutton.addEventListener("click", backToTop);

function backToTop() {
  document.body.scrollTop = 0;
  document.documentElement.scrollTop = 0;
}