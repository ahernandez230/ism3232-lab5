# echo_model.py
# Author: Ariadna Hernandez


class EchoModel:
    """A stand-in model that repeats the customer's last message."""

    def reply(self, instructions, history):
        """Return 'You said: ' followed by the last message in the history."""
        last_message = history[-1]["content"]
        return "You said: " + last_message
