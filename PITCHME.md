# Algorithmique des tableaux

Christophe Saint-Jean

[Transparents du cours](https://gitpitch.com/christophesaintjean/cours/AlgoTabS2)

[Code du cours](https://tinyurl.com/ycq9smp7)

Année 2018-2019

---

@transition[fade]

## Organisation de l'UE

+++

### L'équipe enseignante

* **Christophe Saint-Jean** (CM/TD/TP - Resp.)
* Laurent Mascarilla (TD/TP)
* El Hadi Zahzah (TD/TP)

+++

### Communication

* Questions pédagogiques : [Moodle](https://moodle.univ-lr.fr/)
  * Appronfondissement/Questions (Forum)
  * Organisation de l'UE/Planning (Messages privés)
* Questions administratives (Secrétariat)
  * Appartenance groupes TD/TP
  * Absences/Justifications

+++

### Dispositif horaire

@ul

* 6 cours de 1,5 heures (Amphithéâtre)
* 4 TDs de 1,5 heures
* 5 TPs de 1,5 heures (Sallles de TP)
* 4 créneaux de 1,5h de TEA (Salles de TP)

@ulend

+++

### Evaluation

$$S_1 = \frac{CC_1+CC_2}{2}$$

$$S_2 = CC_3$$

Les CC se passent *a priori* en TP 3 et 5 sur machine.
Attention à la règle sur les absences

+++

### Les objectifs de cet enseignement

* Initiation à l'algorithmique
  * Qu'est ce qu'un algorithme ?
  * Différence algorithme / programme (cf. TD)
  * Initiation à l'analyse d'un algorithme.
* Approfondir vos connaissances sur :
  * les listes, tableaux, fonctions.
  * le langage Python.
* Découvrir des algorithmes simples et les analyser.
* Initiation à la récursivité.

---

@transition[fade]

## Généralités sur l'algorithmique

+++

### Algorithme (Définition)

```Un algorithme est la description d’une méthode de calcul qui, à partir d’un ensemble de données d’entrée (problème) et une suite finie d'étapes, produit un ensemble de données en sortie (solution).```

+++

### Analogie recette

1. Mettez la farine dans un saladier avec le sel et le sucre.
2. Faites un puits au milieu et versez-y les œufs légèrement battus à la fourchette.
3. Commencez à incorporer doucement la farine avec une cuillère en bois. Quand le mélange devient épais, ajoutez le lait froid petit à petit.
4. Quand tout le lait est mélangé, la pâte doit être assez fluide, si elle vous paraît trop épaisse, rajoutez un peu de lait. Ajoutez ensuite le beurre fondu, mélangez bien.
5. Faites cuire les crêpes dans une poêle chaude.
6. Répétez jusqu'à épuisement de la pâte.

* Langage de description intelligible
* Instructions séquentielles, fonctions, répétitives.

+++

### Algorithme 1/4

```Un algorithme est la description d’une méthode de calcul qui, à partir d’un ensemble de données d’entrée (problème) et une suite finie d'étapes, produit un ensemble de données en sortie (solution).```

**_Description_**

On doit décrire chaque fonction (sous-algorithmes) et structures de données employées

+++

### Algorithme 2/4

```Un algorithme est la description d’une méthode de calcul qui, à partir d’un ensemble de données d’entrée (problème) et une suite finie d'étapes, produit un ensemble de données en sortie (solution).```

**_Méthode de calcul_**

Il ne peut résoudre que des problèmes calculables.
On démontre que certains problèmes ne sont pas calculables (décidables).

Ex.: Problème de l'arrêt

+++

### Algorithme 3/4

```Un algorithme est la description d’une méthode de calcul qui, à partir d’un ensemble de données d’entrée (problème) et une suite finie d'étapes, produit un ensemble de données en sortie (solution).```

**_Une suite finie d'étapes_**

Attention, ne pas confondre:

* Une séquence d’instructions qui se termine.
* Une description de longueur finie ⇒ possibilité de boucle infinie.

+++

### Algorithme 4/4

```Un algorithme est la description d’une méthode de calcul qui, à partir d’un ensemble de données d’entrée (problème) et une suite finie d'étapes, produit un ensemble de données en sortie (solution).```

**_Solution_**

L'algorithme apporte t'il une solution au problème posé ?

+++

### Algorithmique (Définition)

```L'algorithmique est la science qui étudie les algorithmes pour eux-même indépendamment de tout langage de programmation.```

d'après "Al Khwarizmi", surnom du mathématicien arabe [Muhammad Ibn Musa](https://fr.wikipedia.org/wiki/Al-Khw%C3%A2rizm%C3%AE) (IX siècle).

+++

### Algorithmique (Histoire)

L'algorithmique et les algorithmes sont bien antérieurs à l'informatique:

* Abaques grecques, romaines, [PGCD d'Euclide](https://fr.wikipedia.org/wiki/Algorithme_d%27Euclide) (IIIème siècle av. J.-C.)
* [Boulier chinois](https://fr.wikipedia.org/wiki/Soroban) (XIIIème siècle)
* [Pascaline](Pascalinehttps://fr.wikipedia.org/wiki/Pascaline) (1646)

+++

### Questions de l’algorithmique

1. L’algorithme A est t'il correct ?
2. L’algorithme A se termine t’il ?
3. L’algorithme A est t’il plus efficace qu’un algorithme B ?

Parallèlement, des questions plus fondamentales:

* Est il possible de trouver un algorithme qui resoud un problème P ? (Décidabilité)
* Si, oui existe t’il un algorithme efficace pour le résoudre ? (Classes de complexité)

+++

### Exemple d'algorithme (cf. S1)

```
Algorithme : Approx. π
Données : n (entier) nombre de termes
Résultat : Une approximation décente de π
S <- 0
Pour k<-0 à n-1 Faire:
    Ajouter (-1)^k/(2k+1) à S;
Retourner S;
```

* Correction: Convergence de la série (math)
* Terminaison: Oui.
* Efficacité: La vitesse de convergence (math).

---

@transition[fade]

## Description d'un algorithme

On utilisera un langage de description d'un algorithme appelé **pseudo-code**.

+++

### Caractérisques du pseudo-code

* Il ne doit pas être attaché la syntaxe d'un langage informatique particulier.
* Il doit être lisible par un non-programmeur.
* Être capable de décrire les structures de contrôle des langages impératifs (If, While, For, ...).

+++

### Décrire l'interface de l'algorithme

* Quelques sont les entrées attendues par l'algorithme ?
  * Type : Nombre, Tableau, Liste, Arbre, etc ...
  * Taille : nombre de bits, nombre d'éléments du tableau, nombre de feuilles, ...
  * Propriétés : entiers positifs, tableau trié, ...
* Que fait/produit l'algorithme ?
  * _Idem_ que sur les entrées
  * Description textuelle (éventuelle) de l'algorithme

+++

### Les types utilisables

Types de données élémentaires :

* Variables simples : booléen, entier, réel, caractère
* Tableaux
* *Pointeurs*

Cela permet de d ́efinir des structures de plus haut niveau:

* Chaîne de caractères
* Ensemble, Collection
* Liste, *table de hachage*
* *Graphes, ...*

+++

### Quelques instructions du pseudo-code 1/2

* Affectation : <-
* Test : =
* Opérations arithm ́etiques : +,-,*,/
* Séparateur d’instructions : ” ;”
* Elements d’un tableau T : ”T[i]” (convention 1..n !!)
* Adresse d’une variable ”@”
* Instruction de retour : Retourner <val. sortie>

+++

### Quelques instructions du pseudo-code 2/2

* Le branchement conditionnel :
  
  ```
  Si <condition> alors  
    <blocsi>  
  sinon  
    <blocsinon>
  finSi
  ```

* Les itératives et les répétitives :  
  
  ```
  Pour i <- 1 à n [par pas de 1] faire  
     <bloc>  
  finPour
  
  Tant que <condition> faire
     <bloc>  
  finTq
 ```

+++

### Exemple 1

![Maximum](images/max.png)

+++

### Exemple 2

![Maximum Trié](images/max_trie.png)

---

@transition[fade]

## Listes, Tableaux