# Get-Started-with-Kubernetes
Get Started with Kubernetes

## Run Locally 
```bash
cd app
```

```bash
pip install -r requirements.txt
python main.py

```

## Create Docker Image
In the `app/` directory, build the docker image with the following command
```bash
docker build -f ../docker/Dockerfile -t hello-api:latest .
```
To verify if image was created, run the following command:
```bash
docker image ls
```

## Running the Image in Docker
```bash
docker run -p 3050:3000 hello-api
``` 
Now navigate to `http://localhost:3050` to see the message.  

## Running in Kubernetes 
What is my current context point to? 
```bash
kubectl config current-context
```
Use `kubectl` to send the YAML file to Kubernetes by running the following command:
```bash
kubectl apply -f deployment.yaml
```
To verify the pods are running, execute the following command:
```bash
kubectl get pods
```