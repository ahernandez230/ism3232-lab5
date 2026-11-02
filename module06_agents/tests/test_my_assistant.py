# tests/test_my_assistant.py
# Author: Ariadna Hernandez

from my_assistant import BakeryAssistant
from my_tool import BakeryOrderLookup


def make_assistant():
    """Build a fresh assistant with its own tool for each test."""
    order_tool = BakeryOrderLookup(
        {"CB101": "baking", "CB102": "ready for pickup", "CB103": "picked up"}
    )
    return BakeryAssistant(
        "Quackie",
        "You are a friendly support assistant for Sweet Crumb Bakery.",
        order_tool,
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
