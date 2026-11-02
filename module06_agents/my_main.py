# my_main.py
# Author: Ariadna Hernandez

from my_assistant import BakeryAssistant
from my_tool import BakeryOrderLookup

ORDERS = {"CB101": "baking", "CB102": "ready for pickup", "CB103": "picked up"}

order_tool = BakeryOrderLookup(ORDERS)
bot = BakeryAssistant(
    "Quackie",
    "You are a friendly support assistant for Sweet Crumb Bakery.",
    order_tool,
)

print("Type a message, or type quit to stop.")
user_message = input("You: ")
while user_message != "quit":
    print(f"{bot.name}: {bot.respond(user_message)}")
    user_message = input("You: ")

print(f"Messages in this conversation: {len(bot.history)}")
