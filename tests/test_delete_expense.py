import json
import random
import allure
from utils.checking import Checking
from utils.api import Open_api_expense

""" Update expense """


@allure.epic("Delete expense method [Delete] v1/expense/{expense_uid}}")
class Test_delete_expense():
    @allure.description("VALID request => Checking response status code")
    def test_status_code(self):
        """
        Test the deletion of an expense and check the response status code.

        Steps:
        1. Send a valid request to get the full expense list.
        2. Get a random UID from the list.
        3. Send a valid request to delete the entry with the selected UID.
        4. Check if the status code of the response is 204 (No Content).
        5. Send a valid request to get the full expense list.
        6. Check that the entry with the specified UID was deleted.
        """
        expense_uid = Open_api_expense.get_random_expense_uid()
        result_delete = Open_api_expense.delete_expense(expense_uid)
        Checking.check_status_code(result_delete, 204)  # Expected status code: 204 Deleted

        result_get_list = Open_api_expense.get_expense_list(0, 0)
        check_data = result_get_list.json()
        assert expense_uid not in [entry["uid"] for entry in check_data["expenses"]]

    @allure.description("VALID request => Checking status code if nonexistent uid")
    def test_delete_nonexistent_uid(self):
        """
        Test the deletion of an expense with a nonexistent UID.

        Steps:
        1. Send a valid request to delete an entry with UID = "333" (nonexistent UID).
        2. Check if the status code of the response is 404 (Not Found).
        """
        result_delete = Open_api_expense.delete_expense("333")
        Checking.check_status_code(result_delete, 404)  # Expected status code: 404 Not Found

    @allure.description("VALID request => Checking tokens if nonexistent uid")
    def test_expenses_tokens_nonexistent_uid(self):
        """
        Test the deletion of an expense with a nonexistent UID and check the error tokens.

        Steps:
        1. Send a valid request to delete an entry with UID = "333" (nonexistent UID).
        2. Check if the response contains the expected error tokens: ['message', 'status', 'description'].
        """
        result_delete = Open_api_expense.delete_expense("333")
        Checking.check_json_token(result_delete, ['message', 'status', 'description'])
