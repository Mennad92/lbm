# Les biscuits de maman

Bienvenue dans le projet **Les biscuits de maman** ! Il s'agit d'un site web de vente de biscuits artisanaux, développé avec Django, un framework web en Python. Ce site permet aux utilisateurs de parcourir les différents types de biscuits disponibles, d'ajouter des produits à leur panier, et de passer commande en ligne.

## Prérequis

Avant de commencer, assurez-vous d'avoir les éléments suivants installés sur votre machine :

- **Python 3.8+** : Vous pouvez le télécharger depuis [python.org](https://www.python.org/downloads/).
- **pip** : L'outil de gestion de paquets de Python, généralement installé avec Python.
- **virtualenv** : Optionnel, mais recommandé pour isoler l'environnement du projet.

## Installation

### 1. Cloner le dépôt

Commencez par cloner ce dépôt Git sur votre machine locale :

```bash
git clone https://github.com/Mennad92/lbm.git
cd lbm
```

### 2. Créer un environnement virtuel
Il est recommandé d'utiliser un environnement virtuel pour isoler les dépendances du projet :

```bash
python -m venv env
```

Activez l'environnement virtuel :

Sur Windows :
```bash
env\Scripts\activate
```
Sur macOS/Linux :
```bash
source env/bin/activate
```
### 3. Installer les dépendances
Installez les dépendances Python nécessaires à partir du fichier requirements.txt :

```bash
pip install -r requirements.txt
```

### 4. Appliquer les migrations
Appliquez les migrations de la base de données pour configurer les tables nécessaires :

```bash
python manage.py migrate
```
### 5. Créer un superutilisateur
Créez un compte administrateur pour accéder à l'interface d'administration de Django :

```bash
python manage.py createsuperuser
```
### 6. Lancer le serveur de développement
Vous pouvez maintenant lancer le serveur de développement local pour voir le site en action :

```bash
python manage.py runserver
```
Visitez http://127.0.0.1:8000/ dans votre navigateur pour accéder au site.

## Fonctionnalités
- Affichage de la liste des biscuits disponibles
- Gestion du panier d'achats
- Processus de commande en ligne
- Interface d'administration pour gérer les produits, les commandes et les utilisateurs
- Déploiement

Pour déployer ce projet en production, vous pouvez suivre les étapes suivantes :

- Configurer une base de données de production (ex. : PostgreSQL).
- Configurer le serveur web (ex. : Gunicorn, Nginx).
- Mettre à jour les paramètres de production dans settings.py (notamment ALLOWED_HOSTS, DEBUG, etc.).
- Collecter les fichiers statiques avec la commande collectstatic.
- Configurer les services de gestion de certificats SSL (optionnel mais recommandé).

## Contribuer
Les contributions sont les bienvenues ! Si vous souhaitez contribuer au projet, merci de suivre les étapes suivantes :
- Forkez le dépôt.
- Créez une branche pour votre fonctionnalité (git checkout -b nouvelle-fonctionnalite).
- Commitez vos modifications (git commit -m 'Ajouter une nouvelle fonctionnalité').
- Poussez sur la branche (git push origin nouvelle-fonctionnalite).
- Ouvrez une Pull Request.

## Licence
Ce projet est sous licence MIT. Voir le fichier LICENSE pour plus de détails.

## Remerciements
Merci d'avoir utilisé Les biscuits de maman ! Nous espérons que vous apprécierez ce projet autant que nous avons apprécié le développer.