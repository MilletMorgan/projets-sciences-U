
public class Case {
	
	private Bateau contenue;
	private boolean dejaVise;
	
	public boolean getDejaVise() {
		return dejaVise;
	}
	
	public void setDejaVise(boolean dejaVise) {
		this.dejaVise = dejaVise;
	}
	
	public Bateau getContenue() {
		return contenue;
	}
	
	public void setContenue(Bateau contenue) {
		this.contenue = contenue;
	}
	
	public Case(Bateau contenue, boolean dejaVise) {
		this.dejaVise = dejaVise;
		this.contenue = contenue;
	}
	
	public String toString() {
		if (dejaVise == true && contenue != null)
			return "X";
		if (dejaVise == true && contenue == null)
			return "0";
		if (contenue != null)
			return "B";
		if (contenue == null)
			return "~";
		
		return "";
	}
}
