# Flask + MongoDB Kubernetes Project 

## Project Overview 

This project demonstrates how to deploy a Flask web application with MongoDB on Kubernetes.

The application is containerized using Docker and deployed on a Kubernetes cluster using Deployment and Services.

## Technologies Used

- Python (Flask)
- MongoDB
- Docker
- Kubernetes
- Docker Hub
- Minikube
- Kubectl

```
## Project Architecture

Browser
  |
Flask Service (NodePort)
  |
Flask Deployment
  |
Flask Pods
  |
MongoDB Service
  |
MongoDB Deployment
  |
MongoDB Pod
```

```
## Project Files

- app.py
- requirements.txt
- Dockerfile
- namespace.yaml
- flask-deployment.yaml
- flask-service.yaml
- mongodb-deployment.yaml
- mongodb-service.yaml
- mongodb-secret.yaml
- mongodb-pvc.yaml
```

## Kubernetes Commands
```bash
kubectl apply -f namespace.yaml

kubectl apply -f mongodb-secret.yaml
kubectl apply -f mongodb-pvc.yaml
kubectl apply -f mongodb-deployment.yaml
kubectl apply -f mongodb-service.yaml

kubectl apply -f flask-deployment.yaml
kubectl apply -f flask-service.yaml

kubectl get pods -n flask-project
kubectl get svc -n flask-project

minikube service flask-service -n flask-project
```

## Features
- Flask application running on kubernetes
- MongoDB database
- Dockerized application
- NodePort Service
- Kubernetes deployment
- kubernetes secret
- multi-pod deployment
- Easy scaling using replicas

## What I Learnes

- Docker Image Creation
- Docker Hub
- Kubernetes Deployment
- Kubernetes Services
- Kubernetes Secrets
- Labels and Selectors
- Pod Networking
- Debugging ImagePullBackOff
- Debugging Service Selector Issues

## Author 
appi47
