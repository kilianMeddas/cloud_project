# Docker Setup Guide for Redis and Flask Application

## Prerequisites
1. Pull the Redis image on Docker:
    ```bash
    docker pull redis
    ```

## Instructions

1. **Create a Docker network:**

    ```bash
    docker network create my_network
    ```

2. **Create a Docker volume:**

    ```bash
    docker volume create redis_data
    ```

3. **Run the Redis container with the created volume:**

    ```bash
    docker run -d --name redis --network my_network -v redis_data:/data redis
    ```

4. **Build and run the Flask application container:**

    After building the Docker image for the app, run it with the following command:
    
    ```bash
    docker run --name kilian --network my_network -p 5000:5000 kmeddas/cloud
    ```

5. **Test the application:**

    To test the connection to the app, use these commands:

    ```bash
    curl http://localhost:5000/products
    ```

    ```bash
    curl -X POST http://localhost:5000/products -H "Content-Type: application/json" -d '{"name": "banane", "price": 69}'
    ```

6. **Restart the container:**

    After the first run, to start the containers again, use:

    ```bash
    docker start <container_name>
    ```

> **Note:** Replace `<container_name>` with the actual name of the container to restart.
