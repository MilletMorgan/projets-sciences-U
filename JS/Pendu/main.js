var motATrouver = 'bonjour';
var lettreSaisies = [];
var nombreCoups = 0;
var a = 0;

genererBouttonsPourAffichage();

function genererBouttonsPourAffichage(){
    var nombreDeLettre = motATrouver.length;

    var espaceJeu = document.getElementById("espaceJeu");

    for (var i = 0; i < nombreDeLettre; i++){
        espaceJeu.innerHTML += '<button type="button" id="' + i + '" class="btn btn-light custom-btn"></button>';
    }
}

function jouer(){
    var lettreSaisies = document.getElementById("lettre").value;
    var nombreDeCoup = document.getElementById("lettreSaisies").value;

    a++;

    for (var i = 0; i < motATrouver.length; i++) {
        if (motATrouver[i] == lettreSaisies) {
            document.getElementById(i).innerText = lettreSaisies;
        }
    }

    document.getElementById("lettreSaisies").innerText += " " + lettreSaisies + ", ";
    document.getElementById("nombreCoup").innerText = "Nombres de coups : " + a;
    document.getElementById("lettre").value = "";
}
