# Connecteur LLF pour Zotero

Ce connecteur a pour but de lancer depuis Zotero une recherche sur le site du Laboratoire de linguistique formelle.

Il ne fonctionne pour le moment que sur les plateformes Linux et MacOS. La version Windows est en cours d’écriture.

L’installation du connecteur aura pour effet de rajouter un moteur de recherche dans l’application Zotero.

## Distribution

Le connecteur est distribué dans sa version 0.2 sous licence CECILL 2.1 :
http://www.cecill.info/licences/Licence_CeCILL_V2.1-fr.txt

L’archive LLF-connector-Zotero-linux-mac-v0.2.tar.gz contient les fichiers suivants :
- *LLF-connector-Zotero-linux-mac.py* : le programme d’installation, à lancer dans un terminal (*shell*) ;
- *README.md* : le présent fichier qui contient des informations diverses ainsi que les instructions d'installation.

## Installation

1. Télécharger la dernière archive
2. Décompacter dans le répertoire de votre choix
3. Lancer le script *LLF-connector-Zotero-linux-mac.py* dans un terminal (*shell*) :
```shell
$ python LLF-connector-Zotero-linux-mac.py
```

## Utilisation

1. Lancer Zotero
2. Sélectionner une publication
3. Cliquer, dans la barre d’outils, sur l’icône représentée par une flèche verte vers la droite
4. Dans le menu contextuel, sélectionner "LLF : quelles sont les publications de l’auteur ?"
