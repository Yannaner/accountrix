from flask_socketio import emit
from . import socketio

@socketio.on("place_order")
def handle_order(data):
    emit("order_update", {"status": "Order received"}, broadcast=True)
