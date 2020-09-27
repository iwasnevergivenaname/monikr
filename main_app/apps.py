from django.apps import AppConfig
from flask import Flask, render_template
from flask_material import Material 

app = Flask(__name__)
Material(app)

if __name__ == '__main__':
    app.run(debug=True)


class MainAppConfig(AppConfig):
    name = 'main_app'
