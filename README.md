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

#### [Check list with latest results here](https://docs.google.com/spreadsheets/d/1aNPkDXLTJkZ0Z4gBNLPEyHZEjuNoy4R-673wqIylBP4/edit?usp=sharing, "https://docs.google.com/spreadsheets/d/1aNPkDXLTJkZ0Z4gBNLPEyHZEjuNoy4R-673wqIylBP4/edit?usp=sharing")

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

### 2. Generating Allure Test Report
To generate an Allure test report, you can use the following command:

```bash
python -m pytest --alluredir=test_results tests/
```

This command generates Allure-compatible XML files in the test_results directory. Afterward, you can use the Allure command-line tool to generate the HTML report:

```bash
allure serve test_results
```
This will open a browser window displaying the interactive Allure test report.

Note: Ensure that the allure command-line tool is installed on your system.You can install Allure Command Line by following the instructions on the official Allure Framework website: [Installing Allure](https://allurereport.org/docs/gettingstarted-installation/, "https://allurereport.org/docs/gettingstarted-installation/")

This section provides instructions on running tests using Pytest and generating an Allure test report. Users can choose between running specific test files or generating a comprehensive Allure report for a broader overview of test results.


## Files description

### 1. utils/checking.py
#### This file contains utility methods for checking various aspects of API responses.

#### Methods:

<table>
    <tr>
        <th>Methods</th>
        <th>Description</th>
    </tr>
    <tr>
        <td>check_status_code(response, expected_code)</td>
        <td>Verifies if the response status code matches the expected code</td>
    </tr>
    <tr>
        <td>check_json_token(response, expected_tokens)</td>
        <td>Checks if the JSON response contains the expected tokens</td>
    </tr>
</table>


### 2. utils/api.py
#### This file encapsulates methods for interacting with the expense API.

#### Methods:

<table>
    <tr>
        <th>Methods</th>
        <th>Description</th>
    </tr>
    <tr>
        <td>get_expense_list(limit=None, offset=None)</td>
        <td>Gets the list of expenses with optional limit and offset parameters.</td>
    </tr>
    <tr>
        <td>get_expense_details(uid)</td>
        <td>Gets details for a specific expense identified by its UID</td>
    </tr>
	<tr>
		<td>get_total_count_from_list()</td>
		<td>Gets the total count of expenses from the expense list</td>
	</tr>
	<tr>
		<td>post_create_expense(json_data)</td>
		<td>Creates a new expense with the provided JSON data</td>
	</tr>
	<tr>
		<td>put_update_expense(uid, json_data)</td>
		<td>Updates an existing expense identified by its UID with the provided JSON data</td>
	</tr>
	<tr>
		<td>delete_expense(uid)</td>
		<td>Deletes an expense identified by its UID</td>
	</tr>
	<tr>
		<td>get_summary_expense()</td>
		<td>Gets a summary of expenses</td>
	</tr>
</table>

### 3. utils/http_method.py
#### Contains methods for making HTTP requests.

#### Methods:

<table>
    <tr>
        <th>Methods</th>
        <th>Description</th>
    </tr>
    <tr>
        <td>send_get_request(url, params=None)</td>
        <td>Sends a GET request to the specified URL with optional parameters</td>
    </tr>
    <tr>
        <td>send_post_request(url, json_data)</td>
        <td>Sends a POST request to the specified URL with JSON data</td>
    </tr>
	<tr>
		<td>send_put_request(url, json_data)</td>
		<td>Sends a PUT request to the specified URL with JSON data</td>
	</tr>
	<tr>
		<td>send_delete_request(url)</td>
		<td>Sends a DELETE request to the specified URL</td>
	</tr>
</table>

### 4. utils/logger.py
#### Provides logging functionality for the project.

#### Methods:

<table>
    <tr>
        <th>Methods</th>
        <th>Description</th>
    </tr>
    <tr>
        <td>setup_logger(log_file)</td>
        <td>Configures the logger with the specified log file</td>
    </tr>
    <tr>
        <td>log_info(message)</td>
        <td>Logs informational messages</td>
    </tr>
	<tr>
		<td>log_error(message)</td>
		<td>Logs error messages</td>
	</tr>
</table>

### 5. test_create_expense.py
#### This test file contains methods to test the creation of expense entries.

#### Test Methods:

<table>
    <tr>
        <th>Methods</th>
        <th>Description</th>
    </tr>
    <tr>
        <td>test_status_code</td>
        <td>Checks the response status code after creating a new expense</td>
    </tr>
    <tr>
        <td>test_expenses_values</td>
        <td>Checks if the received UID, amount, category, and description match the expected values</td>
    </tr>
	<tr>
		<td>test_expenses_tokens_invalid_request</td>
		<td>Checks error tokens for an invalid request</td>
	</tr>
	<tr>
		<td>test_status_code_invalid_json</td>
		<td>Checks the response status code for an invalid JSON in the request</td>
	</tr>
</table>

### 6. test_delete_expense.py
#### This test file contains methods to test the deletion of expense entries.

#### Test Methods:

<table>
    <tr>
        <th>Methods</th>
        <th>Description</th>
    </tr>
    <tr>
        <td>test_status_code</td>
        <td>Checks the response status code after deleting an expense</td>
    </tr>
    <tr>
        <td>test_expenses_tokens_nonexistent_uid</td>
        <td>Checks tokens for a nonexistent UID</td>
    </tr>
	<tr>
		<td>test_status_code_invalid_request</td>
		<td>Checks the response status code for an invalid request</td>
	</tr>
</table>

### 7. test_get_expense.py
#### This test file contains methods to test the retrieval of expense details.

#### Test Methods:

<table>
    <tr>
        <th>Methods</th>
        <th>Description</th>
    </tr>
    <tr>
        <td>test_status_code</td>
        <td>Checks the response status code after getting expense details</td>
    </tr>
    <tr>
        <td>test_expenses_tokens_nonexistent_uid</td>
        <td>Checks tokens for a nonexistent UID</td>
    </tr>
	<tr>
		<td>test_status_code_invalid_request</td>
		<td>Checks the response status code for an invalid request</td>
	</tr>
</table>

### 8. test_get_list.py
#### This test file contains methods to test the retrieval of expense lists.

#### Test Methods:

<table>
    <tr>
        <th>Methods</th>
        <th>Description</th>
    </tr>
    <tr>
        <td>test_status_code</td>
        <td>Checks the response status code after getting the expense list</td>
    </tr>
    <tr>
        <td>test_expenses_count</td>
        <td>Checks the count of expenses in the list</td>
    </tr>
	<tr>
		<td>test_json_tokens</td>
		<td>Checks JSON tokens in the response</td>
	</tr>
	<tr>
		<td>test_limit_normal</td>
		<td>Checks the response when the limit is between 0 and total_count</td>
	</tr>
	<tr>
		<td>test_limit_0</td>
		<td>Checks the response when the limit is 0</td>
	</tr>
	<tr>
		<td>test_limit_total</td>
		<td>Checks the response when the limit is total_count</td>
	</tr>
	<tr>
		<td>test_json_tokens</td>
		<td>Checks JSON tokens in the response</td>
	</tr>
	<tr>
		<td>test_limit_more</td>
		<td>Checks the response when the limit is greater than total_count</td>
	</tr>
	<tr>
		<td>test_limit_negative</td>
		<td>Checks the response when the limit is negative</td>
	</tr>
	<tr>
		<td>test_limit_less_negative_total</td>
		<td>Checks the response when the limit is less than negative total_count</td>
	</tr>
	<tr>
		<td>test_limit_total</td>
		<td>Checks the response when the limit is total_count</td>
	</tr>
	<tr>
		<td>test_offset_normal</td>
		<td>Checks the response when the offset is between 0 and total_count</td>
	</tr>
	<tr>
		<td>test_offset_0</td>
		<td>Checks the response when the offset is 0</td>
	</tr>
	<tr>
		<td>test_offset_equal_total</td>
		<td>Checks the response when the offset is equal to total_count</td>
	</tr>
	<tr>
		<td>test_offset_more_total</td>
		<td>Checks the response when the offset is greater than total_count</td>
	</tr>
	<tr>
		<td>test_offset_negative</td>
		<td>Checks the response when the offset is negative</td>
	</tr>
</table>

### 9. test_summary_expense.py
#### This test file contains methods to test the retrieval of expense summaries.

#### Test Methods:

<table>
    <tr>
        <th>Methods</th>
        <th>Description</th>
    </tr>
    <tr>
        <td>test_status_code</td>
        <td>Checks the response status code after getting the summary</td>
    </tr>
    <tr>
        <td>test_summary_tokens</td>
        <td>Checks JSON tokens in the response</td>
    </tr>
	<tr>
		<td>test_summary_num_transactions</td>
		<td>Checks if num_transactions is equal to the total_count</td>
	</tr>
	<tr>
		<td>test_summary_total_value</td>
		<td>Checks if the total sum is correct</td>
	</tr>
</table>

### 10. test_update_expense.py
#### This test file contains methods to test the update of expense entries.

#### Test Methods:


<table>
    <tr>
        <th>Methods</th>
        <th>Description</th>
    </tr>
    <tr>
        <td>test_status_code</td>
        <td>Checks the response status code after updating an expense</td>
    </tr>
    <tr>
        <td>test_expenses_values</td>
        <td>Checks if the received UID, amount, category, and description match the expected values</td>
    </tr>
	<tr>
		<td>test_expenses_nonexistent_uid</td>
		<td>Checks the response status code for updating an expense with a nonexistent UID</td>
	</tr>
	<tr>
		<td>test_expenses_tokens_nonexistent_uid</td>
		<td>Checks tokens for updating an expense with a nonexistent UID</td>
	</tr>
    <tr>
        <td>test_status_code_invalid_request</td>
        <td>Checks the response status code for an invalid request</td>
    </tr>
    <tr>
        <td>test_expenses_tokens_invalid_request</td>
        <td>Checks if the received UID, amount, category, and description match the expected values</td>
    </tr>
	<tr>
		<td>test_expenses_nonexistent_uid</td>
		<td>Checks tokens for an invalid request</td>
	</tr>
	<tr>
		<td>test_status_code_invalid_json</td>
		<td>Checks the response status code for an invalid JSON in the request</td>
	</tr>
</table>

## Explanation of .log Files
The .log files contain logs generated during the execution of the tests. These logs capture information and errors, providing insights into the test execution process. The log files are named based on their purpose or the test file they correspond to. Log files are helpful for debugging and understanding the flow of test execution.


## Load Testing
Conduct comprehensive load testing for your expense management system using the auto-generated load-test.js script in the load_test directory. Execute the script with k6 to simulate various user scenarios, analyze key metrics like request success rate and iteration duration, and iteratively optimize system performance based on the results.
For detailed instructions on running the test, refer to the load_test/readme.md file.






