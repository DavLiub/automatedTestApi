import json
import random
import allure
from utils.checking import Checking
from utils.api import Open_api_expense

json_for_update_expense = {
  "amount": "100",
  "category": "changed"+str(random.randint(1,100)),
  "description": "changed"+str(random.randint(1,100))
}

""" Update expense """

@allure.epic("Update expense method [PUT] v1/expense")
class Test_update_expense():
    @allure.description("VALID request => Checking response status code")
    def test_status_code(self):
        """
        Test a valid PUT request to update an expense entry and check the response status code.

        Steps:
        1. Send a valid GET request to get the full expense list.
        2. Choose a random entry from the list and get the expense UID.
        3. Send a valid PUT request to update the expense entry with the selected UID.
        4. Check if the status code of the response is 200 (OK).
        """
        result_get_expense = Open_api_expense.get_expense_list(0, 0)
        check_data = result_get_expense.json()
        current_count = check_data["meta"]["current_count"]
        expense_uid = check_data["expenses"][random.randint(0, current_count-1)]["uid"]
        result_update = Open_api_expense.put_update_expense(expense_uid, json_for_update_expense)
        Checking.check_status_code(result_update, 200)  # Expected status code: 200 OK

    @allure.description("VALID request => Checking received values uid, amount, category, description")
    def test_expenses_values(self):
        """
        Test a valid PUT request to update an expense entry and check the received values.

        Steps:
        1. Send a valid GET request to get the full expense list.
        2. Choose a random entry from the list and get the expense UID.
        3. Send a valid PUT request to update the expense entry with the selected UID.
        4. Check if the received UID, amount, category, and description match the expected values.
        """
        result_get_expense = Open_api_expense.get_expense_list(0, 0)
        check_data = result_get_expense.json()
        current_count = check_data["meta"]["current_count"]
        expense_uid = check_data["expenses"][random.randint(0, current_count-1)]["uid"]
        result_update = Open_api_expense.put_update_expense(expense_uid, json_for_update_expense)
        check_data = result_update.json()
        assert check_data["expense"]["uid"] == expense_uid
        print("\nSuccess! Received correct entry")
        assert check_data["expense"]["amount"] == json_for_update_expense.get("amount")
        print("\nSuccess! Amount was updated")
        assert check_data["expense"]["category"] == json_for_update_expense.get("category")
        print("\nSuccess! Category was updated")
        assert check_data["expense"]["description"] == json_for_update_expense.get("description")
        print("\nSuccess! Description was updated")

    @allure.description("VALID request => Checking status code for nonexistent uid")
    def test_expenses_nonexistent_uid(self):
        """
        Test a valid PUT request to update an expense entry with a nonexistent UID and check the response status code.

        Steps:
        1. Send a valid PUT request to update the expense entry with UID = "333" (nonexistent UID).
        2. Check if the status code of the response is 404 (Not Found).
        """
        result_update = Open_api_expense.put_update_expense("333", json_for_update_expense)
        Checking.check_status_code(result_update, 404)

    @allure.description("VALID request => Checking tokens for nonexistent uid")
    def test_expenses_tokens_nonexistent_uid(self):
        """
        Test a valid PUT request to update an expense entry with a nonexistent UID and check the error tokens.

        Steps:
        1. Send a valid PUT request to update the expense entry with UID = "333" (nonexistent UID).
        2. Check if the response contains the expected error tokens: ['message', 'status', 'description'].
        """
        result_update = Open_api_expense.put_update_expense("333", json_for_update_expense)
        Checking.check_json_token(result_update, ['message', 'status', 'description'])

    @allure.description("INVALID request => Checking response status code")
    def test_status_code_invalid_request(self):
        """
        Test an invalid PUT request without a body and check the response status code.

        Steps:
        1. Send a valid GET request to get the full expense list.
        2. Choose a random entry from the list and get the expense UID.
        3. Send an invalid PUT request (body=None).
        4. Check if the status code of the response is 400 (Bad Request).
        """
        result_get_expense = Open_api_expense.get_expense_list(0, 0)
        check_data = result_get_expense.json()
        current_count = check_data["meta"]["current_count"]
        expense_uid = check_data["expenses"][random.randint(0, current_count-1)]["uid"]
        result_update = Open_api_expense.put_update_expense(expense_uid, None)
        Checking.check_status_code(result_update, 400)  # Expected status code: 400 Bad Request

    @allure.description("INVALID request => Checking received tokens")
    def test_expenses_tokens_invalid_request(self):
        """
        Test an invalid PUT request without a body and check the error tokens.

        Steps:
        1. Send a valid GET request to get the full expense list.
        2. Choose a random entry from the list and get the expense UID.
        3. Send an invalid PUT request (body=None).
        4. Check if the response contains the expected error tokens: ['message', 'status', 'description'].
        """
        result_get_expense = Open_api_expense.get_expense_list(0, 0)
        check_data = result_get_expense.json()
        current_count = check_data["meta"]["current_count"]
        expense_uid = check_data["expenses"][random.randint(0, current_count-1)]["uid"]
        result_update = Open_api_expense.put_update_expense(expense_uid, None)
        Checking.check_json_token(result_update, ['message', 'status', 'description'])

    @allure.description("INVALID request => Checking response status code")
    def test_status_code_invalid_json(self):
        """
        Test an invalid PUT request with incorrect JSON data and check the response status code.

        Steps:
        1. Send a valid GET request to get the full expense list.
        2. Choose a random entry from the list and get the expense UID.
        3. Send an invalid PUT request with bad JSON data.
        4. Check if the status code of the response is 400 (Bad Request).
        """
        bad_json = {
            "amount": "157",
            "category": 0&5,
            "description": "changed"
        }
        result_get_expense = Open_api_expense.get_expense_list(0, 0)
        check_data = result_get_expense.json()
        current_count = check_data["meta"]["current_count"]
        expense_uid = check_data["expenses"][random.randint(0, current_count-1)]["uid"]
        result_update = Open_api_expense.put_update_expense(expense_uid, bad_json)
        Checking.check_status_code(result_update, 400)  # Expected status code: 400 Bad Request
