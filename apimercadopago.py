import mercadopago

sdk = mercadopago.SDK("TEST-28c8f574-ec33-4964-9bdd-9701238837bb")

payment_data = {
    "transaction_amount": 100,
    
}

result = sdk.payment().create(payment_data)

payment = result["response"]

print(payment)