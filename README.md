# ml-test-policy-paths

Test repo for multi-language policy checks.

- Java (RestTemplate) and Python (requests) both send credit_card_number to https://api.stripe.com/v1/charges.
- Only Python sends ssn to https://api.checkr.com/v1/candidates.
