private void Bt_Calculer_Click(object sender, EventArgs e)
{
    if (cbx_TypeSalarie.Text == "Commercial") {
        double  fixe;
        double  ca;

        if (Double.tryParse(tb_Fixe.Text, out fixe) && Double.tryParse(tb_CA.Text, out ca))
            tb_Salaire.Text = (fixe+ (ca/100)).ToString();
        
        else
            tb_Salaire.Text = "Donnée erronées";

    } else {
        int     nbHeures;
        double  tarifH;
        double  txHS;


        if (Int.tryParse(tb_nbHeures.Text, out nbHeures) && Double.tryParse(tb_TarifHeure.Text, out tarifH) && Double.tryParse(tb_tcHS.Text, out txHS)) {
            double salaire = nbHeures * tarifH;
            
            if (nbHeures > 35)
                salaire = salaire + ((nbHeures - 35) * txHS / 100 * tarifH);

            tb_Salaire.Text = salaire.ToString();
        } else
            tb_Salaire.Tect = "Donnée erronées";
    }
}

private void Tb_NbHeures_KeyPress(object sender, KeyPressEventArgs touche)
{
    if ((touche.KeyChar < '0' || touche.KeyChar > '9') && touche.KeyChar != (char)Keys.Back)
        touche.Handled = true;
}

private void Cbx_TypeSalarie_SelectedIndexChanged(object sender, EventArgs e)
{
    if (cbx_commercial.Text == "Commercial") {
        gbx_commercial.Enabled = true;
        gbx_employe.Enabled = false;
    } else {
        gbx_commercial.Enabled = true;
        gbx_commercial.Enabled = false;
    }
}