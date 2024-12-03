#!/usr/bin/python3

import random

data_base = [
    "L'intelligence artificielle révolutionne de nombreux domaines.",
    "Les algorithmes d'apprentissage profond sont au cœur de l'IA moderne.",
    "L'IA peut analyser d'immenses quantités de données en un temps record.",
    "Les assistants virtuels comme Siri et Alexa utilisent l'IA pour interagir avec les utilisateurs.",
    "La vision par ordinateur permet aux machines de comprendre les images.",
    "Le traitement du langage naturel permet à l'IA de comprendre et de générer du texte humain.",
    "Les robots dotés d'IA peuvent effectuer des tâches répétitives avec précision.",
    "L'IA est utilisée pour prédire les tendances du marché et optimiser les investissements.",
    "Les voitures autonomes s'appuient sur l'IA pour naviguer de manière sécurisée.",
    "Les réseaux de neurones artificiels imitent le fonctionnement du cerveau humain.",
    "L'IA génère des œuvres d'art numériques à partir de simples descriptions textuelles.",
    "Le domaine de la santé bénéficie de l'IA pour le diagnostic et le traitement des maladies.",
    "Les systèmes de recommandation, comme ceux de Netflix et Amazon, utilisent l'IA pour suggérer du contenu.",
    "Les modèles d'IA comme ChatGPT sont capables de tenir des conversations cohérentes avec les utilisateurs.",
    "L'IA est essentielle pour le développement de jeux vidéo interactifs et réalistes.",
    "La détection des fraudes bancaires repose sur des modèles d'IA sophistiqués.",
    "Les drones intelligents utilisent l'IA pour planifier leurs itinéraires et éviter les obstacles.",
    "L'IA peut traduire des textes et des discours en plusieurs langues instantanément.",
    "Les technologies d'IA permettent de simuler des environnements pour l'entraînement virtuel.",
    "Les entreprises utilisent l'IA pour automatiser leurs processus et améliorer leur efficacité.",
    "Les chatbots basés sur l'IA sont couramment utilisés dans le support client.",
    "L'IA aide à la détection des anomalies dans les systèmes de cybersécurité.",
    "Les modèles génératifs peuvent créer des contenus uniques, comme des musiques ou des histoires.",
    "L'IA joue un rôle clé dans l'analyse prédictive pour anticiper les besoins futurs.",
    "La collaboration entre humains et IA transforme la manière dont nous travaillons et innovons."
]

question = input("Entrer votre question ? ")

if ('intelligence artificielle' in question.lower()) or ('ia' in question.lower()):
    print(random.choice(data_base))
else:
    print("Désolé, selon ma dernière mise à jour, je ne peux répondre qu'aux questions liées au domaine de l'IA")

