# PromptFlow Docker Deployment

This project demonstrates how to deploy a simple PromptFlow application using Docker. It's designed to run on Ubuntu WSL on Windows, but can be adapted for other environments.

## Prerequisites

- Docker installed on your system
- Basic knowledge of Python and Docker

## Project Structure

```
promptflow-docker/
│
├── flow.py
├── Dockerfile
├── requirements.txt
└── README.md
```

## Setup

1. Clone this repository:
   ```
   git clone https://github.com/kaljuvee/promptflow-docker.git
   cd promptflow-docker
   ```

2. Build the Docker image:
   ```
   docker build -t promptflow-example .
   ```

3. Run the Docker container:
   ```
   docker run promptflow-example
   ```

## Customization

To customize the PromptFlow application, modify the `flow.py` file. You can add your own flows and logic as needed.

## Troubleshooting

If you encounter any issues, please check the following:

- Ensure Docker is properly installed and running.
- Verify that all files (`flow.py`, `Dockerfile`, `requirements.txt`) are in the same directory.
- Check for any error messages in the Docker build or run output.

