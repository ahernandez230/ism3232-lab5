# my_toolbox.py
# Author: Ariadna Hernandez


class BakeryToolbox:
    """Every tool request from the model comes through here and is checked."""

    def __init__(self, order_tool, cake_queue):
        """Hold the tools the model is allowed to ask for."""
        self.order_tool = order_tool
        self.cake_queue = cake_queue

    def tool_list(self):
        """Return the tools the model may ask for. They are not called here."""
        return [
            self.order_tool.look_up_order,
            self.cake_queue.request_custom_cake,
        ]

    def run(self, name, arguments, history):
        """Check one tool request. Run the tool only if every check passes."""
        if name == "look_up_order":
            order_id = self.clean(arguments, "order_id")
            if order_id == "":
                return "The order ID is missing. Ask the customer for it."
            if not self.customer_said(history, order_id):
                return "The customer has not given that order ID. Ask them for it."
            return self.order_tool.look_up_order(order_id)
        if name == "request_custom_cake":
            customer_name = self.clean(arguments, "customer_name")
            description = self.clean(arguments, "description")
            if customer_name == "" or description == "":
                return "The customer's name and the cake description are both needed."
            if not self.customer_said(history, customer_name):
                return "The customer has not given that name. Ask them for it."
            if not self.customer_said(history, description):
                return "The customer has not given that description. Ask them for it."
            return self.cake_queue.request_custom_cake(customer_name, description)
        return f"There is no tool named {name}."

    def clean(self, arguments, key):
        """Return one argument as text without extra spaces, or "" if it is missing."""
        return str(arguments.get(key, "")).strip()

    def customer_said(self, history, text):
        """Return True if text appears in a message the customer typed."""
        for message in history:
            if message["role"] == "user" and text.lower() in message["content"].lower():
                return True
        return False
