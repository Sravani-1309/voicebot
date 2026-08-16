from fastapi import FastAPI
from pydantic import BaseModel

from app.tools import (
    verify_customer,
    log_promise_to_pay,
    send_payment_link,
    mark_disposition,
    escalate_to_agent,
    get_debt_information,
)

app = FastAPI(title="Voicebot")


class VerificationRequest(BaseModel):
    account_id: str
    verification_code: str


@app.get("/")
def home():
    return {
        "message": "Voicebot backend is running"
    }


@app.post("/verify_customer")
def verify_customer_api(request: VerificationRequest):
    return verify_customer(
        request.account_id,
        request.verification_code
    )


@app.post("/webhook")
def vapi_webhook(data: dict):

    message = data.get("message", {})

    if message.get("type") != "tool-calls":
        return {
            "status": "acknowledged"
        }

    tool_calls = message.get("toolCalls", [])

    results = []

    for tool_call in tool_calls:

        tool_name = tool_call.get("function", {}).get("name")
        arguments = tool_call.get("function", {}).get("arguments", {})
        tool_call_id = tool_call.get("id")

        if tool_name == "verify_customer":

            result = verify_customer(
                arguments.get("account_id"),
                arguments.get("verification_code")
            )

        elif tool_name == "log_promise_to_pay":

            result = log_promise_to_pay(
                arguments.get("account_id"),
                arguments.get("ptp_date"),
                arguments.get("amount")
            )

        elif tool_name == "send_payment_link":

            result = send_payment_link(
                arguments.get("account_id"),
                arguments.get("channel")
            )

        elif tool_name == "mark_disposition":

            result = mark_disposition(
                arguments.get("account_id"),
                arguments.get("status"),
                arguments.get("notes", "")
            )

        elif tool_name == "escalate_to_agent":

            result = escalate_to_agent(
                arguments.get("account_id"),
                arguments.get("reason")
            )

        else:

            result = {
                "success": False,
                "message": f"Unknown tool: {tool_name}"
            }

        results.append({
            "toolCallId": tool_call_id,
            "result": result
        })

    return {
        "results": results
    }

@app.get("/debt/{account_id}")
def debt_information(account_id: str):

    return get_debt_information(account_id)