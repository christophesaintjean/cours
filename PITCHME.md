<style>
.reveal section img { background:none; border:none; box-shadow:none; }
</style>

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

### Analyse: Preuve de terminaison

@ul

* Vérifier que chaque instruction simple se termine:
    * calcul simple, affectation OK
    * affichage OK
    * Appel de fonction -> à vérifier
* Pour les boucles for,  s'assurer que la séquence parcourue est taille finie.
* Pour la répétitive While, s'assurer que dans tous les cas que la condition de continuation sera fausse au moins une fois. 

@ulend

+++

### Analyse : Preuve de correction

Il est question de prouver que l'algorithme fait ce qu'il dit faire !

On utilise souvent un invariant de boucle et la preuve par récurrence.

```
Un invariant de boucle est une propriété qui est vraie avant et après chaque répétition
```

Rappel récurrence: Initialisation et Hérédité.

+++

### Analyse : Complexité algorithmique 1/2

L'algorithme est il rapide ?

Pour un tableau T de taille *n*, la rapidité *devrait* dépendre de:
@ul
* *n* la taille *T*.
* d'une propriété, du contenu de *T*.
* du langage de programmation ?

@ulend

### Analyse : Complexité algorithmique 2/2

Les outils du jour:

* Mesurer le temps d'exécution du programme implémentant l'algorithme (module time)
* Tracer une courbe (module matplotlib)
* Le module tqdm

### Exemple 2

![Maximum Trié](images/max_trie.png)

---

@transition[fade]

## Tableaux et Listes

+++

### Liste

Une **liste** est une structure de données qui contient une séquence de valeurs.

Syntaxe:

```python
[<valeur_1>, <valeur_2>, ..., <valeur_n>]
```

* Les valeurs ne sont pas nécessairement de même type.
* Une liste est une séquence

+++

#### Exemples de listes

```python
In [1]: couleurs = ['rouge', 'vert', 'bleu']

In [2]: Sam = [28 , 'Toronto', False, None]

In [3]: Jeff = [70, 'Cambridge', True, 25]

In [4]: People = [Sam, Jeff]

In [5]: print(People)
[[28, 'Toronto', False, None], [70, 'Cambridge', True, 25]]
```

+++

#### Utilisation d'une liste

On peut rappeler un élément particulier d'une liste par son **indice**.</br>
Pour une liste de longueur *n*, l'indice est un entier entre **0** et **n-1**.

```python
In [1]: couleurs = ['rouge', 'vert', 'bleu']

In [2]: len(couleurs)   # longueur de la liste
Out[2]: 3

In [3]: couleurs[0]
Out[3]: 'rouge'

In [4]: couleurs[5]
...
IndexError: list index out of range
```

+++

#### Liste: Indiçage négatif

Pour faciliter l'accès des derniers éléments d'une liste, *Python* a introduit l'indiçage négatif.

|liste| 'h' | 'e' | 'l' | 'l' | 'o' |
|-|-----|-----|-----|-----|-----|
|indice positif| 0   | 1   | 2   | 3   | 4   |
|indice négatif| -5  | -4  | -3  | -2  | -1  |

Le dernier élément de la liste  toujours l'indice -1.

+++

#### Extraction d'une sous-liste 1/3

Syntaxe ($\sim$ *range*):

```python
       L[<start>:<stop>:<step>]
```

Quelques cas fréquents (L est une liste):

* Eléments entre l'indice 2 (inclus) et l'indice 5 (exclus):</br>
  L[2:5]
* Eléments à partir de  l'indice 4:</br>
  L[4:]
* Les 10 premiers éléments:</br>
  L[:10]

+++

#### Extraction d'une sous-liste 2/3

* Duplication de la liste:</br>
  L[:]
* Un élément sur 2:</br>
  L[::2]

+++

#### Extraction d'une sous-liste 3/3

Quelques cas fréquents avec indice négatif:

* Les 5 derniers éléments:</br>
  L[-5:]
* Tout sauf les derniers 3 éléments:</br>
  L[:-3]
* Duplication de *a* dans l'ordre inverse:</br>
  L[::-1]

+++

#### Affecter une valeur à une liste existante

```python
In [1]: couleurs = ['rouge', 'vert', 'bleu']

In [2]: couleurs[0] = 'jaune'

In [3]: couleurs
Out[3]: ['jaune', 'vert', 'bleu']

In [4]: couleurs[:2]= [34, 48]

In [5]: couleurs
Out[5]: [34, 48, 'bleu']
```

+++

#### Insérer un élément en fin de liste : *append*

```python
In [1]: couleurs = ['rouge', 'vert', 'bleu']

In [2]: couleurs.append('cyan')

In [3]: couleurs
Out[3]: ['rouge', 'vert', 'bleu', 'cyan']

In [4]: L = []   ## liste vide !!!

In [5]: L.append(4)

In [6]: L
Out[6]: [4]
```

+++

#### Insérer un élément : *insert*

Syntaxe ($\sim$ *range*):

```python
    L.insert(<indice>, <element>)
```

Insère avec décalage vers la fin:

```python
In [1]: couleurs = ['rouge', 'vert', 'bleu']

In [2]: couleurs.insert(2, 'cyan')

In [3]: couleurs
Out[3]: ['rouge', 'vert', 'cyan', 'bleu']
```

+++

#### Concaténer deux listes 1/2

Rappel: Concaténer c'est mettre bout à bout deux structures de données.

Deux syntaxes:

```python
    L = L1 + L2 ou L1+=L2
    L1.extend(L2)
```

```python
In [1]: ['rouge', 'vert', 'bleu'] + ['r', 'v', 'b']
Out[1]: ['rouge', 'vert', 'bleu', 'r', 'v', 'b']
```

+++

#### Concaténer deux listes 2/2

```python
In [2]: couleurs = ['rouge', 'vert', 'bleu']

In [3]: couleurs.extend(['r', 'v', 'b'])

In [4]: print(couleurs)
['rouge', 'vert', 'bleu', 'r', 'v', 'b']
```

+++

#### Suppression d'éléments: *del* ou *remove*

```python
    del L[3] ou del L[3:]    ## par indice
    L.remove(5)              ## la première occurrence
```

```python
In [1]: couleurs = ['rouge', 'vert', 'bleu']

In [2]: del couleurs[1]

In [3]: couleurs
Out[3]: ['rouge', 'bleu']

In [4]: couleurs = ['rouge', 'vert', 'bleu', 'vert', 'orange']

In [5]: couleurs.remove('vert')

In [6]: couleurs
Out[6]: ['rouge', 'bleu', 'vert', 'orange']
```

+++

#### Parcours d'une liste par indice

On peut utiliser les indices.

```python
In [1]: couleurs = ['rouge', 'vert', 'bleu']

In [2]: for i in range(len(couleurs)):
          print(couleurs[i].upper(), end=', ')
###
ROUGE, VERT, BLEU,
```

On peut très bien faire aussi avec un *while*

+++

#### Parcours d'une liste par itérateur

Rappel: *for* permet d'itérer toute séquence.

```python
In [1]: couleurs = ['rouge', 'vert', 'bleu']

In [2]: for couleur in couleurs:
          print(couleur.upper(), end=', ')
###
ROUGE, VERT, BLEU,
```

Très simple, mais on a perdu la position dans la liste !

+++

#### Parcours d'une liste par *enumerate*

```python
In [1]: couleurs = ['rouge', 'vert', 'bleu']

In [2]: for i, couleur in enumerate(couleurs):
          print('indice:', i, 'valeur:', couleur.upper())
###
indice: 0 valeur: ROUGE
indice: 1 valeur: VERT
indice: 2 valeur: BLEU
```

C'est le meilleur choix si l'on a besoin de l'indice en plus de la valeur.

+++

#### Exemple sur les listes 1/2

A partir d'une liste de noms, sélectionner ceux qui commencent ou terminent par une voyelle.

```python
In [1]: voyelles = ['a', 'e', 'i', 'o', 'u', 'y']

In [2]: noms = ['mila', 'mathis', 'anne', 'myriam', 'eloan', 'pierre', 'jules']

In [3]: select = []

In [4]: for nom in noms:
          for voyelle in voyelles:
            if nom[0] == voyelle or nom[-1]==voyelle:
              select.append(nom)
              break

In [5]: select
Out[5]: ['mila', 'anne', 'eloan', 'pierre']

```

+++

#### Exemple sur les listes 2/2

Une version plus compacte:

```python
In [1]: voyelles = 'aeiouy'

In [2]: noms = ['mila', 'mathis', 'anne', 'myriam', 'eloan', 'pierre', 'jules']

In [3]: select = []

In [4]: for nom in noms:
          if nom[0] in voyelles or nom[-1] in voyelles:
              select.append(nom)

In [5]: select
Out[5]: ['mila', 'anne', 'eloan', 'pierre']

```