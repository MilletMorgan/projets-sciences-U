function recupererBalise() {
    var champSaisi = document.getElementById('champDeSaisi');
    alert(champSaisi.value);
}

function testerNombre(){
    var nombre = document.getElementById('nombre').value;

    if (nombre > 0) {
      console.log("nombre positif")
    } else if (nombre < 0) {
      console.log("Nombre négatif");
    } else {
      console.log("Nombre nul")
    }
}

function testerBoucle(){
    var debut = document.getElementById('debut').value;
    var fin = document.getElementById('fin').value;

    for(i = debut; i!=fin; i++) {
      console.log(i);
    }
}

var fruits = ['pomme', 'poire', 'bannane'];

fruits.push('orange');

for (var i = 0; i < fruits.length;i++){
  console.log(fruits[i]);
}

function ajouterFruit(){
  console.log('----------------');
  var fruitAAjouter = document.getElementById("fruits");

  document.getElementById("ajouterFruit").innerHTML += fruitAAjouter;
}
