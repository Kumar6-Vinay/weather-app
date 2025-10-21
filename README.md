# 🌦️ Weather Dashboard – Flask Web App

A simple and elegant **Flask-based weather dashboard** that fetches real-time weather data using the **OpenWeatherMap API**.  
This project demonstrates backend API integration, frontend templating, and live deployment — ideal for showcasing full-stack development skills.

---

## 🚀 Live Demo
🔗 **[View Live on Render] https://weather-dashboard-mf4n.onrender.com/**  

---

## 🧠 Overview

This web app allows users to:
- Search weather by **city name**
- View **temperature, humidity, and weather conditions** in real-time
- Experience a simple and responsive **Flask + HTML/CSS** interface
- Learn how APIs can power public-facing apps

---

## ⚙️ Tech Stack

| Component | Technology |
|------------|-------------|
| **Backend** | Python (Flask) |
| **Frontend** | HTML, CSS, Bootstrap |
| **API** | [OpenWeatherMap](https://openweathermap.org/) |
| **Hosting** | Render |
| **Version Control** | Git & GitHub |

---


On **Render**, add this under:
> Settings → Environment → Add Environment Variable

| Key | Value |
|------|-------|
| `OPENWEATHER_API_KEY` | your_actual_key_here |


Create a virtual environment (optional but recommended)

python -m venv venv
source venv/bin/activate   # on macOS/Linux
venv\Scripts\activate      # on Windows


Install dependencies

pip install -r requirements.txt


Run the Flask app

python app.py

Then open your browser at http://127.0.0.1:8080


🌍 Deployment on Render

Push your code to GitHub

Go to https://render.com

Create a New Web Service → connect your repo

Add environment variable:

OPENWEATHER_API_KEY = your API key

Add a Procfile:

web: gunicorn app:app

Deploy 🎉

