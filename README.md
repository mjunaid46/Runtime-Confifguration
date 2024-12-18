# Runtime-Configuration

This project demonstrates dynamic configuration management in a Dockerized environment. It consists of Python scripts, Docker setup files, and a configuration update process.

## Project Structure

test2/ 

├── external.py # Host-side script to update configuration inside the container

├── new_config2.ini # New configuration file to be copied to the container 

  
│ └── test/ # Contains Docker-related files and runtime scripts 

   ├── Dockerfile # Dockerfile to build the container image 
  
   ├── docker-compose.yml # Compose file to manage services 
  
   ├── dynamic_config.py # Script running inside the container

  
---

## Features

1. **Dynamic Configuration Update**:
   - Use the `external.py` script to copy an updated configuration file (`new_config2.ini`) into a running Docker container.

2. **Real-Time Config Monitoring**:
   - The `dynamic_config.py` script inside the container continuously monitors and logs the configuration file's contents.

3. **Dockerized Deployment**:
   - A lightweight container is built using the `Dockerfile` and managed using `docker-compose`.

---

## Prerequisites

- Python 3.9 or later
- Docker and Docker Compose
- A basic understanding of Docker and Python

---

## How to Run

### 1. Build and Start the Docker Container
1. Navigate to the `test` folder.
   ```bash
   
   cd test
   ```
### 2. Build and run the container.
```bash
docker-compose up --build
```

## 2. Update Configuration Dynamically
1. Edit new_config2.ini with the desired settings.
2. Run the external.py script to update the container's config file.

```bash
python external.py
```
## 3. Monitor Changes in Real Time
-The container logs the content of config2.ini every second.


