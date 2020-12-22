# Get-Started-with-Kubernetes
Tl:dr: A simple `hello world` example to get started with Kubernetes. 

## Step 1: Run Locally 
```bash
cd app
```

```bash
pip install -r requirements.txt
python main.py

```

## Step 2: Create Docker Image
In the `app/` directory, build the docker image with the following command
```bash
docker build -f ../docker/Dockerfile -t hello-api:latest .
```
To verify if image was created, run the following command:
```bash
docker image ls
```

## Step 3: Running the Image in Docker
```bash
docker run -p 3050:3000 hello-api
``` 
Now navigate to `http://localhost:3050` to see the message.  

## Step 4: Running in Kubernetes 
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