<style>
.reveal section img { background:none; border:none; box-shadow:none; }
</style>

# Cours "Python Ecole Doctorale"

Construire des pipelines scientifiques avec Luigi

Christophe Saint-Jean

Année 2019

+++

### Mentions Légales

<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/"><img alt="Licence Creative Commons" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png" /></a><br />Ce(tte) œuvre est mise à disposition selon les termes de la <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/">Licence Creative Commons Attribution - Pas d’Utilisation Commerciale - Partage dans les Mêmes Conditions 4.0 International</a>.

---

## Introduction 1

La plupart d'entre nous (tous) utilisons des pipelines scientifiques pour nos travaux:

* Génération ou recueil (manuel ou automatisé) de données
* Assemblage de plusieurs sources
* Exploration des données recueillies (statistiques, graphiques, ...)
* Analyse(s) des données, Méthodes numériques
* Production de graphiques, tableaux de résultats 

+++

## Introduction 2

Un flot de calcul correspond à un enchaînement de ces tâches qui:

* dépendent les unes des autres
* peuvent être ré-exécuter à intervalles réguliers