# Expense API Testing Project

## Project Overview

This project aims to perform comprehensive testing on an expense API, ensuring its functionality, reliability, and stability. The tests are designed to cover various aspects of the API, including creating, updating, and retrieving expense entries.

## Purpose

The main purposes of this testing project are:

1. **Functional Testing:** Verify that each API endpoint functions correctly according to the specified requirements.

2. **Data Integrity Testing:** Ensure that data is accurately stored, updated, and retrieved, maintaining integrity throughout the process.

3. **Error Handling Testing:** Validate the API's ability to handle erroneous requests gracefully, providing meaningful error messages.

4. **Performance Testing:** Assess the performance of the API under different scenarios, including handling a varying number of expense entries.

5. **Documentation Validation:** Confirm that the API documentation aligns with the actual behavior of the API.

## Test Scenarios

The test scenarios cover a range of scenarios, including valid and invalid requests, edge cases, and performance testing. The goal is to provide thorough coverage and uncover any potential vulnerabilities or areas of improvement in the API.

## Directory Structure

- **tests/:** Contains test files that cover different aspects of the expense API.
- **utils/:** Houses utility files providing reusable functions for API interactions and test validations.

## How to Run Tests

### 1. Running Tests Using Pytest

To execute the test suite using Pytest, you can use the following command:

```bash
python -m pytest -s -v [optional: test_file_name]
```
-s: Allows printing to the console.
-v: Increases verbosity.
Optionally, you can specify the name of a specific test file (e.g., test_create_expense.py) to run only that particular test.

###2. Generating Allure Test Report
To generate an Allure test report, you can use the following command:

```bash
python -m pytest --alluredir=test_results /tests/*
```

This command generates Allure-compatible XML files in the test_results directory. Afterward, you can use the Allure command-line tool to generate the HTML report:

```bash
allure serve test_results
```
This will open a browser window displaying the interactive Allure test report.

Note: Ensure that the allure command-line tool is installed on your system.

This section provides instructions on running tests using Pytest and generating an Allure test report. Users can choose between running specific test files or generating a comprehensive Allure report for a broader overview of test results.


## Project Structure

This project consists of several files, each serving a specific purpose related to testing an expense API. Below is an overview of the project's structure:

project_directory/
│
├── utils/
│ ├── checking.py
│ ├── api.py
│ ├── http_method.py
│ ├── logger.py
│ └── init.py
│
├── test_create_expense.py
├── test_delete_expense.py
├── test_get_expense.py
├── test_get_list.py
├── test_summary_expense.py
├── test_update_expense.py



## Files description

###1. utils/checking.py
####This file contains utility methods for checking various aspects of API responses.

####Methods:
check_status_code(response, expected_code)
Verifies if the response status code matches the expected code.

check_json_token(response, expected_tokens)
Checks if the JSON response contains the expected tokens.

###2. utils/api.py
This file encapsulates methods for interacting with the expense API.

#####Methods:
get_expense_list(limit=None, offset=None): Gets the list of expenses with optional limit and offset parameters.
get_expense_details(uid): Gets details for a specific expense identified by its UID.
get_total_count_from_list(): Gets the total count of expenses from the expense list.
post_create_expense(json_data): Creates a new expense with the provided JSON data.
put_update_expense(uid, json_data): Updates an existing expense identified by its UID with the provided JSON data.
delete_expense(uid): Deletes an expense identified by its UID.
get_summary_expense(): Gets a summary of expenses.

###3. utils/http_method.py
####Contains methods for making HTTP requests.

####Methods:
send_get_request(url, params=None): Sends a GET request to the specified URL with optional parameters.
send_post_request(url, json_data): Sends a POST request to the specified URL with JSON data.
send_put_request(url, json_data): Sends a PUT request to the specified URL with JSON data.
send_delete_request(url): Sends a DELETE request to the specified URL.

###4. utils/logger.py
####Provides logging functionality for the project.

####Methods:
setup_logger(log_file): Configures the logger with the specified log file.
log_info(message): Logs informational messages.
log_error(message): Logs error messages.

###5. test_create_expense.py
####This test file contains methods to test the creation of expense entries.

####Test Methods:
test_status_code: Checks the response status code after creating a new expense.
test_expenses_values: Checks if the received UID, amount, category, and description match the expected values.
test_expenses_tokens_invalid_request: Checks error tokens for an invalid request.
test_status_code_invalid_json: Checks the response status code for an invalid JSON in the request.

###6. test_delete_expense.py
####This test file contains methods to test the deletion of expense entries.

####Test Methods:
test_status_code: Checks the response status code after deleting an expense.
test_expenses_tokens_nonexistent_uid: Checks tokens for a nonexistent UID.
test_status_code_invalid_request: Checks the response status code for an invalid request.

###7. test_get_expense.py
####This test file contains methods to test the retrieval of expense details.

####Test Methods:
test_status_code: Checks the response status code after getting expense details.
test_expenses_tokens_nonexistent_uid: Checks tokens for a nonexistent UID.
test_status_code_invalid_request: Checks the response status code for an invalid request.

###8. test_get_list.py
####This test file contains methods to test the retrieval of expense lists.

####Test Methods:
test_status_code: Checks the response status code after getting the expense list.
test_expenses_count: Checks the count of expenses in the list.
test_json_tokens: Checks JSON tokens in the response.
test_limit_normal: Checks the response when the limit is between 0 and total_count.
test_limit_0: Checks the response when the limit is 0.
test_limit_total: Checks the response when the limit is total_count.
test_limit_more: Checks the response when the limit is greater than total_count.
test_limit_negative: Checks the response when the limit is negative.
test_limit_less_negative_total: Checks the response when the limit is less than negative total_count.
test_offset_normal: Checks the response when the offset is between 0 and total_count.
test_offset_0: Checks the response when the offset is 0.
test_offset_equal_total: Checks the response when the offset is equal to total_count.
test_offset_more_total: Checks the response when the offset is greater than total_count.
test_offset_negative: Checks the response when the offset is negative.

###9. test_summary_expense.py
####This test file contains methods to test the retrieval of expense summaries.

####Test Methods:
test_status_code: Checks the response status code after getting the summary.
test_summary_tokens: Checks JSON tokens in the response.
test_summary_num_transactions: Checks if num_transactions is equal to the total_count.
test_summary_total_value: Checks if the total sum is correct.

###10. test_update_expense.py
####This test file contains methods to test the update of expense entries.

####Test Methods:
test_status_code: Checks the response status code after updating an expense.
test_expenses_values: Checks if the received UID, amount, category, and description match the expected values.
test_expenses_nonexistent_uid: Checks the response status code for updating an expense with a nonexistent UID.
test_expenses_tokens_nonexistent_uid: Checks tokens for updating an expense with a nonexistent UID.
test_status_code_invalid_request: Checks the response status code for an invalid request.
test_expenses_tokens_invalid_request: Checks tokens for an invalid request.
test_status_code_invalid_json: Checks the response status code for an invalid JSON in the request.

##Explanation of .log Files
The .log files contain logs generated during the execution of the tests. These logs capture information and errors, providing insights into the test execution process. The log files are named based on their purpose or the test file they correspond to. Log files are helpful for debugging and understanding the flow of test execution.