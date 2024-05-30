from flask import jsonify, request, redirect
from app import app
import uuid
from .utils import revert_base64
import os

popzi_url = os.getenv('POPZI_URL')
domian_name = os.getenv('DOMAIN_NAME')

@app.route('/')
def hello_world():
    return redirect(popzi_url)

@app.route('/process_paylink', methods=['POST'])
def process_payment():
    # Extract data 
    data = request.json

    # Revert base64 encoding of the payload
    payload = revert_base64(data['request']) 

    # Extract relevant information
    amount = payload.get('amount')
    merchantTransactionId = payload.get('merchantTransactionId')
    mobileNumber = payload.get('mobileNumber')

    # Generate a unique payment token
    payment_token = f"transact/pg?token={uuid.uuid4().hex}" 
    short_url = f"https://{domian_name}/popzi/pg?token={payment_token}"
    
    # Prepare the response
    response_data = {
        "success": True,
        'data': {
            "amount": amount / 100,
            "booked": False,
            "contact": mobileNumber,
            "payment": True,
            "currency": "INR",
            "reference_id": merchantTransactionId,
            "locker_type_id": None,
            "instrumentResponse": {
                "token": payment_token,
                "redirectInfo": {
                    "url": short_url
                }
            }
        }
    }
    
    return jsonify(response_data)
