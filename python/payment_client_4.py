import requests


def charge_4(card_number, cvv):
    return requests.post("https://api.stripe.com/v1/charges", json={"card_number": card_number, "cvv": cvv})
