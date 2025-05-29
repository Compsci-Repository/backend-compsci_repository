# BACKEND COMPSCI REPOSITORY

## Description
This repository contains the backend code for the Compsci Repository project.
It is built using Python, Flask and PostgresSQL, and it provides a RESTful API for the frontend to interact with.

The backend is designed to be modular and easy to extend, using OO principles and design patterns. 
The architecture is based on the MVC pattern.

As use Flask, it use routes to define the endpoints for the API. 
Actually, the routes are defined in the folder `controler` and set in the `app.py` file, 
and they are organized by resource.

## How to run the project

### Docker
Use  Docker is the recommended way to run the project.
1. Install Docker and Docker Compose.
2. Clone the repository.
3. Navigate to the project directory.
4. Build the Flask app image using the command:
   ```
   docker build -t compsci_repository  .
   ```
5. Build and run the Docker containers using the command:
   ```
   docker compose up -d --build
   ```
   
6. Access the API at `http://localhost:5000`.
7. *You can access the PostgreSQL database at `localhost:5432` using the credentials defined in the `docker-compose.yml` file.
