# Azure Python API

A FastAPI application deployed on Azure App Service with automated CI/CD via GitHub Actions.

## Live API

| Endpoint | Description |
|----------|-------------|
| [`/`](https://python-api-azure-b9emfebagvg4hvac.southindia-01.azurewebsites.net/) | Root — API status |
| [`/helloworld`](https://python-api-azure-b9emfebagvg4hvac.southindia-01.azurewebsites.net/helloworld) | Returns `{"message": "Hello World"}` |
| [`/docs`](https://python-api-azure-b9emfebagvg4hvac.southindia-01.azurewebsites.net/docs) | Interactive Swagger UI |

## Project Structure

```
azure-python-api/
├── app/
│   └── main.py          # FastAPI application
├── requirements.txt     # Dependencies
├── .gitignore
└── .github/
    └── workflows/
        └── main_python-api-azure.yml  # Auto-generated Azure CI/CD workflow
```

## Tech Stack

- **Framework:** FastAPI
- **Server:** Gunicorn + Uvicorn workers
- **Hosting:** Azure App Service (Linux, Python 3.12)
- **CI/CD:** GitHub Actions via Azure Deployment Center

## Local Development

```bash
# Clone the repo
git clone https://github.com/jofezs/azure-python-api.git
cd azure-python-api

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run locally
uvicorn app.main:app --reload
```

Open `http://127.0.0.1:8000/docs` to test locally.

## Deployment

Every push to `main` automatically triggers a GitHub Actions workflow that builds and deploys the app to Azure App Service.

```bash
git add .
git commit -m "your changes"
git push origin main
```
