# 🧩 **Compteur de Pièces de Puzzle à partir de Photos**

## Qui sommes-nous ? 👋
Nous, **Pierre Riss** et **Sacha Henneuveux**, développons ensemble une solution permettant de compter le nombre de pièces de puzzle à partir d'une photo. Ce projet est né de notre initiative, soutenue par le **hub Epitech**, qui nous a fourni des moyens techniques pour avancer, notamment avec des ressources de calcul sur un ordinateur puissant.

## Qu’est-ce que ce projet ? 🤔
L’objectif est de faciliter le **comptage des pièces de puzzle** pour des organisations comme **Emmaüs**, qui vend des puzzles et doit s’assurer qu’ils sont complets. Nous avons créé un modèle **Yolo** entraîné pour cette tâche et développons une **application** permettant de faire tourner cette solution en local.

## Quand avons-nous commencé ? 📅
Le projet a démarré il y a **un mois**, avec une première phase de compréhension des **IA** et du travail sur les **CNN (réseaux de neurones convolutifs)**. Nous avons commencé avec des **données synthétiques** générées par **Blender** pour créer des images de pièces de puzzle, et un système d'étiquetage automatique. Nous avons ensuite effectué le **fine-tuning** du modèle **Yolo v11**.

## À quoi cela ressemble ? 👀
Ce projet est **en cours de développement**. Nous avons un modèle capable de **compter les pièces de puzzle** à partir de photos. Le processus inclut :
- La génération d'images via **Blender**.
- L'utilisation de **Yolo v11** pour détecter et compter les pièces.
- Une **application locale** que nous développons pour intégrer tout cela.

### Exemple de ce que ça génère : 📷
![alt text](https://github.com/pierreRISS/Zelia-/blob/main/ressources/images/002593.jpg)
![alt text](https://github.com/pierreRISS/Zelia-/blob/main/ressources/images/002616.jpg)


### Test de l'entraînement sur données de validation: 📷

- Labels :
  ![alt text](https://github.com/pierreRISS/Zelia-/blob/main/ressources/images/val_batch1_labels.jpg)
- Résultat:
  ![alt text](https://github.com/pierreRISS/Zelia-/blob/main/ressources/images/val_batch1_pred.jpg)

## Où en sommes-nous ? 🚀
Le projet est encore en développement, avec quelques défis à surmonter, comme faire tourner l’application **en local** de manière optimale. Nous voulons finaliser cette solution pour que des organisations comme **Emmaüs** puissent l'utiliser facilement pour **compter les pièces de puzzle** rapidement.

## Comment installer le projet ? 🛠️
Voici les étapes pour installer ce projet localement :
1. Installer **Blenderproc** pour générer les images de puzzles.
2. Ajouter WitreYoloanimation.py dans "/venv/lib/python3.11/site-packages/blenderproc/python/"
3. Télécharger **Yolo v11** et configurer l’environnement pour l’entraînement.
4. Suivre les étapes dans les fichiers `README` pour le fine-tuning et l’entraînement du modèle.
5. Mettre en place le modèle dans votre environnement local pour tester.

## Fonctionnalités du projet : 📲
- Prendre des photos des pièces de puzzle éparpillées.
- Utiliser **Yolo v11** pour analyser l’image et détecter le nombre de pièces.
- Application qui tourne en **local** pour réaliser l’analyse sur les photos prises.

## Comment contribuer ? 🤝
Actuellement, le projet est en phase de développement interne. Nous n'acceptons pas encore de contributions externes, mais nous vous tiendrons informés si nous ouvrons les contributions à l'avenir.
