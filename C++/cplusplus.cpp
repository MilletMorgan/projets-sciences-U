#include <iostream>
using namespace std;

// fonction de base main()
int main(){
  // Déclaration des Variables. Elles peuvent être créer avant puis leurs attribuers une valeur plus tard. On peut leurs donné le nom qu'on veut mais il faut que ça soit cohérent.

  int varInt; // Variable Int : Uniquement des nombres sans virgule, positif et négatif.
  int variableInt = 10;

  float varFloat; //4 bit

  doube vardouble; // 8 bit

  double varDouble; // Variable Double : Nombre avec et sans virgule, positif et negatif.
  double variableDouble = 5.8;

  string varString; // Variable String : Des charactères alphanumérique, à mettre entre " ".
  string nomUtilisateur; // Variable que l'on demanderaà l'utilisateur d'insérer sa valeur;
  string variableString = "Hello World!";

  bool varBool; // Variable Bool : Vrai ou faux, true ou false
  bool variableBool = true;

  // Affichage

  // Afficher un message.
  cout << "Jean";

  // Afficher le contenue d'une variable.
  cout << variableString;

  // on peut cumuler les messages et variables.
  cout << "Bonjour " << variableString << ", aurevoir." << variableDouble;

  // Demander à l'utilisateur d'écrire, ce qu'il écrira sera déclarer dans une variable;
  cin >> nomUtilisateur; // Ne pas oublier de déclarer la variable au préalable !



  // Structure conditionnel (==, <, >, <=, >=, !=)

  if(variableInt == 10){ // Si variableInt est égal à 10 alors..
    // instruction à exécuter par exemple...
    cout << "variableInt est égal à 10";
  } else if (variableInt > 10 ){ // Sinon si
    cout << "variableInt est supperieur à 10";
  } else { // Sinon .. pas besoins d'écrire de condition
    cout << "variableInt est inférieur à 10"
  }


  // Boucle

  n = 0; // Déclare la variable n,

  while(n != 10) { // la boucle va afficher 0, 1, 2, 3... jusqu'à 10.
    cout << "n = " << n;
    n++;
  }


  // La même chose mais avec do while

  do {
    cout << "n = " << n;
    n++;
  } while (n != 10)


  // Avec la bouvle for

  for(n = 0; n != 10; n++){ // n est égal à 0, la boucle continue tant que n n'est pas égal à 10, fait n + 1 jusqu'a 10.
    cout << "n = " << n;
  }


  // Les tableaux

  int tableau[5]; // tableau de taille 5.
  int nombres[10] = { 2, 3, 5, 7, 11, 13, 17, 19, 23, 29 }; // tableau de taille 10 avec ses valeurs

  cout << nombres[2];

  for (int i = 0; i < 10; i++){  // Parcour du tableau pour l'afficher, i va de 0 à 9 inclus
    cout << nombres[i] << endl; // endl permet un saut à la ligne.
  }

  // Affiche :
  // nombres [ 0 ] = 2
  // nombres [ 1 ] = 3
  // nombres [ 2 ] = 5
  // nombres [ 3 ] = 7
  // nombres [ 4 ] = 11
  // nombres [ 5 ] = 13
  // nombres [ 6 ] = 17
  // nombres [ 7 ] = 19
  // nombres [ 8 ] = 23
  // nombres [ 9 ] = 29
}
