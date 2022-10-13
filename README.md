# Car Evaluation
The purpose behind this project was to demonstrate how to build an instant machine learning application with Streamlit - this is great for rapid prototyping. 
To achieve this I created a simple classification model on the [Car Evaluation Dataset](https://archive.ics.uci.edu/ml/datasets/Car+Evaluation) from the 
[UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/index.php). By following along with the articles below, you will learn how to: create a machine 
learning microservice, create a front end for your machine learning model, and how to wire the two applications together using [Docker](https://www.docker.com/) 
and [Docker-compose](https://docs.docker.com/compose/). The GIF below is a demonstration of how the application works. 

![Example of Machine Learning Web application(2)](https://user-images.githubusercontent.com/43003716/190868371-fb1f5d3f-f74b-4506-9409-0c2fbb1b505e.gif)

## Installation & Usage
These instructions assume that you already have Docker and Docker-compose installed on your machine - if not, please follow the instructions 
[here](https://docs.docker.com/compose/install/). 
- Clone this repository to your computer
- Navigate to the root of the project: `cd car-evaluation-project`
- Build the docker images using `docker-compose up -d --build`
  - This may take a minute
- Open your browser and navigate to http://localhost:8501 to use the application. 

## Extending this project 
- Conduct analysis of the data to build a better classification model
- Set up monitoring for the machine learning model
- Deploy on the cloud

## Articles About this Project 
- [How to Build a Machine Learning Microservice with FastAPI](https://developer.nvidia.com/blog/building-a-machine-learning-microservice-with-fastapi/)
- [How to Build an Instant Machine Learning Web Application with Streamlit and FastAPI](https://developer.nvidia.com/blog/how-to-build-an-instant-machine-learning-web-application-with-streamlit-and-fastapi/)
