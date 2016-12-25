import random

from firebase import fb
from response.result import Result

fallback_responses = [
    "I'm sorry. I'm having trouble understanding the question.",
    "I think I may have misunderstood your last statement.",
    "I'm sorry. I didn't quite grasp what you just said.",
    "I don't think I'm qualified to answer that yet.",
    "I'm a bit confused by that last part.",
    "I'm afraid I don't understand."
]


def fallback(query):
    fb.query(query)
    return Result(message=random.choice(fallback_responses))
