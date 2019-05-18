#include <iostream>
using namespace std;

int main() {
	int ageCli, anneePermis, nbrAccidents, nbrFidel;
	string tarif;
	bool assuree = false;

	cout << "Quel age à le client ? ";
	cin >> ageCli;
	cout << "Depuis combiens d'années le client est titulaire du permis de conduire ?";
	cin >> anneePermis;
	cout << "Combiens d'accidents le clients à t'il eu ?";
	cin >> nbrAccidents;
	cout << "Nombres d'années que le client est inscrit chez nous ?";
	cin >> nbrFidel;

  if ((ageCli < 25) && (anneePermis < 2) && (nbrAccidents == 0)){
    tarif = "rouge";
    assuree = true;
  } else if
  (
    (
      (
        (ageCli < 25) && (anneePermis > 2)
      )
      ||
      (
        (ageCli > 25) && (anneePermis < 2)
      )
    )
    && nbrAccidents == 0
  )

    {

    tarif = "orange";
    assuree = true;
  } else if (nbrAccidents == 1) {
    tarif = "rouge";
    assuree = true;
  } else if((ageCli > 25) && (anneePermis > 2) && (nbrAccidents == 0)){
    tarif = "vert";
    assuree = true;
  } else if ((ageCli > 25) && (anneePermis > 2) && (nbrAccidents == 1)) {
    tarif ="orange";
    assuree = true;
  } else if((ageCli > 25) && (anneePermis > 2) && (nbrAccidents == 2)) {
    tarif = "rouge";
    assuree = true;
  } else if (nbrFidel > 1) {
    tarif = "bleu";
    assuree = true;
  }

  if (assuree == true) {
  cout << "Le client assurée à " << ageCli << " ans. Il est titulaire du permis du permis de conduire depuis " << anneePermis << " ans. Le tarif de son assurance est de niveau " << tarif << ".";
  } else {
  cout << "L'assurance refuse le client qui à " << ageCli << " ans et est titulaire du permis du permis de conduire depuis " << anneePermis << " ans et qui à eu " << nbrAccidents << " accidents.";
  }
}
