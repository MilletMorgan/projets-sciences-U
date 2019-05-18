import java.util.*;
import java.io.*;

public class BatailleNavale {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		System.out.println("Taille tableau ligne : ");
		int ligneGrille = sc.nextInt();
		System.out.println("Taille tableau colonne : ");
		int colonneGrille = sc.nextInt();
				
		System.out.println("Nombre de bateau : ");
		int nbrBateau = sc.nextInt();
		int munition = nbrBateau;
		
		char[] row = {'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'};		
		char[][] grille = new char[ligneGrille][colonneGrille];
		
		for (int i = 0; i != nbrBateau; i++) {
			PlaceBateau(grille, row, ligneGrille, colonneGrille, nbrBateau);
		}
		Affichage(grille, row, ligneGrille, colonneGrille, nbrBateau, munition);
	}

	private static void Affichage(char[][] grille, char[] row, int ligneGrille, int colonneGrille, int nbrBateau, int munition) {
		
		for (int i = 0; i < grille.length; i++) {
			System.out.print("\t|   " + row[i]);
		}
		
		System.out.println("\t|");
		
		int numLigne = 1;
		
		for (int i = 0; i < grille[0].length; i++) {
			for (int j = 0; j < grille.length; j++) {
				System.out.print("--------");
			}
			
			System.out.println("---------");
			System.out.print(numLigne + "\t");
			numLigne += 1;
			
			for (int j = 0; j < grille.length; j++) {
				System.out.print("|   ");
				System.out.print(grille[j][i] + "\t");
			}
			
			System.out.println("|");
		}
		
		for (int i = 0; i < grille.length; i++) {
			System.out.print("--------");
		}
		

		System.out.println("---------");
		Choix(grille, row, ligneGrille, colonneGrille, nbrBateau, munition);
	}
	
	public static void Choix(char[][] grille, char[] row, int ligneGrille, int colonneGrille, int nbrBateau, int munition) {
		Scanner sc = new Scanner(System.in);
		
		System.out.println("Lettre : ");
		char lettre = sc.next().charAt(0);
		
		System.out.println("Chiffre : ");
		int chiffre = sc.nextInt();
		chiffre-=1;
		int chiffre2 = 0;
		
		for (int i = 0; row[i]!= lettre; i++)
			chiffre2 = i+1;
		
		if (grille[chiffre2][chiffre] == 'B') {
			grille[chiffre2][chiffre] = 'X';
			nbrBateau-=1;
		}else
			grille[chiffre2][chiffre] = 'O';
		
		munition-=1;
		
		if (munition == 0) {
			System.out.println("Vous n'avez plus de munition.");
			FinJeu(nbrBateau, 0);
		}
		System.out.println("Nombre de bateau restant " + nbrBateau);
		System.out.println("Nombre de munition restant " + munition);
		
		if(resteBat(grille, row, ligneGrille, colonneGrille, nbrBateau) == true)
			if (nbrBateau != 0)
				Affichage(grille, row, ligneGrille, colonneGrille, nbrBateau, munition);
			else {
				System.out.println("Vous n'avez plus de bateau.");
				FinJeu(nbrBateau, 0);
			}
				
		else
			FinJeu(nbrBateau, 1);
	}

	public static void PlaceBateau(char[][] grille, char[] row, int ligneGrille, int colonneGrille, int nbrBateau) {
		int random1 = new Random().nextInt(grille[0].length);
		int random2 = new Random().nextInt(grille.length);
		int randTailB = new Random().nextInt(3);
		
		if (grille[random2][random1] == 'B' || grille[random2][random1] == 'A' || grille[random2][random1] == 'Z')
			PlaceBateau(grille, row, ligneGrille, colonneGrille, nbrBateau);
		else {
			if (random2+1 < grille.length || random2+2 < grille.length) {
				if(random2-1 > 0 || random2-2 > 0) {
					if (grille[random2][random1] != 'B' || grille[random2][random1] != 'A' || grille[random2][random1] != 'Z') {
						if (grille[random2+1][random1] != 'B' || grille[random2+1][random1] != 'A' || grille[random2+1][random1] != 'Z') {
							if (grille[random2+2][random1] != 'B' || grille[random2+2][random1] != 'A' || grille[random2+2][random1] != 'Z') {
								if (randTailB == 0)
									grille[random2][random1] = 'B';
								else if (randTailB == 1) {
									grille[random2][random1] = 'A';
									grille[random2][random1] = 'A';
								} else {
									grille[random2][random1] = 'Z';
									grille[random2][random1] = 'Z';
									grille[random2][random1] = 'Z';
								}
							} else if (grille[random2-2][random1] != 'B' || grille[random2-2][random1] != 'A' || grille[random2-2][random1] != 'Z')
						} else if (grille[random2-1][random1] != 'B' || grille[random2-1][random1] != 'A' || grille[random2-1][random1] != 'Z')
							grille[random2-1][random1] = 'A';
					} else
						PlaceBateau(grille, row, ligneGrille, colonneGrille, nbrBateau);
				} else
					PlaceBateau(grille, row, ligneGrille, colonneGrille, nbrBateau);
			} else
				PlaceBateau(grille, row, ligneGrille, colonneGrille, nbrBateau);
				
		}
	}

	private static void FinJeu(int nbrBateau, int victoire) {
		if (victoire == 1)
			System.out.println("Gagné");
		else
			System.out.println("Perdu");
		
		System.out.println("Rejouer ?");
		
		Scanner sc = new Scanner(System.in);
		
		int rejouer = sc.nextInt();
		
		if (rejouer == 1)
			main(null);
		else
			System.out.println("Bye ;-°");
	}
	
	private static boolean resteBat(char[][] grille, char[] row, int ligneGrille, int colonneGrille, int nbrBateau) {
		for (int i = 0; i < grille[0].length; i++) {
			for (int j = 0; j < grille.length; j++) {
				if (grille[j][i] == 'B') {
					return true;
				}
			}
		}
		return false;
	}
}
