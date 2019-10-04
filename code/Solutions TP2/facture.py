# facture
designation = input("Désignation ? ")

prix_unitaire = input("Prix unitaire ? ")
prix_unitaire = float(prix_unitaire)

quantite = int(input("Quantité ? "))

print("Facture :  ", quantite, designation, "à",
      prix_unitaire, "€ l'unité font",
      prix_unitaire*quantite, "€", sep=" ")


print("Facture :  " + " " +
      str(quantite) + " " +
      designation + " " +
      "à" + " "+
      str(prix_unitaire)+ " " +
      "€ l'unité font" + " " +
      str(prix_unitaire*quantite) + " " +
      "€")
      
print("Facture :   {} {} à {} € l'unité font {} €".format(quantite, designation, prix_unitaire, prix_unitaire*quantite))
print(f"Facture :   {quantite} {designation} à {prix_unitaire} € l'unité font {prix_unitaire*quantite} €")

