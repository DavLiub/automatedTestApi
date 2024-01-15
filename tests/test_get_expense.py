import json
import random
import allure
from utils.checking import Checking
from utils.api import Open_api_expense

""" GET expense """


@allure.epic("Get expense method [GET] v1/expense/{expense_uid}}")
class Test_get_expense():
    @allure.description("VALID request => Checking response status code")
    def test_status_code(self):
        """
        Test a valid GET request for an expense entry and check the response status code.

        Steps:
        1. Send a request to get the full expense list.
        2. Get a random UID from the list.
        3. Send a valid GET request for the expense entry with the selected UID.
        4. Check if the status code of the response is 200 (OK).
        """
        expense_uid = Open_api_expense.get_random_expense_uid()
        result_get_list = Open_api_expense.get_expense_by_uid(expense_uid)
        Checking.check_status_code(result_get_list, 200)  # Expected status code: 200 OK

    @allure.description("VALID request => Checking response entry uid")
    def test_expenses_count(self):
        """
        Test a valid GET request for an expense entry and check the received UID.

        Steps:
        1. Send a request to get the full expense list.
        2. Get a random UID from the list.
        3. Send a valid GET request for the expense entry with the selected UID.
        4. Check if the received entry UID matches the selected UID.
        """
        expense_uid = Open_api_expense.get_random_expense_uid()
        result_get_expense = Open_api_expense.get_expense_by_uid(expense_uid)
        check_data = result_get_expense.json()
        assert check_data["expense"]["uid"] == expense_uid
        print("Success! Received correct entry")

    @allure.description("VALID request => Checking received tokens")
    def test_expenses_tokens(self):
        """
        Test a valid GET request for an expense entry and check the received tokens.

        Steps:
        1. Send a request to get the full expense list.
        2. Get a random UID from the list.
        3. Send a valid GET request for the expense entry with the selected UID.
        4. Check if the received tokens match the expected tokens:
           ['amount', 'category', 'description', 'id', 'uid', 'created_at'].
        """
        expense_uid = Open_api_expense.get_random_expense_uid()
        result_get_expense = Open_api_expense.get_expense_by_uid(expense_uid)
        token = json.loads(result_get_expense.text)
        token_keys = list(token["expense"].keys())
        assert token_keys == ['amount', 'category', 'description', 'id', 'uid', 'created_at']
        print("Success! All tokens are in their places")

    @allure.description("VALID request => Checking status code for nonexistent uid")
    def test_expenses_nonexistent_uid(self):
        """
        Test a valid GET request for an expense entry with a nonexistent UID and check the response status code.

        Steps:
        1. Send a valid GET request for the expense entry with UID = "333" (nonexistent UID).
        2. Check if the status code of the response is 404 (Not Found).
        """
        result_get_expense = Open_api_expense.get_expense_by_uid("333")
        Checking.check_status_code(result_get_expense, 404)

    @allure.description("VALID request => Checking tokens for nonexistent uid")
    def test_expenses_tokens_nonexistent_uid(self):
        """
        Test a valid GET request for an expense entry with a nonexistent UID and check the error tokens.

        Steps:
        1. Send a valid GET request for the expense entry with UID = "333" (nonexistent UID).
        2. Check if the response contains the expected error tokens: ['message', 'status', 'description'].
        """
        result_get_expense = Open_api_expense.get_expense_by_uid("333")
        Checking.check_json_token(result_get_expense, ['message', 'status', 'description'])
