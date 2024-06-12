import mercadopago

sdk = mercadopago.SDK("APP_USR-d183076f-2c11-4f43-940c-b8632db9582b")

payment_data = {
    "transaction_amount": 100,
    
}

result = sdk.payment().create(payment_data)

payment = result["response"]

print(payment)