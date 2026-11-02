# my_assistant.py
# Author: Ariadna Hernandez

HANDOFF_WORDS = ["allergy", "refund", "cancel"]


class BakeryAssistant:
    """A mock bakery assistant. Its replies come from simple rules, not from AI."""

    def __init__(self, name, instructions, order_tool):
        """Set up one assistant with its own name, instructions, tool, and history."""
        self.name = name
        self.instructions = instructions
        self.order_tool = order_tool
        self.history = []

    def respond(self, user_message):
        """Record the user's message, choose a reply, record it, and return it."""
        self.history.append({"role": "user", "content": user_message})
        reply = self.choose_reply(user_message)
        self.history.append({"role": "assistant", "content": reply})
        return reply

    def choose_reply(self, user_message):
        """Choose a reply with keyword rules. This is the mock part."""
        text = user_message.lower()
        if self.needs_human(text):
            return "I can't help with that here. I'm passing you to a baker, since allergies, refunds, and cancellations require human attention."
        if "order" in text:
            return self.order_reply(user_message)
        if "hello" in text:
            return f"Hello! I'm {self.name}. I can check on your cupcake order for you."
        return (
            "I'm not sure how to help with that. I can check a cupcake order for you."
        )

    def needs_human(self, text):
        """Return True if the message is about something a person must handle."""
        for word in HANDOFF_WORDS:
            if word in text:
                return True
        return False

    def order_reply(self, user_message):
        """Use the order tool to answer a question about an order."""
        order_id = self.order_tool.find_order_id(user_message)
        if order_id is None:
            return "Which order? Please send an order ID like CB101."
        status = self.order_tool.find_status(order_id)
        return f"Order {order_id} is {status}."
