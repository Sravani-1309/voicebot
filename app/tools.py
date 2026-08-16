CUSTOMER = {
    "account_id": "ACC-88392",
    "customer_name": "Rahul Sharma",
    "loan_type": "Personal Loan",
    "overdue_amount": 8499,
    "days_overdue": 12,
    "verification_codes": ["1234", "1995"]
}

# Stores successfully authenticated accounts
AUTHENTICATED_ACCOUNTS = set()


def verify_customer(account_id: str, verification_code: str):

    if account_id != CUSTOMER["account_id"]:
        return {
            "verified": False,
            "message": "Customer verification failed."
        }

    if verification_code not in CUSTOMER["verification_codes"]:
        return {
            "verified": False,
            "message": "Customer verification failed."
        }

    AUTHENTICATED_ACCOUNTS.add(account_id)

    return {
        "verified": True,
        "account_id": account_id,
        "customer_name": CUSTOMER["customer_name"],
        "message": "Identity verified successfully."
    }


def is_authenticated(account_id: str):

    return account_id in AUTHENTICATED_ACCOUNTS


def get_debt_information(account_id: str):

    if not is_authenticated(account_id):
        return {
            "success": False,
            "message": "Customer must be verified before debt information can be disclosed."
        }

    return {
        "success": True,
        "account_id": CUSTOMER["account_id"],
        "customer_name": CUSTOMER["customer_name"],
        "loan_type": CUSTOMER["loan_type"],
        "overdue_amount": CUSTOMER["overdue_amount"],
        "days_overdue": CUSTOMER["days_overdue"]
    }


def log_promise_to_pay(
    account_id: str,
    ptp_date: str,
    amount: float
):

    if not is_authenticated(account_id):
        return {
            "success": False,
            "message": "Customer must be verified before recording a promise to pay."
        }

    return {
        "status": "SUCCESS",
        "ptp_id": "PTP-9921",
        "account_id": account_id,
        "confirmed_date": ptp_date,
        "amount": amount
    }


def send_payment_link(
    account_id: str,
    channel: str
):

    if not is_authenticated(account_id):
        return {
            "success": False,
            "message": "Customer must be verified before sending a payment link."
        }

    return {
        "link_sent": True,
        "account_id": account_id,
        "channel": channel,
        "message": f"Payment link sent successfully via {channel}."
    }


def mark_disposition(
    account_id: str,
    status: str,
    notes: str = ""
):

    return {
        "success": True,
        "account_id": account_id,
        "status": status,
        "notes": notes
    }


def escalate_to_agent(
    account_id: str,
    reason: str
):

    return {
        "success": True,
        "account_id": account_id,
        "escalated": True,
        "reason": reason,
        "message": "Call escalated to a human agent."
    }