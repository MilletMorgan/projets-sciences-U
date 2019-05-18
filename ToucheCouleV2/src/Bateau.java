
public class Bateau {

		private String Nom;
		private int Taille;
		private int nbTouche;
		
		public Bateau(String Nom, int Taille, int nbTouche) {
			this.Nom = Nom;
			this.Taille = Taille;
			this.nbTouche = nbTouche;
		}
		
		public String getNom() {
			return Nom;
		}
		
		public void setNom(String Nom) {
			this.Nom = Nom;
		}
		
		public int getTaille() {
			return Taille;
		}
		
		public void setFaille(int Taille) {
			this.Taille = Taille;
		}
		
		public int getNbTouche() {
			return nbTouche;
		}
		
		public void setNbTouche(int nbTouche) {
			this.nbTouche = nbTouche;
		}
		
		
}
