# Customer Churn Prediction System 🚀

A web application built using **Django**, **Tailwind CSS**, and **Scikit-Learn** to predict the likelihood of customer churn. The frontend features a responsive prediction dashboard, and the backend handles processing and inference using a pre-trained machine learning model.

---

## 🛠️ Local Development

### 1. Prerequisites
Make sure you have Python 3.10+ installed.

### 2. Setup environment
Create a virtual environment and install the required packages:
```bash
# Create virtual environment
python -m venv .venv

# Activate virtual environment
source .venv/bin/activate  # On macOS/Linux
# .venv\Scripts\activate   # On Windows

# Install dependencies
pip install -r requirements.txt
```

### 3. Run the application
Run the database migrations and start the Django development server:
```bash
# Run migrations
python churn_project/manage.py migrate

# Run server
python churn_project/manage.py runserver
```
Visit `http://127.0.0.1:8000/` in your browser. It will automatically redirect to the `/dashboard/` endpoint where the form is hosted.

---

## 🌐 Deployment on Render

This project is pre-configured for one-click deployment on **Render** using a Blueprint (`render.yaml`) configuration.

### Deployment Steps:
1. Push this repository to your GitHub account.
2. Sign in to [Render](https://render.com/).
3. Click **New** -> **Blueprint**.
4. Connect this GitHub repository.
5. Click **Approve**. Render will read `render.yaml`, configure the environment, run `build.sh` to install dependencies, run migrations, collect static files, and launch the service via `gunicorn`.

### Manual Deployment Configuration:
If you prefer to configure the web service manually on Render, use the following settings:
* **Runtime**: `Python`
* **Build Command**: `./build.sh`
* **Start Command**: `gunicorn --chdir churn_project churn_project.wsgi:application`
* **Environment Variables**:
  * `PYTHON_VERSION`: `3.11.9`
  * `DEBUG`: `False`
  * `ALLOWED_HOSTS`: `*`
  * `SECRET_KEY`: *(Any secure random string)*