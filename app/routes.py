from flask import jsonify, request, redirect
from app import app
import uuid

@app.route('/')
def hello_world():
    return redirect("https://popkey.in/")

@app.route('/process_paylink', methods=['POST'])
def process_payment():
    # Extract data 
    data = request.json
    
    # Extract relevant information
    amount = data.get('amount')
    merchantTransactionId = data.get('merchantTransactionId')
    mobileNumber = data.get('mobileNumber')

    # Generate a unique payment token
    payment_token = f"transact/pg?token={uuid.uuid4().hex}" 
    short_url = f"https://kishore-t2.poovarasan.com/popzi/pg?token={payment_token}"
    
    # Prepare the response
    response_data = {
        "amount": amount / 100,
        "booked": False,
        "contact": mobileNumber,
        "payment": True,
        "currency": "INR",
        "reference_id": merchantTransactionId,
        "locker_type_id": None,
        "payment_details": {
            "token": payment_token,
            "short_url": short_url
        }
    }
    
    return jsonify(response_data)
