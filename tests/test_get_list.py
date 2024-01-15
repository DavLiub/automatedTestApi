import random
import allure
from utils.checking import Checking
from utils.api import Open_api_expense


""" Getting expense list"""

@allure.epic("Get expense method [GET] v1/expense (without options)")
class Test_get_expense_list_valid_request():
    @allure.description("VALID request => Checking response status code")
    def test_status_code(self):
        print("\n")
        print("|-------------------------------------------------|")
        print("|    Start test [GET] v1/expense                  |")
        print("|    (valid request - without options)            |")
        print("|-------------------------------------------------|\n")
        print(">>> Test validation Status code")
        print("1. Send valid request")
        result_get_list = Open_api_expense.get_expense_list()
        print("2. Checking status code = 200")
        Checking.check_status_code(result_get_list, 200)  # Expected status code: 200 Created

    @allure.description("VALID request => Checking expenses count in list")
    def test_expenses_count(self):
        print(">>> Test validation Count entries")
        print("1. Send valid request")
        result_get_list = Open_api_expense.get_expense_list()
        check_data = result_get_list.json()
        expected_count = check_data["meta"]["total_count"]
        if expected_count > check_data["meta"]["limit"]:
            expected_count = check_data["meta"]["limit"]
        expense_count = len(check_data["expenses"])
        print("2. Checking expenses count in list")
        assert expense_count == expected_count
        print("Success! In list is correct value of expense entries ")

    @allure.description("VALID request (without options) tokens")
    def test_json_tokens(self):
        print(">>> Test validation Tokens")
        print("1. Send valid request")
        result_get_list = Open_api_expense.get_expense_list()
        print("2. Checking tokens = ['expenses', 'meta']")
        Checking.check_json_token(result_get_list, ['expenses', 'meta'])

@allure.epic("Get expense method [GET] v1/expense (with parameter limit)")
class Test_get_expense_list_limit():
    @allure.description("Checking when limit between 0 and total_count")
    def test_limit_normal(self):
        print("\n")
        print("|------------------------------------------------------|")
        print("|    Start test [GET] v1/expense                       |")
        print("|    (valid request - with parameter limit)            |")
        print("|------------------------------------------------------|\n")
        print(">>> Test with limit between 0 and total_count'")
        print("1. Send valid request (limit = 1")
        limit = 1
        result_get_list = Open_api_expense.get_expense_list(limit=limit)
        print("2. Checking status code = 200")
        Checking.check_status_code(result_get_list, 200)
        print("3. Checking current_count and expenses_count")
        check_data = result_get_list.json()
        current_count = check_data["meta"]["current_count"]
        expense_count = len(check_data["expenses"])
        assert current_count == limit
        print("Success! Parameter current_count = limit")
        assert expense_count == limit
        print("Success! Count of expenses in list = limit")

    @allure.description("Checking when limit = 0 ")
    def test_limit_0(self):
        print(">>> Test with limit = 0")
        print("1. Send valid request (limit = 0")
        result_get_list = Open_api_expense.get_expense_list(limit=0)
        check_data = result_get_list.json()
        print("2. Get total_count, current_count and really count of entries for compare")
        total_count = check_data["meta"]["total_count"]
        current_count = check_data["meta"]["current_count"]
        expense_count = len(check_data["expenses"])
        print("3. Checking current_count = total_count")
        # Expected values of current_count and expenses_count = total_count
        assert current_count == total_count
        print("4. Checking expenses_count = current_count")
        assert expense_count == current_count
        print("Success! Count parameters are correct")

    @allure.description("Checking when limit = total_count ")
    def test_limit_total(self):
        print(">>> Test with limit = total_count '")
        print("Previous steps:\n\t- send valid request\n\t- get total_count")
        limit = Open_api_expense.get_total_count_from_list()
        print("1. Send valid request (limit = total_count + 10")
        result_get_list = Open_api_expense.get_expense_list(limit=limit)
        print("2. Get total_count, current_count and really count of entries for compare")
        check_data = result_get_list.json()
        total_count = check_data["meta"]["total_count"]
        current_count = check_data["meta"]["current_count"]
        expense_count = len(check_data["expenses"])
        print("3. Checking current_count = total_count")
        # Expected values of current_count and expenses_count = total_count
        assert current_count == total_count
        print("4. Checking expenses_count = current_count")
        assert expense_count == current_count
        print("Success! Count parameters are correct")

    @allure.description("Checking when limit > total_count")
    def test_limit_more(self):
        print(">>> Test with limit > total_count")
        print("Previous steps:\n\t- send valid request\n\t- get total_count")
        limit = Open_api_expense.get_total_count_from_list() + 10
        print("1. Send valid request (limit = total_count + 10")
        result_get_list = Open_api_expense.get_expense_list(limit=limit)
        print("2. Get total_count, current_count and really count of entries for compare")
        check_data = result_get_list.json()
        total_count = check_data["meta"]["total_count"]
        current_count = check_data["meta"]["current_count"]
        expense_count = len(check_data["expenses"])
        print("3. Checking current_count = total_count")
        # Expected values of current_count and expenses_count = total_count
        assert current_count == total_count
        print("4. Checking expenses_count = current_count")
        assert expense_count == current_count
        print("Success! Count parameters are correct")

    @allure.description("Checking when limit < 0")
    def test_limit_negotive(self):
        print(">>> Test with limit < 0")
        print("1. Send valid request (limit = -2")
        limit = -2
        result_get_list = Open_api_expense.get_expense_list(limit=limit)
        print("2. Get total_count, current_count and really count of entries for compare")
        check_data = result_get_list.json()
        current_count = check_data["meta"]["current_count"]
        expense_count = len(check_data["expenses"])
        expected_count = check_data["meta"]["total_count"] + limit
        print("3. Checking current_count = total_count - |limit|")
        # Expected values of current_count and expenses_count = total_count - |limit|
        assert current_count == expected_count
        print("4. Checking expenses_count = current_count")
        assert expense_count == current_count
        print("Success! Count parameters are correct")

    @allure.description("Checking when limit < -total_count")
    def test_limit_less_negotive_total(self):
        print("\nStart test 'get expense list with limit > total_count '")
        print("Previous steps:\n\t- send valid request\n\t- get total_count")
        limit = -Open_api_expense.get_total_count_from_list() - 10
        print("1. Send valid request (limit = -total_count - 10")
        result_get_list = Open_api_expense.get_expense_list(limit=limit)
        print("2. Get current_count and really count of entries for compare")
        check_data = result_get_list.json()
        current_count = check_data["meta"]["current_count"]
        expense_count = len(check_data["expenses"])
        print("3. Checking current_count = 0")
        # Expected values of current_count and expenses_count = 0
        assert current_count == 0
        print("3. Checking expenses_count = current_count")
        assert expense_count == current_count
        print("Success! Count of expenses in list = current_count")

@allure.epic("Get expense method [GET] v1/expense (with parameter offset)")
class Test_get_expense_list_offset():

    @allure.description("Checking when offset between 0 and total_count")
    def test_offset_normal(self):
        print("\n")
        print("|------------------------------------------------------|")
        print("|    Start test [GET] v1/expense                       |")
        print("|    (valid request - with parameter offset            |")
        print("|------------------------------------------------------|\n")
        print(">>> Test with offset between 0 and total_count '")
        print("1. Send valid request (offset = 0, limit =0)")                # to get full list
        result_get_list = Open_api_expense.get_expense_list(0, 0)
        check_data = result_get_list.json()
        total_count = check_data["meta"]["total_count"]
        offset = random.randint(1, total_count-1)
        expense_uid_expected = check_data["expenses"][offset]["uid"]                      # get expense uid with will be on 0 position
        print("2. Checking status code = 200")
        Checking.check_status_code(result_get_list, 200)                        # Expected status code: 200 Created
        print(f"3. Send valid request (offset = {offset}")
        result_get_list = Open_api_expense.get_expense_list(offset=offset)
        print(f"4. Checking list started from expense with expense {offset}")
        check_data = result_get_list.json()
        assert check_data["expenses"][0]["uid"] == expense_uid_expected
        print("Success! List started from number of record = offset")

    @allure.description("Checking when offset = 0")
    def test_offset_0(self):
        print(">>> Test with offset = 0 '")
        print("1. Send valid request (offset = 0, limit 0)")                # to get full list
        result_get_list = Open_api_expense.get_expense_list(0, 0)
        check_data = result_get_list.json()
        total_count = check_data["meta"]["total_count"]
        current_count = check_data["meta"]["current_count"]
        print("2. Checking that list is full (current_count = total_count)")
        assert current_count == total_count
        print("Success! List is full and started from entry #0")

    @allure.description("Checking when offset = total_count")
    def test_offset_equal_total(self):
        print(">>> Test with offset = total_count '")
        print("Previous steps:\n\t- send valid request\n\t- get total_count")
        offset = Open_api_expense.get_total_count_from_list()
        print("1. Send valid request (offset = total_current)")
        result_get_list = Open_api_expense.get_expense_list(offset=offset)
        print("2. Checking is list empty")
        check_data = result_get_list.json()
        assert check_data["expenses"] == []
        print("Success! List is empty")

    @allure.description("Checking when offset > total_count")
    def test_offset_more_total(self):
        print(">>> Test with offset > total_count '")
        print("Previous steps:\n\t- send valid request\n\t- get total_count")
        offset = Open_api_expense.get_total_count_from_list() + 10
        print("2. Send valid request (offset > total_current)")
        result_get_list = Open_api_expense.get_expense_list(offset=offset)
        print("3. Checking is list empty")
        check_data = result_get_list.json()
        assert check_data["expenses"] == []
        print("Success! List is empty")

    @allure.description("Checking when offset < 0")
    def test_offset_negative(self):
        print(">>> Test with offset < 0>")
        offset = -4
        print("1. Send valid request (offset = -4)")
        result_get_list = Open_api_expense.get_expense_list(offset=offset)
        print("2. Checking is list empty")
        check_data = result_get_list.json()
        assert check_data["expenses"] == []
        print("Success! List is empty")

@allure.epic("Get expense method [GET] v1/expense (Invalid options)")
class Test_get_expense_list_invalid_request():
    @allure.description("INVALID request => Checking response status code")
    def test_status_code(self):
        print("\n")
        print("|------------------------------------------------------|")
        print("|    Start test [GET] v1/expense                       |")
        print("|    (invalid request                      )           |")
        print("|------------------------------------------------------|\n")
        print("1. Send invalid request (limit is float")
        result_get_list = Open_api_expense.get_expense_list(limit=5.4)
        print("2. Checking status code = 500")
        Checking.check_status_code(result_get_list, 500)  # Expected status code: 500 Internal Server Error

        print("3. Send invalid request (limit is string")
        result_get_list = Open_api_expense.get_expense_list(limit="5a4")
        print("4. Checking status code = 500")
        Checking.check_status_code(result_get_list, 500)  # Expected status code: 500 Internal Server Error

        print("5. Send invalid request (offset is float")
        result_get_list = Open_api_expense.get_expense_list(offset=5.4)
        print("6. Checking status code = 500")
        Checking.check_status_code(result_get_list, 500)  # Expected status code: 500 Internal Server Error

        print("7. Send invalid request (offset is string")
        result_get_list = Open_api_expense.get_expense_list(offset="5a4")
        print("8. Checking status code = 500")
        Checking.check_status_code(result_get_list, 500)  # Expected status code: 500 Internal Server Error

