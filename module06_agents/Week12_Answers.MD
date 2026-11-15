# Week 12 answers

## Exercise 1
1. The messages the customer typed: The customer typed: I want to change my shipping address, It's order A102, 9 Pine Street, Tampa

2. How many tool requests were refused, and why: 2 were refused. The first used order A100 and the second used the address 123 Main St, Anytown, AN 12345; the customer had typed neither.

3. If the customer now types "thanks", how many messages does Ollama receive on the next call?: 14 messages

4. Why does "Do you sell gift cards?" still go to a person, and why is that acceptable?: Because the payment rule looks for card anywhere in the message. A wait is a cheap mistake; a missed payment question could put card details in front of the model.

## Exercise 2
Added check_return(order_id) to OrderLookup: A delivered order can be returned within 30 days, anything else cannot be returned yet

## Exercise 3

```
Type a message, or type quit to stop.
You: I want to change my shipping address
Sunny: Your request to change the shipping address for order A100 has been submitted and is awaiting staff approval.
You: quit
Messages in this conversation: 3
Staff review
Request 1: A100 to 123 Main St, Anytown, AN 12345
Approve? yes or no: no
Request 1 rejected.
A100 14 Bay Road
A101 3 Gull Lane
A102 88 Pier Street
```
## Exercise 4
Added FallbackModel in fallback_model.py and tests. 