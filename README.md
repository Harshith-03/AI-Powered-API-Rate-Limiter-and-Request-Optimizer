# AI-Powered API Rate Limiter and Request Optimizer

## Overview
This project implements an **AI-powered API rate limiter** and **request optimizer** using **FastAPI**, **Redis**, and **Machine Learning** to optimize the rate limit of API requests dynamically. The system uses a trained machine learning model to predict the optimal request rate limit based on historical traffic data, and Redis is used to store API request logs and manage rate limiting.

## Features
- **AI-Powered Rate Limiting**: Uses machine learning to predict the optimal rate limit for incoming API requests.
- **FastAPI**: Built with FastAPI to ensure high performance and scalability.
- **Redis Caching**: Redis is used to store and manage API request logs, ensuring fast retrieval and effective rate limiting.
- **AWS Deployment**: The project is deployed on an AWS EC2 instance, making it scalable and production-ready.

## Tools and Technologies
- **Python**: Programming language used for the backend logic.
- **FastAPI**: Web framework for building the API.
- **Redis**: In-memory data store used for caching and managing request logs.
- **Scikit-learn**: Library used for building the machine learning model.
- **Postman**: Tool for testing the API.
- **AWS EC2**: Cloud service used for deploying the application.
- **Git & GitHub**: Version control system and code hosting platform.

## Installation

### Prerequisites
- Python 3.x
- Redis (local installation or AWS instance)
- AWS EC2 instance (for deployment)
