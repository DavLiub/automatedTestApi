# Expense API Testing Checklist

Use this checklist to ensure comprehensive testing coverage for the expense API. Mark each item as completed when the corresponding test scenario has been executed and verified.

## Test Scenarios

### 1. GET Expense 

### GET: /v1/expense/{expense_uid}

- [x] Verify response status code for a valid GET request (Expected: 200 OK).
- [x] Confirm the correctness of the received entry UID.
- [x] Check if received tokens match the expected tokens.
- [ ] Verify response status code for an invalid GET request with a nonexistent UID to `/v1/expense/{nonexistent_uid}` (Expected: 404 Not Found).
- [ ] Check error tokens for an invalid GET request with a nonexistent UID to `/v1/expense/{nonexistent_uid}`.

### 2. GET Expense List 

### GET: /v1/expense?limit=№&offset=№

- [x] Validate response status code for a valid GET request (Expected: 200 OK).
- [x] Confirm the correct count of expenses in the list.
- [x] Check received tokens for a valid GET request (without options).
- [x] Test with various limit parameters (normal, 0, total_count, more, negative).
- [x] Test with various offset parameters (normal, 0, total_count, more, negative).
- [x] Verify response status code for invalid requests (limit/offset as float or string).

### 3. Summary Expense 

### GET: /v1/summary?start_date="DD-MM-YYYY"&end_date="DD-MM-YYYY"

- [x] Validate response status code for a valid summary request to (Expected: 200 OK).
- [x] Confirm the correctness of the received tokens.
- [x] Check if the value of num_transactions matches the total count from the expense list.
- [x] Validate the total sum received in the summary against the total sum calculated from the expense list.
- [x] Verify response status code for an invalid summary request without authentication.

### 4. PUT Update Expense 

### PUT: /v1/expense
```json
{
  "amount": "number",
  "category": "string",
  "description": "string"
}
```
- [x] Verify response status code for a valid PUT request (Expected: 200 OK).
- [x] Confirm the received UID, amount, category, and description match the expected values.
- [x] Verify response status code for updating an entry with a nonexistent UID (Expected: 404 Not Found).
- [x] Check error tokens for updating an entry with a nonexistent UID.
- [x] Verify response status code for an invalid PUT request without a body(Expected: 400 Bad Request).
- [x] Check error tokens for an invalid PUT request without a body.
- [x] Verify response status code for an invalid PUT request with incorrect JSON data (Expected: 400 Bad Request).
- [ ] Verify response status code for an invalid PUT request with incomplete JSON data (Expected: 400 Bad Request).

### 5. DELETE Expense Endpoint

### DELETE: /v1/expense/{expense_uid}

- [ ]  Verify response status code for a valid DELETE request (Expected: 204 Deleted).
- [ ]  Confirm that the entry with the specified UID has been successfully deleted.
- [ ]  Verify response status code for a DELETE request with a nonexistent UID (Expected: 404 Not Found).
- [ ]  Check error tokens for a DELETE request with a nonexistent UID .
- [ ]  Verify response status code for an invalid DELETE request with a malformed UID (Expected: 400 Bad Request).
- [ ]  Check error tokens for an invalid DELETE request with a malformed UID.

## Additional Tests

- [x] Execute performance testing with a varying number of expense entries.
- [x] Validate API documentation against actual API behavior.
- [x] Verify response status code for an invalid request with malformed JSON data to `/v1/expense` (Expected: 400 Bad Request).
- [x] Check error tokens for an invalid request with malformed JSON data to `/v1/expense`.

## How to Run Tests

Refer to the project's README for instructions on executing the test suite and generating an Allure test report.
