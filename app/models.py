# app/models.py

from . import db  # Import the global db object from app/__init__.py
from datetime import datetime
class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False, unique=True)
    cash_balance = db.Column(db.Float, default=0.0)
    balance_sheet = db.Column(db.Text)  # JSON for assets, liabilities, equity
    inventory = db.Column(db.Text)  # JSON for product inventory

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_type = db.Column(db.String(80))
    quantity = db.Column(db.Integer)
    price_per_unit = db.Column(db.Float)
    allocated_to = db.Column(db.Integer, db.ForeignKey('player.id'))  # Foreign key to Player

class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    player_id = db.Column(db.Integer, db.ForeignKey('player.id'), nullable=False)
    type = db.Column(db.String(50), nullable=False)  # "sale", "purchase", "AR", "AP"
    amount = db.Column(db.Float, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)
    debit_account = db.Column(db.String(50))  # E.g., "Cash", "Inventory"
    credit_account = db.Column(db.String(50))  # E.g., "Sales", "AP"
