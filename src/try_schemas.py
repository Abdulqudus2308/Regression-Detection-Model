from pydantic import ValidationError
from schemas import EmailResult

GOOD_SUMMARY = "Customer was charged twice for their monthly subscription."


def run_case(label, **fields):
    try:
        result = EmailResult(**fields)
        print(f"{label} -> accepted: {result}")
    except ValidationError as e:
        print(f"{label} -> rejected: {e.errors()[0]['msg']}")


run_case("valid", email_category="billing", summary=GOOD_SUMMARY)
run_case("empty summary", email_category="billing", summary="")
run_case("unknown category", email_category="refund", summary=GOOD_SUMMARY)
run_case("capital B", email_category="Billing", summary=GOOD_SUMMARY)
run_case("missing summary", email_category="billing")
run_case("spaces only", email_category="billing", summary="      ")
