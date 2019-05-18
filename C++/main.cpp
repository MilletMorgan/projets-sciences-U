/**
 *	TD 1
 */

/**
 *	Exercice 1
 */
#include <iostream>
using namespace std;

int main() {
	int nb1;

    cout << "Nombre 1 :";
    cin >> nb1;
    cout << nb1*nb1;
}

/**
 * Exercice 2
 */
#include <iostream>
using namespace std;

int main() {
	double prixHT, TVA;
	int nbrArticles;

    cout << "Prix hors taxes (€): ";
    cin >> prixHT;
	cout << "TVA (%): ";
	cin >> TVA;
	cout << "Nombres d'articles : ";
	cin >> nbrArticles;
	cout << (prixHT * (1+(TVA/100))) * nbrArticles << "€";
}

/**
 * Exercice 3
 */
#include <iostream>
using namespace std;

int main() {
	string nom1, nom2, nom3;

	cout << "Nom 1 : ";
	cin >> nom1;
	cout << "Nom 2 : ";
	cin >> nom2;
	cout << "Nom 3 : ";
	cin >> nom3;

	if(nom1 < nom2 && nom2 < nom3) {
		cout << "Les noms sont dans l'ordre alphabetique.";
	} else {
		cout << " Les noms ne sont pas dans l'ordre alphabetique.";
	}
}

/**
 * Exercice 4
 */
#include <iostream>
using namespace std;

int main() {
	int nb1;

	cout << "Votre nombre : ";
	cin >> nb1;

	if(nb1 > 0){
		cout << "Votre nombre est positif.";
	} else if(nb1 < 0){
		cout << "Votre nombre est negatif.";
	} else{
		cout << "Votre nombre est nul.";
	}
}

/**
 * Exercice 5
 */
#include <iostream>
using namespace std;

int main() {

}

/**
 * Exercice 6
 */
#include <iostream>
using namespace std;

int main() {

}

/**
 * Exercice 7
 */
#include <iostream>
using namespace std;

int main() {

}

/**
 * Exercice 8
 */
#include <iostream>
using namespace std;

int main() {

}






/*
#include <iostream>
using namespace std;

int main() {
    //Les variables
    double nb1, nb2;
    char op;
    double resultat;

    cout << "Nombre 1 :";
    cin >> nb1;
    cout << "Nombre 2 :";
    cin >> nb2;
    cout << "Operation( s: somme, p: produit) : ";
    cin >> op;

    if(op == 's')
    	resultat = nb1 + nb2;
	else
    	resultat = nb1 * nb2;

    cout << "Résultat : " << resultat << endl;
}



/*
#include <iostream>

using namespace std;

int main(){
    //Commentaire sur une ligne.
	/*
	Commentaire
	sur
	plusieurs
	ligne.
	*/
/*
	int age;
	int anneeNaissance;

	cout << "Entrer votre année de naissance : " << endl;

	cin >> anneeNaissance;

	age = 2018 - anneeNaissance;

	cout << "Votre age en 2018 : " << age << "ans." << endl;
}
*/

#include <iostream>
using namespace std;

int main() {
	double nb;

	do {
		cout << "Entrez un nombre (0 pour quitter)";
		cin >> nb;
		cout << "Le carr� : " << nb*nb << endl;

	} while (nb != 0);
}


#include <iostream>
using namespace std;

int main() {
	int i;

	for(i=1; i<10; i++) {
		cout << "Bonjour";
	}
}


#include <iostream>
using namespace std;

int main() {
	cout << "Saisir 2 nombres : ";
	cin >> nb1 >> nb2;

	if((nb1 == 0) || (nb2 == 0)){
		cout << "Le produit est nul " << endl;
	} else if(nb1>0 && nb2<0){
		cout << "Le produit est n�gatif " << endl;
	} else{
		cout << "Le produit est positid" << endl;
	}
}
