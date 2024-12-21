from flask import Blueprint, jsonify, request
from app.models import Player, Transaction
from app import db

main = Blueprint("main", __name__)

# @main.route("/dashboard/<int:player_id>", methods=["GET"])
# def dashboard(player_id):
#     player = Player.query.get(player_id)
#     if not player:
#         return jsonify({"error": "Player not found"}), 404

#     return jsonify({
#         "username": player.username,
#         "cash_balance": player.cash_balance,
#         "balance_sheet": player.balance_sheet,
#         "inventory": player.inventory
#     })
@main.route("/produce/<int:player_id>", methods=["POST"])
def produce(player_id):
    player = Player.query.get(player_id)
    if not player:
        return jsonify({"error": "Player not found"}), 404

    # For now, simulate inventory production
    new_inventory = {"product": "Widget", "quantity": 10, "unit_cost": 5.0}
    player.inventory = str(new_inventory)  # Update inventory (temporary JSON storage)
    player.cash_balance -= 50.0  # Deduct production cost
    db.session.commit()

    return jsonify({"message": "Production successful", "inventory": player.inventory})


#Stimulating agent order generation
from app.agency.dynamic_decision import generate_order

@main.route("/order/<int:player_id>", methods=["GET"])
def order(player_id):
    player = Player.query.get(player_id)
    if not player:
        return jsonify({"error": "Player not found"}), 404

    # Simulate order creation
    order = generate_order(player_data={"inventory": player.inventory})
    return jsonify(order)

from flask import request
from app.models import Player, Transaction, db
from app.agency.dynamic_decision import generate_order

@main.route("/order/<int:player_id>", methods=["POST"])
def handle_order(player_id):
    player = Player.query.get(player_id)
    if not player:
        return jsonify({"error": "Player not found"}), 404

    # Simulate order creation (in a real game, the order would already exist)
    order = generate_order(player_data={"inventory": player.inventory})

    # Check if the player accepts the order
    data = request.json
    if not data or "action" not in data:
        return jsonify({"error": "Action required"}), 400

    if data["action"] == "accept":
        # Deduct inventory
        inventory = eval(player.inventory)  # Convert JSON-like string back to dict
        if inventory["quantity"] < order["quantity"]:
            return jsonify({"error": "Not enough inventory"}), 400

        inventory["quantity"] -= order["quantity"]
        player.inventory = str(inventory)

        # Record transaction
        transaction = Transaction(
            player_id=player.id,
            type="sale",
            amount=order["quantity"] * order["price_per_unit"],
            debit_account="Cash",
            credit_account="Sales"
        )

        db.session.add(transaction)

        # Add payment terms logic
        if order["payment_terms"] == "Net 30":
            player.cash_balance += 0.5 * transaction.amount  # Partial payment example

        db.session.commit()

        return jsonify({"message": "Order accepted", "remaining_inventory": inventory})

    elif data["action"] == "reject":
        return jsonify({"message": "Order rejected"})

    else:
        return jsonify({"error": "Invalid action"}), 400

@main.route("/transactions/<int:player_id>", methods=["GET"])
def transactions(player_id):
    transactions = Transaction.query.filter_by(player_id=player_id).all()
    return jsonify([{
        "id": t.id,
        "type": t.type,
        "amount": t.amount,
        "date": t.date
    } for t in transactions])


from flask import render_template

@main.route("/dashboard/<int:player_id>")
def dashboard(player_id):
    player = Player.query.get(player_id)
    if not player:
        return "Player not found", 404

    return render_template("dashboard.html",
                           username=player.username,
                           cash_balance=player.cash_balance,
                           balance_sheet=player.balance_sheet,
                           inventory=player.inventory)


@main.route("/order/<int:player_id>", methods=["GET"])
def view_order(player_id):
    player = Player.query.get(player_id)
    if not player:
        return "Player not found", 404

    # Simulate order creation
    order = generate_order(player_data={"inventory": player.inventory})
    return render_template("order.html", order=order, player_id=player.id)
