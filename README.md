# 🔶 21. La Machine de Turing
## A Docstring Discord Challenge #21
*Marty ! Grimpe dans la DeLorean, on fonce vers 1936 !  
Nous allons assister à la naissance de ce qui a probablement changé la face du monde.*  
-- Emmet "Doc(string)" Brown --

👉  Le but de ce challenge, qui nous est proposé par @Steph,  consiste à développer le prototype d'un "ordinateur" très rudimentaire, qu'on appelle une machine de Turing. Cet ordinateur peut être programmé avec un "langage machine" qui lui est propre.

👉  Le challenge consiste également à écrire un programme pour cette machine, capable d'effectuer la négation d'un nombre binaire quelconque, qui est fourni par l'utilisateur.

👉  Si tu es parvenu à relever les deux défis précédents, un bonus consistera à écrire un autre programme, un peu plus élaboré, capable d'effectuer l'addition de deux nombres binaires quelconques, qui seront également fournis par l'utilisateur.

Tu as probablement déjà dû entendre parler du créateur de cette machine singulière, Alan Turing, qui a été rendu célèbre auprès du grand public, en 2014, par le film **[The Imitation Game](https://www.allocine.fr/film/fichefilm_gen_cfilm=198371.html)**. Si sa machine éveille ta curiosité, tu peux aller consulter [la page de Wikipedia](https://fr.wikipedia.org/wiki/Machine_de_Turing) qui t'en apprendra davantage sur le sujet.

## Description de la machine

Une machine de Turing est un modèle abstrait, c'est-à-dire un objet mathématique, qui décrit le fonctionnement des ordinateurs qu'on connaît aujourd'hui. Ce modèle a été imaginé par Alan Turing en 1936, à une époque où l'ordinateur n'existait pas encore ! Seuls quelques appareils mécaniques de calcul, comme la Pascaline de Blaise Pascal ou la machine analytique de Charles Babbage, existaient alors.

Une machine de Turing est constituée des éléments suivants :

### 1. Une mémoire supposée infinie

Il s'agit d'un modèle abstrait, ne l'oublions pas... Cette mémoire est décrite par un simple ruban de longueur infinie, qui est divisé en cases consécutives. Ces cases peuvent être vides, ou contenir un symbole appartenant à un alphabet donné, de taille finie. Un exemple simple d'alphabet est l'ensemble { 0, 1, _ } permettant d'écrire des nombres binaires sur le ruban. Le symbole _, que l'on pourrait appeler symbole blanc, permet de représenter une case vide du ruban. Par exemple, si l'on souhaite inscrire deux nombres sur le ruban, comme 27 et 13, au format binaire, on obtient :

```
           2 7                   1 3
  ┌─────────┴─────────┐   ┌───────┴───────┐
──┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬──
  │ 1 │ 1 │ 0 │ 1 │ 1 │   │ 1 │ 1 │ 0 │ 1 │  
──┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴──

Donc, avec l'alphabet { 0, 1, _ }, on écrira :

                _11011_1101_

    on se contente ici de ne représenter
        que la partie utile du ruban
```

### 2. Un bus de données

C'est le module de transfert des données entre l'unité centrale de la machine (que nous allons décrire  juste après) et sa mémoire. Ce module est représenté par une tête de lecture / écriture, qui peut se déplacer sur le ruban, d'une case vers la gauche ou d'une case vers la droite (mais d'une seule case à la fois), et lire une donnée, ou en écrire une autre, sur la case qu'elle indique.

```
                      ruban
──┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬──
  │ 1 │ 1 │ 0 │ 1 │ 1 │   │ 1 │ 1 │ 0 │ 1 │  
──┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴──
                    ▲
        tête de lecture / écriture
  qui peut se déplacer d'une case à la fois
 ◀──  vers la gauche ou vers la droite  ──▶
```

### 3. Un registre d'état

Il s'agit d'une mémoire unitaire permettant simplement à la machine de représenter l'état dans lequel elle se trouve, parmi un ensemble d'états donnés, de taille finie. On pourra distinguer, en particulier, l'état initial de la machine, c'est-à-dire l'état dans lequel elle se trouve au moment de démarrer, et un ou plusieurs états finaux, qui marquent l'arrêt du fonctionnement de la machine.

```
                      ruban
──┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬──   ╔═══╗
  │ 1 │ 1 │ 0 │ 1 │ 1 │   │ 1 │ 1 │ 0 │ 1 │     ║ E ║
──┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴──   ╚═╤═╝
                    ▲                             │
        tête de lecture / écriture         registre d'état
```

### 4. Une unité centrale de traitement

C'est en quelque sorte son CPU, dans lequel on a implanté un programme, c'est-à-dire un ensemble d'instructions, exprimées en "langage machine", qui indiquent à la machine quelle(s) opération(s) effectuer, en fonction :
de l'état dans lequel elle se trouve (qui est inscrit dans le registre d'état),
et du symbole inscrit sur le ruban, dans la case qui est pointée par la tête de lecture / écriture.

3 types d'opérations peuvent être effectuée par la machine :
écrire un nouveau symbole sur le ruban, à l'emplacement désigné par la tête de lecture / écriture,
déplacer la tête d'une case vers la gauche, ou vers la droite,
modifier son état en l'inscrivant dans son registre d'état.

Voyons maintenant comment peut être décrit un tel programme.
‎ 
#### Exemple de machine de Turing

Pour se fixer les idées, prenons l'exemple concret d'une machine de Turing capable de déterminer si un nombre binaire est pair ou impair. Pour cela, il suffit d'examiner le bit de poids le plus faible. S'il est égal à 0, alors le nombre est pair. Par contre, s'il est égal à 1, alors le nombre est impair.

Et partons du principe que les conditions initiales sont les suivantes :

```
                    ruban
──┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬──   ╔═══╗
  │ 1 │ 0 │ 1 │ 1 │ 0 │ 0 │ 0 │ 1 │   │   │     ║ a ║
──┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴──   ╚═╤═╝
                                        ▲         │
               position initiale        │    état initial
                   de la tête de  ──────┘
              lecture / écriture
```

Nous choisissons ici de placer la tête de lecture / écriture après le nombre inscrit sur le ruban.

La première chose à faire ici est donc de déplacer la tête vers la gauche jusqu'à ce qu'elle rencontre le premier bit du nombre à examiner. C'est précisément ce que doit effectuer la machine dans son état initial `a` :

```
──┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬──   ╔═══╗
  │ 1 │ 0 │ 1 │ 1 │ 0 │ 0 │ 0 │ 1 │   │   │     ║ a ║  état initial
──┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴──   ╚═══╝
                                        ▲
                     on lit un "blanc" ─┘
donc on déplace la tête vers la gauche

──┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬──   ╔═══╗
  │ 1 │ 0 │ 1 │ 1 │ 0 │ 0 │ 0 │ 1 │   │   │     ║ a ║  on reste dans le même état
──┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴──   ╚═══╝
                                    ▲
                    même chose ici ─┘

──┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬──   ╔═══╗
  │ 1 │ 0 │ 1 │ 1 │ 0 │ 0 │ 0 │ 1 │   │   │     ║ i ║
──┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴──   ╚═╤═╝
                                ▲                 │
    cette fois ci on rencontre ─┘       donc on change d'état
   un bit dont la valeur est 1      et on passe à l'état final "i"
                                   qui marque l'arrêt de la machine
                                avec reconnaissance d'un nomnbre impair
```

Réessayons avec un nombre pair cette fois-ci :

```
──┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬──   ╔═══╗
  │ 1 │ 0 │ 1 │ 1 │ 0 │ 0 │ 1 │ 0 │   │   │     ║ a ║  état initial
──┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴──   ╚═══╝
                                        ▲
                     on lit un "blanc" ─┘
donc on déplace la tête vers la gauche

──┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬──   ╔═══╗
  │ 1 │ 0 │ 1 │ 1 │ 0 │ 0 │ 1 │ 0 │   │   │     ║ a ║  on reste dans le même état
──┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴──   ╚═══╝
                                    ▲
                    même chose ici ─┘

──┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬──   ╔═══╗
  │ 1 │ 0 │ 1 │ 1 │ 0 │ 0 │ 1 │ 0 │   │   │     ║ p ║
──┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴──   ╚═╤═╝
                                ▲                 │
    cette fois ci on rencontre ─┘       donc on change d'état
   un bit dont la valeur est 0      et on passe à l'état final "p"
                                   qui marque l'arrêt de la machine
                                avec reconnaissance d'un nomnbre pair
```

Si l'on souhaite formaliser cet algorithme, nous pourrions l'écrire ainsi :

```
  ┌────────────────── s [state]      état courant de la machine
  │   ┌────────────── r [read]       lecture du ruban
  │   │   ┌────────── w [write]      écriture sur le ruban
  │   │   │   ┌────── m [move]       déplacement de la tête sur le ruban
  │   │   │   │   ┌── n [new state]  nouvel état de la machine
  ▼   ▼   ▼   ▼   ▼
┌───┬───┬───┬───┬───┐
│ a │ _ │   │ < │   │ [a] est l'état initial de la machine
│ a │ 0 │   │   │ p │ [p] => terminaison du programme avec le résultat "pair"
│ a │ 1 │   │   │ i │ [i] => terminaison du programme avec le résultat "impair"
└───┴───┴───┴───┴───┘
└───┬───┘└────┬─────┘ ici, { a, p, i } est l'ensemble des états de la machine
    ▲         ▼
 entrées   sorties
```

Autrement dit, chaque instruction est formée par un quintuplet `<s, r, w, m, n>`, et le programme correspond donc à l'ensemble de ces instructions mises bout-à-bout :

```
┌───┬───┬───┬───┬───╥───┬───┬───┬───┬───╥───┬───┬───┬───┬───┐
│ a │ _ │   │ < │   ║ a │ 0 │   │   │ p ║ a │ 1 │   │   │ i │
└───┴───┴───┴───┴───╨───┴───┴───┴───┴───╨───┴───┴───┴───┴───┘
```

Que l'on peut condenser en une simple chaîne de caractères :

`'a_ < a0  pa1  i'`

## 🔹 Étapes et Conditions

👉  Le programme en Python turing.py que tu dois réaliser doit être capable d'implémenter n'importe quelle machine de Turing, pour peu qu'on lui fournisse comme arguments les éléments suivants :
la suite d'instructions en langage machine à exécuter,
l'état initial du ruban, en prévoyant un ruban suffisamment large pour réaliser les opérations nécessaires,
l'état initial de la machine,
l'ensemble des états finaux qui marquent l'arrêt de la machine,
et la position initiale de la tête de lecture / écriture.

Il devra donc pouvoir être invoqué de la façon suivante :

`> python3 turing.py <program> <ribbon> <init>:<final_set> <head>`

Pour l'exemple précédent, il devra pouvoir être invoqué ainsi :

```
#                                       état initial           position
#                                         du ruban          ┌─ initiale
#                                        ┌────┴───┐         │  de la tête
> python3  turing.py  'a_ < a0  pa1  i'  10110010__  a:p,i  9
#                     └───────┬───────┘              │ └┬┘
#                         programme                  │  └─ état finaux
#                                                    └──── état initial
```

En admettant qu'on ait numéroté les cases du ruban de cette manière :

```
    0   1   2   3   4   5   6   7   8   9
──┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬──   ╔═══╗
  │ 1 │ 0 │ 1 │ 1 │ 0 │ 0 │ 1 │ 0 │   │   │     ║ a ║  état initial
──┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴──   ╚═══╝
                                        ▲
                                position initiale
                         de la tête de lecture / écriture
```

L'exécution du programme `turing.py` devra mettre en évidence la position courante de la tête de lecture, ainsi que le contenu du registre d'état, pendant toute la durée d'exécution :

![affichage script turing.py]()

👉  La deuxième étape de réalisation de ce challenge consistera à concevoir un programme en langage machine capable d'effectuer la négation d'un nombre binaire quelconque, qui est fourni par l'utilisateur. Par exemple, avec le nombre 10110001, voici les conditions initiales que l'on pourrait envisager :

```
    0   1   2   3   4   5   6   7   8   9
──┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬──   ╔═══╗
  │   │ 1 │ 0 │ 1 │ 1 │ 0 │ 0 │ 0 │ 1 │   │     ║ a ║  état initial
──┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴──   ╚═══╝
    ▲
position initiale
de la tête de lecture / écriture
```

Et voici comment doit se terminer l'exécution du programme :

```
    0   1   2   3   4   5   6   7   8   9
──┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬──   ╔═══╗
  │   │ 0 │ 1 │ 0 │ 0 │ 1 │ 1 │ 1 │ 0 │   │     ║ @ ║  état final
──┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴──   ╚═══╝
                                        ▲
                                 position finale
                         de la tête de lecture / écriture
```

Là aussi, on souhaite pouvoir suivre l'exécution du programme pas-à-pas. Tu pourrais utiliser la méthode time.sleep() pour ralentir l'exécution du programme Python afin que l'on puisse observer les différentes étapes de l'algorithme exécuté sur la machine de Turing :
‎‎‎‎ ‎ ‎ 
![gif de la machine de Turing en action]()

***NB** : j'ai volontairement encapsulé le programme dans une variable `PROGRAM` pour ne pas le dévoiler.* 🤫

## 🔹 Bonus

Maintenant que ta machine de Turing est au point, tu vas devoir te pencher sur la mise en œuvre d'un algorithme un peu plus élaboré, pour réaliser l'addition de deux nombres binaires inscrits sur le ruban et séparés par une case vide (donc un blanc). Par exemple, si l'on souhaite réaliser l'addition des nombres décimaux 45 et 9 écrits en binaire, voici les conditions initiales que l'on pourrait envisager :

```
    0   1   2   3   4   5   6   7   8   9  10  11  12
──┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬──   ╔═══╗
  │   │ 1 │ 0 │ 1 │ 1 │ 0 │ 1 │   │ 1 │ 0 │ 0 │ 1 │   │     ║ a ║
──┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴──   ╚═══╝
        ▲
```

Et voici l'état de la machine une fois le programme terminé :

```
    0   1   2   3   4   5   6   7   8   9  10  11  12
──┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬──   ╔═══╗
  │   │ 1 │ 1 │ 0 │ 1 │ 1 │ 0 │   │   │   │   │   │   │     ║ @ ║
──┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴──   ╚═══╝
                                                    ▲
```

Voici le déroulement de l'opération pas-à-pas :

![machine de Turing]()

**Maintenant, à toi de jouer ! 💪**
