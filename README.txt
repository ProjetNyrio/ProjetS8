Notes importantes à l'utilisation des interfaces de traitement d'image et contrôle du robot :

Le dossier contenant le code fonctionnel et permettant l'utilisation du projet est Interface Complete.

Base Interface est un dossier contenant d'autres essais de programmation d'interfaces via tkinter qui nous ont permis de tester différentes possibilités d'intéragir avant de selectionner la plus adaptée, nous avons donc choisi de laisser Base Interface accessible sur le depôt git pour permettre de comprendre l'évolution de notre projet.

Le dossier Interface Complete vous permet d'acceder à la version finale du programme et de le tester. Celui-ci s'appelle interface_complete.py
Il dispose également de video_canvas.py une classe régissant le comportement du widget servant à afficher le flux vidéo de la caméra du robot.
Enfin on trouve deux autres dossiers : images_natives ou sont stockées les images incorporées à l'interface, et demo_scripts qui contient quelques programmes que nous avions écrits pour tester l'interface IDLE de traitement d'image, et que nous avons donc choisi de rendre accesible à l'utilisateur.

Le panneau de contrôle permet de contrôler les différents axes du robot en leur passant en paramètre une valeur en radians.
L'interface de traitement d'image quant à elle à besoin que l'on enregistre le code avant chaque éxécution sinon elle ne prend pas en compte les dernier changements.

Enfin l'interface est utilisable avec des thèmes, ne sachant pas nous avions le droit de poster un theme ayant son propre dépot git sur notre dépot nous avons préféré laisser l'utilisateur se charger d'installer le theme si il le souhaite.
Le thème que nous utilisions était Azure-ttk-theme disponible à l'adresse suivante :
https://github.com/rdbende/Azure-ttk-theme 

Merci et bonne utilisation de nos interfaces!
