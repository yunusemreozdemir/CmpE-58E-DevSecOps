# CmpE-58E-DevSecOps

### Working Locally

**Create a Virtual Environment**

```bash
python -m venv venv
```

**Activate the Virtual Environment**

```bash
source venv/bin/activate
```

**Install Requirements**

```bash
pip install -r requirements.txt
pip install pylint pytest

```

**Start the Application**

```bash
uvicorn app.main:app --reload
```

Health Check
```bash
curl --request GET \
  --url http://127.0.0.1:8000/health
```

Echo
```bash
curl --request POST \
  --url http://127.0.0.1:8000/echo \
  --header 'Content-Type: application/json' \
  --data '{
  "test": "data"
}'
```

**Linting**

```bash
pylint app/ tests/
```

**Running the Tests**

```bash
PYTHONPATH=. pytest
```

**Building the Docker Image**

```bash
docker build -t devsecops-fastapi-app:latest .
```

**Running the Docker Container**

```bash
docker run -p 80:80 devsecops-fastapi-app:latest
```

Health Check
```bash
curl --request GET \
  --url http://127.0.0.1:80/health
```

Echo
```bash
curl --request POST \
  --url http://127.0.0.1:80/echo \
  --header 'Content-Type: application/json' \
  --data '{
  "test": "data"
}'
```

### Terraform

**Initialize Terraform**

```bash
cd terraform
terraform init
```

**Plan Terraform**

```bash
terraform plan -var-file=terraform.tfvars
```

**Apply Terraform**

```bash
terraform apply -var-file=terraform.tfvars
```
