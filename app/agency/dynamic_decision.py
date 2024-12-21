import random

def generate_order(player_data):
    # Placeholder logic for order generation
    return {
        "product_type": "Widget",
        "quantity": random.randint(1, 20),
        "price_per_unit": round(random.uniform(5.0, 15.0), 2),
        "payment_terms": random.choice(["Net 30", "Net 60", "Net 90"])
    }
