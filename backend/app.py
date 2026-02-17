from flask import Flask
from controllers.auth_controller import auth_bp
from controllers.user_controller import user_bp
from controllers.tech_controller import tech_bp
from controllers.ticket_controller import ticket_bp

import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

app = Flask(
    __name__,
    template_folder=os.path.join(BASE_DIR, "templates")
)
app.secret_key = "clave_secreta"

app.register_blueprint(auth_bp)
app.register_blueprint(user_bp)
app.register_blueprint(tech_bp)
app.register_blueprint(ticket_bp)

if __name__ == "__main__":
    app.run(debug=True)
