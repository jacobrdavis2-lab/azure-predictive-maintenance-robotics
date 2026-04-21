# function_app.py
# Azure Function that calls the deployed ML model for real-time inference
# Part of Jacob Davis's predictive maintenance solution
import azure.functions as func
import json
import requests

def main(req: func.HttpRequest) -> func.HttpResponse:
    try:
        telemetry = req.get_json()
        # Call to Azure ML online endpoint
        endpoint_url = "https://jacob-ml-endpoint.azureml.net/score"
        headers = {"Authorization": "Bearer YOUR_MODEL_KEY_HERE"}
        payload = {"data": [telemetry]}
        response = requests.post(endpoint_url, json=payload, headers=headers)
        prediction = response.json()
        risk_score = prediction.get("risk_level", 0)
        return func.HttpResponse(json.dumps({"risk_score": risk_score}), status_code=200)
    except Exception as e:
        return func.HttpResponse(str(e), status_code=400)
