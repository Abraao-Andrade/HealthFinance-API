from flask import Flask

from src.main.routes.user_routes import user_router_bp
from src.main.routes.patient_routes import patient_router_bp
from src.main.routes.pharmacie_routes import pharmacie_router_bp
from src.main.routes.transaction_routes import transaction_router_bp

app = Flask(__name__)

app.register_blueprint(user_router_bp)
app.register_blueprint(patient_router_bp)
app.register_blueprint(pharmacie_router_bp)
app.register_blueprint(transaction_router_bp)
