from flask import Flask

app = Flask(__name__)

# Set a default value for 'venv' if not already set
app.config.setdefault("venv", "production")

if app.config["venv"] == "production":
    app.config.from_object("config.DevelopmentConfig")
elif app.config["venv"] == "testing":
    app.config.from_object("config.TestingConfig")
else:
    app.config.from_object("config.ProductionConfig")

from app import views
