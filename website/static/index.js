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
        window.location.href = "/";
    } )
}