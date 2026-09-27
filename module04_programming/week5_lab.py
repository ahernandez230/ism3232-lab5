# week5_lab.py
# Author: Ariadna Hernandez
# Business Domain: Italian Food Restaurant

product_name = "Pizza Margherita"
status = "Available"
quantity = 10
unit_price = 12.99
is_over_limit = unit_price * quantity > 1000

print(type(product_name), type(quantity), type(unit_price), type(is_over_limit))

subtotal = unit_price * quantity
tax = subtotal * 0.07
total = subtotal + tax
requires_approval = total > 500

print("=== Purchase Request Summary ===")
print(f"Product:  {product_name}")
print(f"Qty:      {quantity}")
print(f"Subtotal: ${subtotal:.2f}")
print(f"Tax:      ${tax:.2f}")
print(f"Total:    ${total:.2f}")
print(f"Requires approval: {requires_approval}")

# Step 6

user_qty = int(input("Enter the quantity you would like to purchase: "))
new_total = unit_price * user_qty * 1.07
print(f"New total for {user_qty} units: ${new_total:.2f}")
print(f"Requires approval: {new_total > 500}")
