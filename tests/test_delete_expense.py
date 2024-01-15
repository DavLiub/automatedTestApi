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
        print("\n")
        print("|-------------------------------------------------|")
        print("|       Start test validation Status code         |")
        print("|                 (valid request)                 |")
        print("|-------------------------------------------------|\n")
        print("Previous steps:\n\tSend request get list\n\tGet random UID from list")
        expense_uid = Open_api_expense.get_random_expense_uid()
        print("1. Send valid request for delete entry uid="+expense_uid)
        result_delete = Open_api_expense.delete_expense(expense_uid)
        print("2. Checking status code = 200")
        Checking.check_status_code(result_delete, 204)  # Expected status code: 204 Deleted
        print("3. Send valid request for getting full list")
        result_get_list = Open_api_expense.get_expense_list(0, 0)
        print(f"4. Checking that entry with uid={expense_uid} was deleted")
        check_data = result_get_list.json()
        flag = 0
        for i in range(0, check_data["meta"]["current_count"]-1):
            if expense_uid == check_data["expenses"][i]["uid"]:
                flag = 1
        assert flag == 0
        print("Success! Entry was deleted")


    @allure.description("VALID request => Checking status code if nonexistent uid")
    def test_delete_nonexistent_uid(self):
        print("\n")
        print("|-------------------------------------------------|")
        print("|       Start test validation Status code         |")
        print("|   (valid request - nonexistent uid expense)     |")
        print("|-------------------------------------------------|\n")
        print("1. Send valid request (expense_uid = 333)")
        result_delete = Open_api_expense.delete_expense("333")
        print("2. Checking status code = 404")
        Checking.check_status_code(result_delete, 404)     # Expected status code: 404 Not Found

    @allure.description("VALID request => Checking tokens if nonexistent uid")
    def test_expenses_tokens_nonexistent_uid(self):
        print("\n")
        print("|-------------------------------------------------|")
        print("|          Start test validation Tokens           |")
        print("|   (valid request - nonexistent uid expense)     |")
        print("|-------------------------------------------------|\n")
        print("1. Send valid request (expense_uid = 333)")
        result_delete = Open_api_expense.delete_expense("333")
        print("2. Checking tokens = ['message', 'status', 'description']")
        Checking.check_json_token(result_delete, ['message', 'status', 'description'])

