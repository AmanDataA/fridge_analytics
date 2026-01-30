# ==============================
# PRODUCTS DATA
# ==============================

products = {
    "Milk": {"price": 80, "quantity": 2, "calories_per_100g": 60},
    "Bread": {"price": 30, "quantity": 3, "calories_per_100g": 100},
    "Honey": {"price": 100, "quantity": 2, "calories_per_100g": 50},
    "Chicken": {"price": 40, "quantity": 4, "calories_per_100g": 200},
    "Kefir": {"price": 75, "quantity": 1, "calories_per_100g": 80},
}

print("------ Products that meet conditions ------")

# ==============================
# INITIAL VALUES
# ==============================

total_spent = 0
total_unit_price = 0

highest_calories = 0
highest_cal_product = ""

highest_price = 0
most_expensive = ""

# ==============================
# LOOP THROUGH PRODUCTS
# ==============================

for name, data in products.items():
    cost = data["price"] * data["quantity"]
    total_spent += cost
    total_unit_price += data["price"]

    if data["price"] > highest_price:
        highest_price = data["price"]
        most_expensive = name

    if data["calories_per_100g"] > highest_calories:
        highest_calories = data["calories_per_100g"]
        highest_cal_product = name

    if data["quantity"] > 2 and data["price"] > 50:
        print(f"{name} - ${data['price']} - qty: {data['quantity']}")

# ==============================
# CALCULATE AVERAGE PRICE
# ==============================

average_price = total_unit_price / len(products)

print(f"Total spent: ${total_spent}")
print(f"Most expensive product: {most_expensive}")
print(f"Highest calorie product: {highest_cal_product}")
print(f"Average unit price: ${average_price:.2f}")

