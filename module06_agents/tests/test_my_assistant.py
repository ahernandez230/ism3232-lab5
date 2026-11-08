# tests/test_my_assistant.py
# Author: Ariadna Hernandez

from mock_model import MockModel
from my_assistant import BakeryAssistant
from my_tool import BakeryOrderLookup


class SilentModel:
    """A model that never has an answer. It stands in for Ollama being switched off."""

    def reply(self, instructions, history):
        return None


def make_assistant():
    """Build a fresh assistant with its own tool and a mock model for each test."""
    order_tool = BakeryOrderLookup(
        {"CB101": "baking", "CB102": "ready for pickup", "CB103": "picked up"}
    )
    return BakeryAssistant(
        "Quackie",
        "You are a friendly support assistant for Sweet Crumb Bakery.",
        order_tool,
        MockModel(),
    )


def make_assistant_with_silent_model():
    """Build an assistant whose model never answers."""
    order_tool = BakeryOrderLookup(
        {"CB101": "baking", "CB102": "ready for pickup", "CB103": "picked up"}
    )
    return BakeryAssistant(
        "Quackie",
        "You are a friendly support assistant for Sweet Crumb Bakery.",
        order_tool,
        SilentModel(),
    )


def test_tool_returns_none_for_unknown_order():
    assistant = make_assistant()
    assert assistant.order_tool.find_status("CB999") is None


def test_order_question_uses_the_tool():
    assistant = make_assistant()
    assert assistant.respond("Where is order CB101?") == "Order CB101 is baking."


def test_allergy_question_goes_to_a_human():
    assistant = make_assistant()
    assert "baker" in assistant.respond("I have an allergy to nuts.")


def test_unknown_request_gets_a_safe_reply():
    assistant = make_assistant()
    assert "not sure" in assistant.respond("What is the weather today?")


def test_respond_records_both_messages():
    assistant = make_assistant()
    assistant.respond("hello")
    assert len(assistant.history) == 2
    assert assistant.history[0]["role"] == "user"
    assert assistant.history[1]["role"] == "assistant"


def test_other_messages_go_to_the_model():
    assistant = make_assistant()
    assert assistant.respond("hello") == "Hello! How can I help you today?"


def test_safe_reply_when_the_model_has_no_answer():
    assistant = make_assistant_with_silent_model()
    assert "try again" in assistant.respond("hello")


def test_order_rule_does_not_need_the_model():
    assistant = make_assistant_with_silent_model()
    assert assistant.respond("Where is order CB101?") == "Order CB101 is baking."


def test_handoff_rule_does_not_need_the_model():
    assistant = make_assistant_with_silent_model()
    assert "baker" in assistant.respond("I have an allergy to nuts.")
