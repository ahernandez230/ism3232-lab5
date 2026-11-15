# my_queue.py
# Author: Ariadna Hernandez


class CakeQueue:
    """Custom cake requests waiting for a baker. Nothing is accepted until they approve."""

    def __init__(self):
        """Start with no requests and no accepted cake orders."""
        self.requests = []
        self.cake_orders = []

    def request_custom_cake(self, customer_name, description):
        """Ask the bakers to take a custom cake order. A baker must approve it.

        Args:
            customer_name: The customer's full name.
            description: The cake they want and the date they need it.
        """
        number = len(self.requests) + 1
        self.requests.append(
            {
                "number": number,
                "customer_name": customer_name,
                "description": description,
                "status": "waiting",
            }
        )
        return (
            f"Request {number} was sent to the bakers. The cake is not confirmed yet."
        )

    def waiting(self):
        """Return the requests that are still waiting for a decision."""
        result = []
        for request in self.requests:
            if request["status"] == "waiting":
                result.append(request)
        return result

    def find(self, number):
        """Return the request with this number, or None."""
        for request in self.requests:
            if request["number"] == number:
                return request
        return None

    def approve(self, number):
        """Approve one waiting request and accept the cake order."""
        request = self.find(number)
        if request is None:
            return f"There is no request {number}."
        if request["status"] != "waiting":
            return f"Request {number} is already {request['status']}."
        request["status"] = "approved"
        self.cake_orders.append(request)
        return f"Request {number} approved."

    def reject(self, number):
        """Reject one waiting request. Nothing is accepted."""
        request = self.find(number)
        if request is None:
            return f"There is no request {number}."
        if request["status"] != "waiting":
            return f"Request {number} is already {request['status']}."
        request["status"] = "rejected"
        return f"Request {number} rejected."
