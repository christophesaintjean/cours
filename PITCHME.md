# Introduction à la programmation

Christophe Saint-Jean

[https://gitpitch.com/christophesaintjean/cours/IntroProgS1](https://gitpitch.com/christophesaintjean/cours/IntroProgS1)

Année 2018-2019

---

@transition[fade]

## Organisation de l'UE

### L'équipe enseignante

* Christophe Saint-Jean (Cours/TP - Resp.)
* Laurent Mascarilla (TP)
* El Hadi Zahzah (TP)
* Renaud Péteri (TP)
* *Etc*

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

* 5 cours de 1,5 heures (Amphithéâtre)
* 10 TPs de 1,5 heures (Sallles de TP)
* 2 créneaux de 1,5h de TEA (Salles de TP)

@ulend

+++

### Evaluation

$$Session~1 = \frac{CC_1+CC_2}{2}$$
$$Session~2 = CC_3$$

Les CC se passent en TP sur machine:

* Une partie QCM
* Une partie évaluée par un enseignant
* Attention à la règle sur les absences
* Le TEA sera pris en compte dans l'évaluation

+++

### Les objectifs de cet enseignement

* Découvrir les bases de la programmation informatique
* Maîtriser des concepts
* Appprendre un des langages support de votre formation
* Libérer votre créativité

+++

### *Sondage !*

![images/langages.jpg](Sondage)

---

## Programmer

### Langage humain

* Un certain vocabulaire, une orthographe, des règles de grammaire communes
* Grande expressivité et diversité
* Même si l'on commet des erreurs, nous sommes capables de comprendre "globalement" le message

+++

### Langage informatique

* La machine traite des informations binaires: 100110010101000110 ... (même si images, sons, *programmes*, ...)
* Le vocabulaire d'instructions machine est très réduit
* Pas ou peu (encore) d'expressivité
* Pas de tolérance aux erreurs d'instructions

+++

### Niveau d'un langage

Différents niveaux d'abstraction par rapport aux instructions du processeur:

* 100110010101000110 ... (Quasi-impossible)
* Langages de bas niveau (Ex. Assembleur)
* Langages de bas/haut niveau (Ex. C)
* Langages de haut niveau (Ex. Python, Java, C++, R, ...)

+++

### Programme Source (ou Code)

Un programme source est un *texte* qui dépend du langage:

* Utilise un certain nombre de conventions (nommage, opérations, ...),
* Obéit à des régles de syntaxe, de grammaire
* En génerale, sauvegardé puis exécuté depuis un fichier.

Le mode d'exécution du programme est variable (compilation, interprétation, ...)

+++

### Les différentes sources d'erreur

@ul

* Erreurs de syntaxe: Non respect des conventions du langage
* Erreurs d'exécution (Runtime-Error): Opération non valide lors de l'exécution
* Erreurs sémantiques: Résultat différent de celui désiré

@ulend

+++

### Exécution d'un programme (Compilation)

![images/compilation.png](Compilation)

@ul

* Analogie: Service de traduction intégrale à distance
* Avantages:
  * Rapidité
  * Vérification de la syntaxe à la compilation
* Inconvénients:
  * Temps de compilation (une fois)
  * Mono-cible

@ulend

---

### Exécution d'un programme (Interprétation)

Mettre ici un dessin adapté

* Analogie: Traduction à la volée
* Avantages: Flexibilité
* Inconvénients:
  * Lenteur (/compilateur)
  * découverte d'erreurs à l'exécution

---

### Exécution d'un programme (Hybride)

Mettre ici un dessin adapté

Le meilleur des deux mondes:

* Flexible, relativement rapide, multi-cible

---

### En pratique !

* De nombreux langages disposent à la fois de compilateurs et d'interpréteurs.
* C'est l'usage historique qui a fait penché la balance...

 ```bash
  // Compilation et exécution pour le compilateur gcc
  gcc source.c -o executable
  ./executable

  // Exécution d un code Python
  python source.py
  ```

---

## Les outils d'édition du code

Un environnement de développement intégré est

---

### Quelques paradigmes de programmation

* Langages impératifs (Python, C/C++)
* Langages à objets
* Langages fonctionnels (Javascript, OCAML, Haskell)
* Langages déclaratifs (HTML)

La plupart des langages sont multi-paradigmes.

---

## Quelques exemples de code (Hello World)

* En python:

  ```python
  print('hello world')
  ```

* En java:

  ```java
  public class HW {
      public static void main(String[] args) {
        System.out.println('hello world');
      }
  }
  ```

---

## Vrac

```python
import os
```

$$\alpha = 3$$

---
