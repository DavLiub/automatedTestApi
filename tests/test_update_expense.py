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
        print("\nStart test 'update expense'")
        print("\nStep 1. Send valid request for getting full list")
        result_get_expense = Open_api_expense.get_expense_list(0, 0)
        print("\nStep 2. Chose random entry from list and getting expense_uid")
        check_data = result_get_expense.json()
        current_count = check_data["meta"]["current_count"]
        expense_uid = check_data["expenses"][random.randint(0, current_count-1)]["uid"]
        print("\nStep 3. Checking response status code")
        result_update = Open_api_expense.put_update_expense(expense_uid, json_for_update_expense)
        Checking.check_status_code(result_update, 200)  # Expected status code: 200 Created

    @allure.description("VALID request => Checking received values uid, amount, category, description")
    def test_expenses_values(self):
        print("\nStart test 'get expense'")
        print("\nStep 1. Send valid request for getting full list")
        result_get_expense = Open_api_expense.get_expense_list(0, 0)
        print("\nStep 2. Chose random entry from list and getting expense_uid")
        check_data = result_get_expense.json()
        current_count = check_data["meta"]["current_count"]
        expense_uid = check_data["expenses"][random.randint(0, current_count-1)]["uid"]
        print("\nStep 3. Checking response uid")
        result_update = Open_api_expense.put_update_expense(expense_uid, json_for_update_expense)
        check_data = result_update.json()
        assert check_data["expense"]["uid"] == expense_uid
        print("\nSuccess! Received correct entry")
        print("\nStep 4. Checking response amount")
        assert check_data["expense"]["amount"] == json_for_update_expense.get("amount")
        print("\nSuccess! Amount was updated")
        print("\nStep 5. Checking response category")
        assert check_data["expense"]["category"] == json_for_update_expense.get("category")
        print("\nSuccess! Category was updated")
        print("\nStep 6. Checking response description")
        assert check_data["expense"]["description"] == json_for_update_expense.get("description")
        print("\nSuccess! Description was updated")

    @allure.description("VALID request => Checking status code if nonexistent uid")
    def test_expenses_nonexistent_uid(self):
        print("\nStart test 'get expense'")
        print("\nStep 1. Send valid request (expense_uid = 333)")
        result_update = Open_api_expense.put_update_expense("333", json_for_update_expense)
        print("\nStep 2. Checking response status code")
        Checking.check_status_code(result_update, 404)

    @allure.description("VALID request => Checking tokens if nonexistent uid")
    def test_expenses_tokens_nonexistent_uid(self):
        print("\nStart test 'get expense'")
        print("\nStep 1. Send valid request (expense_uid = 333)")
        result_update = Open_api_expense.put_update_expense("333", json_for_update_expense)
        print("\nStep 2. Checking response tokens")
        Checking.check_json_token(result_update, ['message', 'status', 'description'])

    @allure.description("INVALID request => Checking response status code")
    def test_status_code_invalid_request(self):
        print("\nStart test 'update expense' without body")
        print("\nStep 1. Send valid request for getting full list")
        result_get_expense = Open_api_expense.get_expense_list(0, 0)
        print("\nStep 2. Chose random entry from list and getting expense_uid")
        check_data = result_get_expense.json()
        current_count = check_data["meta"]["current_count"]
        print("\nStep 3. Send invalid request (body=None)")
        expense_uid = check_data["expenses"][random.randint(0, current_count-1)]["uid"]
        result_update = Open_api_expense.put_update_expense(expense_uid, None)
        print("\nStep 4. Checking response status code")
        Checking.check_status_code(result_update, 400)  # Expected status code: 400 Bad Request

    @allure.description("INVALID request => Checking received tokens")
    def test_expenses_tokens_invalid_request(self):
        print("\nStart test 'get expense'")
        print("\nStep 1. Send valid request for getting full list")
        result_get_expense = Open_api_expense.get_expense_list(0, 0)
        print("\nStep 2. Chose random entry from list and getting expense_uid")
        check_data = result_get_expense.json()
        current_count = check_data["meta"]["current_count"]
        expense_uid = check_data["expenses"][random.randint(0, current_count-1)]["uid"]
        print("\nStep 3. Send invalid request (body=None")
        result_update = Open_api_expense.put_update_expense(expense_uid, None)
        check_data = result_update.json()
        result_update = Open_api_expense.put_update_expense("333", json_for_update_expense)
        print("\nStep 4. Checking response tokens")
        Checking.check_json_token(result_update, ['message', 'status', 'description'])

    @allure.description("INVALID request => Checking response status code")
    def test_status_code_invalid_json(self):
        bad_json = {
            "amount": "157",
            "category": 0&5,
            "description": "changed"
        }
        print("\nStart test 'update expense' with incorrect json data")
        print("\nStep 1. Send valid request for getting full list")
        result_get_expense = Open_api_expense.get_expense_list(0, 0)
        print("\nStep 2. Chose random entry from list and getting expense_uid")
        check_data = result_get_expense.json()
        current_count = check_data["meta"]["current_count"]
        print("\nStep 3. Send invalid request (bad json)")
        expense_uid = check_data["expenses"][random.randint(0, current_count-1)]["uid"]
        result_update = Open_api_expense.put_update_expense(expense_uid, bad_json)
        print("\nStep 4. Checking response status code")
        Checking.check_status_code(result_update, 400)  # Expected status code: 400 Bad Request
