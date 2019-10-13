#/usr/bin/env python
#-*- coding: utf-8 -*-

# Modules import
import json, os.path, platform

if __name__ == "__main__":

    # Path to Zotero engines (mac & linux)
    path = os.path.expanduser('~') + '/Zotero/locate/engines.json' if (platform.system() in ['Darwin', 'Linux']) else exit()

    # Reading the file
    with open(path) as src:
        txt = temp = ""
        while True:
            temp = src.read(10)
            if temp == "":
                break
            else:
                txt += temp

    # Data in JSON
    data = json.loads(txt)

    # Exit if engine already installed
    [exit() if (engine['alias'] == 'LLF') else True for engine in data]

    # Engine configuration
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

    # Adding the engine to the file
    data.append(LLFengine)

    # Reverse order
    data.reverse()

    # Saving the configuration file of the engines
    with open(path, 'w') as dest:
        json.dump(data, dest, separators=(',', ':'), indent=4)
