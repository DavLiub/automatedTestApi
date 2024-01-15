import random
import allure
from utils.checking import Checking
from utils.api import Open_api_expense


""" Getting expense list"""

@allure.epic("Get expense method [GET] v1/expense (without options)")
class Test_get_expense_list_valid_request():
    @allure.description("VALID request => Checking response status code")
    def test_status_code(self):
        """
        Test validation Status code.
        1. Send valid request.
        2. Checking status code = 200.
        """
        result_get_list = Open_api_expense.get_expense_list()
        Checking.check_status_code(result_get_list, 200)  # Expected status code: 200 Created

    @allure.description("VALID request => Checking expenses count in list")
    def test_expenses_count(self):
        """
        Test validation Count entries.
        1. Send valid request.
        2. Checking expenses count in the list.
        """
        result_get_list = Open_api_expense.get_expense_list()
        check_data = result_get_list.json()
        expected_count = check_data["meta"]["total_count"]
        if expected_count > check_data["meta"]["limit"]:
            expected_count = check_data["meta"]["limit"]
        expense_count = len(check_data["expenses"])
        assert expense_count == expected_count
        print("Success! In the list is the correct value of expense entries.")

    @allure.description("VALID request (without options) tokens")
    def test_json_tokens(self):
        """
        Test validation Tokens.
        1. Send valid request.
        2. Checking tokens = ['expenses', 'meta'].
        """
        result_get_list = Open_api_expense.get_expense_list()
        Checking.check_json_token(result_get_list, ['expenses', 'meta'])

@allure.epic("Get expense method [GET] v1/expense (with parameter limit)")
class Test_get_expense_list_limit():
    @allure.description("Checking when limit between 0 and total_count")
    def test_limit_normal(self):
        """
        Test with limit between 0 and total_count.
        1. Send valid request (limit = 1).
        2. Checking status code = 200.
        3. Checking current_count and expenses_count.
        """
        limit = 1
        result_get_list = Open_api_expense.get_expense_list(limit=limit)
        Checking.check_status_code(result_get_list, 200)
        check_data = result_get_list.json()
        current_count = check_data["meta"]["current_count"]
        expense_count = len(check_data["expenses"])
        assert current_count == limit
        # Success! Parameter current_count = limit.
        assert expense_count == limit
        print("Success! Count of expenses in the list = limit.")

    @allure.description("Checking when limit = 0 ")
    def test_limit_0(self):
        """
        Test with limit = 0.
        1. Send valid request (limit = 0).
        2. Get total_count, current_count, and really count of entries for comparison.
        3. Checking current_count = total_count.
        4. Checking expenses_count = current_count.
        """
        result_get_list = Open_api_expense.get_expense_list(limit=0)
        check_data = result_get_list.json()
        total_count = check_data["meta"]["total_count"]
        current_count = check_data["meta"]["current_count"]
        expense_count = len(check_data["expenses"])
        assert current_count == total_count
        # Expected values of current_count and expenses_count = total_count.
        assert expense_count == current_count
        print("Success! Count parameters are correct.")

    @allure.description("Checking when limit = total_count ")
    def test_limit_total(self):
        """
        Test with limit = total_count.
        Previous steps:
            - send a valid request
            - get total_count.
        1. Send a valid request (limit = total_count).
        2. Get total_count, current_count, and really count of entries for comparison.
        3. Checking current_count = total_count.
        4. Checking expenses_count = current_count.
        """
        limit = Open_api_expense.get_total_count_from_list()
        result_get_list = Open_api_expense.get_expense_list(limit=limit)
        check_data = result_get_list.json()
        total_count = check_data["meta"]["total_count"]
        current_count = check_data["meta"]["current_count"]
        expense_count = len(check_data["expenses"])
        assert current_count == total_count
        # Expected values of current_count and expenses_count = total_count.
        assert expense_count == current_count
        print("Success! Count parameters are correct.")

    @allure.description("Checking when limit > total_count")
    def test_limit_more(self):
        """
        Test with limit > total_count.
        Previous steps:
            - send a valid request
            - get total_count.
        1. Send a valid request (limit = total_count + 10).
        2. Get total_count, current_count, and really count of entries for comparison.
        3. Checking current_count = total_count.
        4. Checking expenses_count = current_count.
        """
        limit = Open_api_expense.get_total_count_from_list() + 10
        result_get_list = Open_api_expense.get_expense_list(limit=limit)
        check_data = result_get_list.json()
        total_count = check_data["meta"]["total_count"]
        current_count = check_data["meta"]["current_count"]
        expense_count = len(check_data["expenses"])
        assert current_count == total_count
        # Expected values of current_count and expenses_count = total_count.
        assert expense_count == current_count
        print("Success! Count parameters are correct.")

    @allure.description("Checking when limit < 0")
    def test_limit_negative(self):
        """
        Test with limit < 0.
        1. Send valid request (limit = -2).
        2. Get total_count, current_count, and really count of entries for comparison.
        3. Checking current_count = total_count - |limit|.
        4. Checking expenses_count = current_count.
        """
        limit = -2
        result_get_list = Open_api_expense.get_expense_list(limit=limit)
        check_data = result_get_list.json()
        current_count = check_data["meta"]["current_count"]
        expense_count = len(check_data["expenses"])
        expected_count = check_data["meta"]["total_count"] + limit
        assert current_count == expected_count
        # Expected values of current_count and expenses_count = total_count - |limit|.
        assert expense_count == current_count
        print("Success! Count parameters are correct.")

    @allure.description("Checking when limit < -total_count")
    def test_limit_less_negative_total(self):
        """
        Start test 'get expense list with limit > total_count '.
        Previous steps:
            - send a valid request
            - get total_count.
        1. Send valid request (limit = -total_count - 10).
        2. Get current_count and really count of entries for comparison.
        3. Checking current_count = 0.
        4. Checking expenses_count = current_count.
        """
        limit = -Open_api_expense.get_total_count_from_list() - 10
        result_get_list = Open_api_expense.get_expense_list(limit=limit)
        check_data = result_get_list.json()
        current_count = check_data["meta"]["current_count"]
        expense_count = len(check_data["expenses"])
        assert current_count == 0
        # Expected values of current_count and expenses_count = 0.
        assert expense_count == current_count
        print("Success! Count of expenses in the list = current_count.")

@allure.epic("Get expense method [GET] v1/expense (with parameter offset)")
class Test_get_expense_list_offset():

    @allure.description("Checking when offset between 0 and total_count")
    def test_offset_normal(self):
        """
        Test with offset between 0 and total_count.
        1. Send valid request (offset = 0, limit = 0) to get the full list.
        2. Checking status code = 200.
        3. Send a valid request (offset = {offset}).
        4. Checking the list started from the expense with expense {offset}.
        """
        result_get_list = Open_api_expense.get_expense_list(0, 0)
        check_data = result_get_list.json()
        total_count = check_data["meta"]["total_count"]
        offset = random.randint(1, total_count-1)
        expense_uid_expected = check_data["expenses"][offset]["uid"]
        Checking.check_status_code(result_get_list, 200)
        # Expected status code: 200 Created
        result_get_list = Open_api_expense.get_expense_list(offset=offset)
        check_data = result_get_list.json()
        assert check_data["expenses"][0]["uid"] == expense_uid_expected
        print("Success! List started from the number of the record = offset")

    @allure.description("Checking when offset = 0")
    def test_offset_0(self):
        """
        Test with offset = 0.
        1. Send valid request (offset = 0, limit 0) to get the full list.
        2. Checking that the list is full (current_count = total_count).
        """
        result_get_list = Open_api_expense.get_expense_list(0, 0)
        check_data = result_get_list.json()
        total_count = check_data["meta"]["total_count"]
        current_count = check_data["meta"]["current_count"]
        assert current_count == total_count
        # Success! List is full and started from entry #0.

    @allure.description("Checking when offset = total_count")
    def test_offset_equal_total(self):
        """
        Test with offset = total_count.
        Previous steps:
            - send a valid request
            - get total_count.
        1. Send a valid request (offset = total_current).
        2. Checking if the list is empty.
        """
        offset = Open_api_expense.get_total_count_from_list()
        result_get_list = Open_api_expense.get_expense_list(offset=offset)
        check_data = result_get_list.json()
        assert check_data["expenses"] == []
        # Success! List is empty.

    @allure.description("Checking when offset > total_count")
    def test_offset_more_total(self):
        """
        Test with offset > total_count.
        Previous steps:
            - send a valid request
            - get total_count.
        1. Send a valid request (offset > total_current).
        2. Checking if the list is empty.
        """
        offset = Open_api_expense.get_total_count_from_list() + 10
        result_get_list = Open_api_expense.get_expense_list(offset=offset)
        check_data = result_get_list.json()
        assert check_data["expenses"] == []
        print("Success! List is empty.")

    @allure.description("Checking when offset < 0")
    def test_offset_negative(self):
        """
        Test with offset < 0.
        1. Send valid request (offset = -4).
        2. Checking if the list is empty.
        """
        offset = -4
        result_get_list = Open_api_expense.get_expense_list(offset=offset)
        check_data = result_get_list.json()
        assert check_data["expenses"] == []
        print("Success! List is empty.")

@allure.epic("Get expense method [GET] v1/expense (Invalid options)")
class Test_get_expense_list_invalid_request():
    @allure.description("INVALID request => Checking response status code")
    def test_status_code(self):
        """
        Start test [GET] v1/expense (invalid request).
        1. Send invalid request (limit is float).
        2. Checking status code = 500.
        3. Send invalid request (limit is string).
        4. Checking status code = 500.
        5. Send invalid request (offset is float).
        6. Checking status code = 500.
        7. Send invalid request (offset is string).
        8. Checking status code = 500.
        """
        result_get_list = Open_api_expense.get_expense_list(limit=5.4)
        Checking.check_status_code(result_get_list, 500)  # Expected status code: 500 Internal Server Error

        result_get_list = Open_api_expense.get_expense_list(limit="5a4")
        Checking.check_status_code(result_get_list, 500)  # Expected status code: 500 Internal Server Error

        result_get_list = Open_api_expense.get_expense_list(offset=5.4)
        Checking.check_status_code(result_get_list, 500)  # Expected status code: 500 Internal Server Error

        result_get_list = Open_api_expense.get_expense_list(offset="5a4")
        Checking.check_status_code(result_get_list, 500)  # Expected status code: 500 Internal Server Error
