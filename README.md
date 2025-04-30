# ONE-FILLER - CLI Application

Auteur: MAGUETTE DIOP - Dev Junior

E-mail : dmax6176@gmail.com

GitHub : jiemCode

28 / 07 / 2023

---

## Description
Ce projet est une application en ligne de commande conçue pour faciliter le processus de remplissage de fichiers SVG avec des champs labelisés en utilisant les informations fournies dans un fichier CSV. L'application est utile dans des cas où vous devez générer plusieurs fichiers SVG personnalisés en fonction des données présentes dans un fichier CSV.

L'application offre les fonctionnalités suivantes :

+ ### Remplissage Automatique :

L'application lit les informations du fichier CSV et remplit automatiquement les champs labelisés du fichier SVG correspondant.

+ ### Personnalisation :

Vous pouvez définir des modèles de fichiers SVG avec des champs spécifiques et les lier aux en-têtes du fichier CSV, permettant ainsi une personnalisation flexible des sorties générées.

+ ### Facilité d'Utilisation :

L'interface en ligne de commande rend l'application conviviale et facile à utiliser, même pour les utilisateurs novices.

---

## 1 - Configuration Requise
Avant d'utiliser l'application, assurez-vous d'avoir les éléments suivants installés sur votre système :

Python (version X.X ou supérieure)
Installation
Téléchargez le code source de l'application à partir du dépôt GitHub.

Assurez-vous d'avoir Python installé sur votre système.

Installez les dépendances nécessaires en exécutant la commande suivante dans le répertoire du projet :

    ~bash
    pip install -r requirements.txt

## 2 - Utilisation
Placez le fichier SVG modèle dans le répertoire de l'application. Assurez-vous que les champs que vous souhaitez remplir sont correctement labelisés avec des noms uniques entre accolades, par exemple : {nom}, {age}, {email}.

Placez votre fichier CSV contenant les informations de remplissage dans le répertoire de l'application. Assurez-vous que les en-têtes du fichier CSV correspondent aux noms des champs labelisés dans le fichier SVG.

Ouvrez une fenêtre de terminal dans le répertoire de l'application.

Exécutez la commande suivante pour remplir les fichiers SVG :

    ~bash
    python app.py --svg fichier_modele.svg --csv fichier_donnees.csv

Les fichiers SVG remplis seront générés dans le répertoire de l'application, portant le nom des enregistrements correspondants dans le fichier CSV.

## 3 - Exemple
Supposons que vous avez un fichier SVG modèle nommé modele.svg avec les champs {prenom} et {profession}, et un fichier CSV nommé donnees.csv avec les colonnes prenom et profession. Vous pouvez exécuter la commande suivante pour remplir le modèle SVG :

    ~bash
    python app.py --svg modele.svg --csv donnees.csv

Cela générera des fichiers SVG remplis pour chaque enregistrement dans le fichier CSV, portant le nom de chaque personne.

## 4 - Avertissement
Assurez-vous de sauvegarder vos fichiers SVG et CSV d'origine, car l'application les modifiera pour les remplir avec les données du fichier CSV.

## 5 - Contribution
Les contributions à l'amélioration de cette application sont les bienvenues! Si vous trouvez des bugs, avez des idées d'amélioration ou souhaitez ajouter de nouvelles fonctionnalités, veuillez soumettre une pull request.

---

### Licence
Ce projet est sous licence MIT. Consultez le fichier LICENSE pour plus d'informations.

Copyrights @jiemCode2023

