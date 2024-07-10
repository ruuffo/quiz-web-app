# Ghibli Quiz

Ce répertoire met à disposition une application web développé en vuejs pour un quiz sur les studio Ghibli.

## Fonctionnalités

- **Quiz interactif** : Répondez à une série de questions sur les films Ghibli.
- **Résultats instantanés** : Voyez votre score et les bonnes réponses immédiatement après avoir terminé le quiz.
- **Interface utilisateur conviviale** : Profitez d'une interface simple et intuitive.

- **Interface administrateur** : Gérez les questions via une interface dédiée.

## Installation

Pour installer et exécuter l'application localement, suivez les étapes ci-dessous :

1. **Clonez le dépôt** :

    ```bash
    git clone https://github.com/ruuffo/quiz-web-app
    cd quiz-web-app
    ```

2. **Partie API**
   1. **Accédez au dossier pour lancer l'API**

        ```bash
        cd quiz-api
        ```

   2. **Créez un environnement virtuel et activez-le**

        ```bash
        python -m venv venv
        .\venv\Scripts\activate
        ```

   3. **Installez les dépendances** :

       ```bash
       pip install -r requirements.txt
       ```

   4. **Lancez l'application** :

       ```bash
       flask run
        ```

3. **Partie UI**
    1. **Installez [nodejs](https://nodejs.org/fr/download/prebuilt-installer)**
    2. **Ouvrez un nouveau terminal et placez-vous dans le répertoire [quiz-ui](./quiz-ui/).**
    3. **installer les packages nécessaires**

        ```bash
        npm install
        ```

    4. (Optionnel) Si nécessaire corriger les vulnérabilités

        ```bash
        npm audit fix
        ```

    5. Lancez l'application et accédez-y [ici](http://localhost:3000)

        ```bash
        npm run dev
        ```
