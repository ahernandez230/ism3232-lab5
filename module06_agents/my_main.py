# my_main.py
# Author: Ariadna Hernandez

from my_assistant import BakeryAssistant
from my_queue import CakeQueue
from my_tool import BakeryOrderLookup
from my_toolbox import BakeryToolbox
from ollama_model import OllamaModel

MODEL_NAME = "granite4.1:3b"

INSTRUCTIONS = """You are Quackie, a friendly support assistant for Sweet Crumb Bakery.
Answer in one short sentence.
The bakery is open 7 am to 3 pm, Tuesday through Sunday, and closed on Mondays.
Custom cakes need 48 hours notice.
Only state facts that appear in these instructions.
After a cake request is sent, say a baker will confirm it. Do not say how long approval takes.
If you do not know, say you do not know and offer to pass the customer to a baker."""

ORDERS = {"CB101": "baking", "CB102": "ready for pickup", "CB103": "picked up"}

order_tool = BakeryOrderLookup(ORDERS)
cake_queue = CakeQueue()
tools = BakeryToolbox(order_tool, cake_queue)
model = OllamaModel(MODEL_NAME)
bot = BakeryAssistant("Quackie", INSTRUCTIONS, tools, model)

print("Type a message, or type quit to stop.")
user_message = input("You: ")
while user_message != "quit":
    print(f"{bot.name}: {bot.respond(user_message)}")
    user_message = input("You: ")

print(f"Messages in this conversation: {len(bot.history)}")
