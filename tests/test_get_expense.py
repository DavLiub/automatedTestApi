import json
import random
import allure
from utils.checking import Checking
from utils.api import Open_api_expense

""" Update expense """



@allure.epic("Get expense method [GET] v1/expense/{expense_uid}}")
class Test_get_expense():
    @allure.description("VALID request => Checking response status code")
    def test_status_code(self):
        print("\n")
        print("|-------------------------------------------------|")
        print("|        [GET] v1/expense/{expense_uid}}          |")
        print("|          Start test validation Tokens           |")
        print("|                  (valid request)                |")
        print("|-------------------------------------------------|\n")
        print("Previous steps:\n\tSend request get list\n\tGet random UID from list")
        expense_uid = Open_api_expense.get_random_expense_uid()
        print(f"1. Send request with uid = {expense_uid}")
        result_get_list = Open_api_expense.get_expense_by_uid(expense_uid)
        print("3. Checking status code=200")
        Checking.check_status_code(result_get_list, 200)  # Expected status code: 200 Created

    @allure.description("VALID request => Checking response entry uid")
    def test_expenses_count(self):
        print("\n")
        print("|-------------------------------------------------|")
        print("|        [GET] v1/expense/{expense_uid}}          |")
        print("|           Start test validation UID             |")
        print("|                  (valid request)                |")
        print("|-------------------------------------------------|\n")
        print("Previous steps:\n\tSend request get list\n\tGet random UID from list")
        expense_uid = Open_api_expense.get_random_expense_uid()
        print(f"1. Send request with uid = {expense_uid}")
        result_get_expense = Open_api_expense.get_expense_by_uid(expense_uid)
        print("2. Checking response entry uid")
        check_data = result_get_expense.json()
        assert check_data["expense"]["uid"] == expense_uid
        print("Success! Received correct entry")

    @allure.description("VALID request => Checking received tokes")
    def test_expenses_tokens(self):
        print("\n")
        print("|-------------------------------------------------|")
        print("|        [GET] v1/expense/{expense_uid}}          |")
        print("|          Start test validation Tokens           |")
        print("|                  (valid request)                |")
        print("|-------------------------------------------------|\n")
        print("Previous steps:\n\tSend request get list\n\tGet random UID from list")
        expense_uid = Open_api_expense.get_random_expense_uid()
        print(f"1. Send request with uid = {expense_uid}")
        result_get_expense = Open_api_expense.get_expense_by_uid(expense_uid)
        print("2. Checking tokens = ['amount', 'category', 'description', 'id', 'uid', 'created_at']")
        token =json.loads(result_get_expense.text)
        token_keys = list(token["expense"].keys())
        assert token_keys == ['amount', 'category', 'description', 'id', 'uid', 'created_at']
        print("Success! All tokens are on their places")


    @allure.description("VALID request => Checking status code if nonexistent uid")
    def test_expenses_nonexistent_uid(self):
        print("\n")
        print("|-------------------------------------------------|")
        print("|        [GET] v1/expense/{expense_uid}}          |")
        print("|       Start test validation Status code         |")
        print("|   (valid request - nonexistent uid expense)     |")
        print("|-------------------------------------------------|\n")
        print("1. Send valid request (expense_uid = 333)")
        result_get_expense = Open_api_expense.get_expense_by_uid("333")
        print("2. Checking status code = 404")
        Checking.check_status_code(result_get_expense, 404)

    @allure.description("VALID request => Checking tokens if nonexistent uid")
    def test_expenses_tokens_nonexistent_uid(self):
        print("\n")
        print("|-------------------------------------------------|")
        print("|        [GET] v1/expense/{expense_uid}}          |")
        print("|          Start test validation Tokens           |")
        print("|   (valid request - nonexistent uid expense)     |")
        print("|-------------------------------------------------|\n")
        print("1. Send valid request (expense_uid = 333)")
        result_get_expense = Open_api_expense.get_expense_by_uid("333")
        print("2. Checking tokens = ['message', 'status', 'description']")
        Checking.check_json_token(result_get_expense, ['message', 'status', 'description'])

