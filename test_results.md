# Voicebot Test Results

| Test ID | Scenario | Expected Result | Status |
|---|---|---|---|
| TC01 | Correct verification | Customer authenticated | PASS |
| TC02 | Wrong verification | Authentication rejected | PASS |
| TC03 | Debt before verification | Debt information blocked | PASS |
| TC04 | Successful PTP | Promise recorded | PASS |
| TC05 | Payment link | Payment link sent | PASS |
| TC06 | Already paid | ALREADY_PAID recorded | PASS |
| TC07 | Financial hardship | Escalated to agent | PASS |
| TC08 | Dispute | Escalated to agent | PASS |
| TC09 | Wrong person | No debt disclosure | PASS |
| TC10 | Do-not-call | DO_NOT_CALL recorded | PASS |