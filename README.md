# CmpE-58E-DevSecOps

## Working Locally

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

**Linting**

```bash
pylint app/ tests/
```

**Running the Tests**

```bash
PYTHONPATH=. pytest
```
