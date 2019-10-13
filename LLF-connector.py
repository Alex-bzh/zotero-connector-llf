#/usr/bin/env python
#-*- coding: utf-8 -*-

# Import des modules
import json, os.path, platform

# Chemin vers le fichier des moteurs, pour un utilisateur Mac ou Linux
path = os.path.expanduser('~') + '/Zotero/locate/engines.json' if (platform.system() in ['Darwin', 'Linux']) else exit()

# Lecture séquentielle du fichier des moteurs Zotero
with open(path) as src:
	txt = temp = ""
	while True:
		temp = src.read(10)
		if temp == "":
			break
		else:
			txt += temp

# Lecture des données au format JSON
data = json.loads(txt)

# Arrêt du programme si le moteur du LLF existe déjà
[exit() if (engine['alias'] == 'LLF') else True for engine in data]

# Configuration du moteur du LLF
LLFengine = {
	"name": "LLF : quelles sont les publications de l’auteur ?",
	"alias": "LLF",
	"icon": "http://www.llf.cnrs.fr/sites/llf.cnrs.fr/files/favicon.png",
	"_urlTemplate": "http://www.llf.cnrs.fr/biblio/author/{rft:aulast?}",
	"description": "Connecteur Zotero des publications du LLF",
	"hidden": False,
	"_urlParams": [],
	"_urlNamespaces": {"rft":"info:ofi/fmt:kev:mtx:journal"}
}
# Ajouter le moteur à la fin de la liste
data.append(LLFengine)
# Renverser l'ordre de la liste pour que le moteur du LLF apparaisse en 1er !
data.reverse()

# Écriture de la liste
with open(path, 'w') as dest:
	json.dump(data, dest, separators=(',', ':'), indent=4)
