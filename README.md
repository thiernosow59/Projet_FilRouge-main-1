# Welfare

## Description

Ce projet à pour but de poser des questions vis à vis du bien-être en entreprise et enregistrer le tout dans une base de donnée.
L'utilisateur pourra ainsi s'enregistrer et répondre de manière anonyme aux différentes questions.

## Prérequis

- docker >= 20.10.12
- python >= 3.10.2

## Kubernetes 

brew install minikube (pour mac os) 

minikube start 

minikube tunnel (laisser le tunnel tourner)

ouvrir un nouveau terminal 

kubectl apply -f .

minikube dashboard

localhost:75000 (dans la barre de recherche)

## Terraform:

Il y'a plusieurs manières d'utiliser terraform pour déployer une application dans le cloud, nous on a choisi docker.

N.B: avant de commencer l'écriture du fichier terraform, préparer votre image docker et l'envoyer dans votre docker hub.

Au début du fichier indique qu'on va utiliser terraform.

Dire à terraform qu'on va utiliser le provider azurerm
    (
        dans ce provider, penser à utiliser vos id de souscriptions azure.
    )

Créer un ressource groupe

Créer un app service plan

Créer un app service
    (       - a ce niveau dire au fichier qu'il va utiliser notre image docker
                -- n'oubliez pas de mettre ":latest" devant votre image.
            - lui indiquer l'url du docker hub hébergeant notre image.
    )

Faire un output pour récupérer l'url du site maintenant hébergé dans le cloud de azure.