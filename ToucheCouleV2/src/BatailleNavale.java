import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Random;
import java.util.Scanner;

public class BatailleNavale {

	public static void affichage(Case[][] cases) {
		char[] lstAlpha = {'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'};
		
		for (int i=0; i < cases.length; i++) {
			System.out.print("\t|   " + lstAlpha[i]);
		}
		
		
		System.out.println("\t|");
		int numLigne = 1;
		
		for (int i = 0; i < cases[0].length; i++ ) {
			for (int j = 0; j < cases.length; j++) {
				System.out.print("--------");				
			}
			
			System.out.println("---------");
			System.out.print(numLigne);
			System.out.print("\t");
			numLigne +=1;
			for (int j = 0; j < cases[0].length; j++) {
				System.out.print("|   ");
				System.out.print(cases[j][i].toString() + "\t");
			}
			System.out.println("|");
		}

		for (int i = 0; i < cases.length; i++) {
			System.out.print("--------");				
		}
		System.out.println("---------");
	}
	
	public static void choix(Case[][] cases, int nbBateau, int nbMun) {
		List<String> colonne = Arrays.asList("A", "B", "C", "D", "E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z");
		Scanner reader = new Scanner(System.in);  // Reading from System.in
		System.out.print("Coordonées de la prochaine attaque : ");
		String str = reader.nextLine();
		nbMun -= 1;
		int posx = colonne.indexOf(str.split("")[0]);
		int posy = Integer.parseInt(str.substring(1))-1;
		if (cases[posx][posy].getDejaVise() == true) {
			choix(cases, nbBateau, nbMun);
		} else {
			if (cases[posx][posy].getContenue() != null) {
				cases[posx][posy].setDejaVise(true);
				nbBateau -= 1;
			}else {
				int tailleBat = cases[posx][posy].getContenue().getTaille();
				for (int i = 0; i <= tailleBat; i++) {
					if(cases[posx][posy].getDejaVise()) {
						int nbTouche = cases[posx][posy].getContenue().getNbTouche();
						cases[posx][posy].getContenue().setNbTouche(nbTouche++);
						
						if(nbTouche == tailleBat) {
							System.out.println("Coulé");
						}
					}
				}
				cases[posx][posy].setDejaVise(true);
			}
			affichage(cases);
			
			if (nbBateau > 0 && nbMun > 0) {
				choix(cases, nbBateau, nbMun);
			}else {
				reader.close();
				finJeu(nbBateau);
			}
		}
	}
	
	public static void finJeu(int nbBat) {
		if (nbBat == 0) {
			System.out.println("Félicitation, vous avez gagné.");
		} else {
			System.out.println("Mission échouée. Il reste " + nbBat + " bateaux à flôt.");
		}
	}
	
	public static void placeBateau(Case[][] grille) {
		Bateau[] tab = new Bateau[3];
		tab[0] = new Bateau("Bateau1", 3, 0);
		tab[1] = new Bateau("Bateau2", 1, 0);
		tab[2] = new Bateau("Bateau3", 5, 0);
		
		Random rand = new Random();

		/*
		for (int i = 0; i <= 10; i++) {
			for (int j = 0; j <= 10; j++) {
				tab[i].getTaille();
				if(grille[i][j].getContenue() == null) {
					
				}
			}
		}
		*/
		
		
		// Creation liste de taille de bateau
		
		Scanner reader = new Scanner(System.in); 
		System.out.print("Choisir le nombre de bateau : ");
		int nbBat = reader.nextInt();
		/**
		// ArrayList<Integer> tailleBat = new ArrayList<Integer>(nbBat);
		*/
		int[] tailleBat = new int[nbBat];
		// int[] tailleBateau = {1, 2, 3, 4, 5};
		
		for (int i = 0; i < nbBat; i++) {
			int taille = rand.nextInt(5);
			tailleBat[i] = taille;
			
		}		
		
		System.out.print("Choisir le nombre de munition : ");
		int nbMun = reader.nextInt();
		int posx, posy;
		boolean caseNull = true;
		int compt = nbBat;
		while (compt > 0) {
			posx = rand.nextInt(grille.length);
			posy = rand.nextInt(grille[0].length);
			if (grille[posx][posy].getContenue() == null) {
				int positionX = tab[0].getTaille() + posx;
				int positionY = tab[0].getTaille() + posy;
				
				int HorVerAl = rand.nextInt(1);
				
				
				if(tab[0].getTaille() == 1) {
					grille[posx][posy].setContenue(tab[0]);
				}
				else if (HorVerAl == 0){
					if(positionX < grille.length) {
						for(int i = 0; i != tab[0].getTaille(); i++) {
							if(grille[posx+i][posy].getContenue() != null)
								caseNull = false;
						}
						
						if(caseNull) {
							for(int i = 0; i != tab[0].getTaille(); i++) {
								if(grille[posx+i][posy].getContenue() == null) {
									grille[posx+i][posy].setContenue(tab[0]);
									System.out.print("Bateau placée");
								}

							}
						}
					}
				} else {
					if(positionY < grille.length) {
						for(int i = 0; i != tab[0].getTaille(); i++) {
							if(grille[posx+i][posy].getContenue() != null)
								caseNull = false;
						}
						
						if(caseNull) {
							for(int i = 0; i != tab[0].getTaille(); i++) {
								if(grille[posx][posy+i].getContenue() == null) {
									grille[posx][posy+i].setContenue(tab[0]);
									System.out.print("Bateau placée");
								}
							}
						}
					}
				}
				
				compt -= 1;
			}
		}
		affichage(grille);
		choix(grille, nbBat, nbMun);
	}
	
	public static void main(String[] args) {
		//Case cases = new Case(false, false);
	
		Case[][] grille = new Case[10][10];
		
		for (int i = 0; i < 10; i++) {
			for (int j = 0; j < 10; j++) {
				
				grille[i][j] = new Case(null, false);
			}
			
		}
		placeBateau(grille);
	}

}
