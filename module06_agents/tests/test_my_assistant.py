# tests/test_my_assistant.py
# Author: Ariadna Hernandez

from fake_model import FakeModel
from keyword_model import KeywordModel
from my_assistant import BakeryAssistant
from my_queue import CakeQueue
from my_tool import BakeryOrderLookup
from my_toolbox import BakeryToolbox


class SilentModel:
    """A model that never has an answer. It stands in for Ollama being switched off."""

    def decide(self, instructions, history, tools):
        return None


def make_assistant(model):
    """Build a fresh assistant with its own tools and the model it is given."""
    order_tool = BakeryOrderLookup(
        {"CB101": "baking", "CB102": "ready for pickup", "CB103": "picked up"}
    )
    tools = BakeryToolbox(order_tool, CakeQueue())
    return BakeryAssistant(
        "Quackie",
        "You are a friendly support assistant for Sweet Crumb Bakery.",
        tools,
        model,
    )


def ask_for_tool(name, arguments):
    """Build the decision a model returns when it wants a tool."""
    return {"tool": name, "arguments": arguments}


def test_tool_returns_none_for_unknown_order():
    assistant = make_assistant(KeywordModel())
    assert assistant.tools.order_tool.find_status("CB999") is None


def test_order_question_uses_the_tool():
    model = FakeModel(
        [ask_for_tool("look_up_order", {"order_id": "CB101"}), {"text": "Baking!"}]
    )
    assistant = make_assistant(model)
    assistant.respond("Where is order CB101?")
    assert assistant.history[1]["content"] == "Order CB101 is baking."


def test_allergy_question_goes_to_a_human():
    assistant = make_assistant(FakeModel([]))
    assert "baker" in assistant.respond("I have an allergy to nuts.")


def test_unknown_request_gets_a_safe_reply():
    assistant = make_assistant(KeywordModel())
    assert "not sure" in assistant.respond("What is the weather today?")


def test_respond_records_both_messages():
    assistant = make_assistant(KeywordModel())
    assistant.respond("hello")
    assert len(assistant.history) == 2
    assert assistant.history[0]["role"] == "user"
    assert assistant.history[1]["role"] == "assistant"


def test_other_messages_go_to_the_model():
    assistant = make_assistant(KeywordModel())
    assert assistant.respond("hello") == "Hello! How can I help you today?"


def test_safe_reply_when_the_model_has_no_answer():
    assistant = make_assistant(SilentModel())
    assert "try again" in assistant.respond("hello")


def test_made_up_name_is_refused():
    model = FakeModel(
        [
            ask_for_tool(
                "request_custom_cake",
                {"customer_name": "Dana Cruz", "description": "chocolate cake"},
            ),
            {"text": "What is your name?"},
        ]
    )
    assistant = make_assistant(model)
    assistant.respond("I want a custom cake")
    assert "has not given that name" in assistant.history[1]["content"]
    assert assistant.tools.cake_queue.waiting() == []


def test_cake_request_waits_for_a_baker():
    model = FakeModel(
        [
            ask_for_tool(
                "request_custom_cake",
                {"customer_name": "Dana Cruz", "description": "chocolate cake"},
            ),
            {"text": "Sent to the bakers."},
        ]
    )
    assistant = make_assistant(model)
    assistant.respond("I'm Dana Cruz and I want a chocolate cake")
    assert len(assistant.tools.cake_queue.waiting()) == 1
    assert assistant.tools.cake_queue.cake_orders == []


def test_second_approval_changes_nothing():
    assistant = make_assistant(FakeModel([]))
    queue = assistant.tools.cake_queue
    queue.request_custom_cake("Dana Cruz", "chocolate cake")
    assert queue.approve(1) == "Request 1 approved."
    assert queue.approve(1) == "Request 1 is already approved."
    assert len(queue.cake_orders) == 1


def test_handoff_never_reaches_the_model():
    assistant = make_assistant(FakeModel([]))
    assert "baker" in assistant.respond("I have an allergy to nuts.")
