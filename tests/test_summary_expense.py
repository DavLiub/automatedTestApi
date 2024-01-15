import json
import allure
from utils.checking import Checking
from utils.api import Open_api_expense

""" Summary expense """

@allure.epic("Get expense method [GET] v1/summary")
class Test_get_summary():
    @allure.description("VALID request (without options) => Checking response status code")
    def test_status_code(self):
        """
        Test validation status code.
        1. Send a valid request (without options) for getting summary.
        2. Checking response status code.
        """
        result_get_summary = Open_api_expense.get_summary_expense()
        Checking.check_status_code(result_get_summary, 200)  # Expected status code: 200 Created

    @allure.description("VALID request => Checking tokens")
    def test_summary_tokens(self):
        """
        Test validation request tokens.
        1. Send a valid request (without options) for getting summary.
        2. Checking request tokens.
        """
        result_get_summary = Open_api_expense.get_summary_expense()
        Checking.check_json_token(result_get_summary, ['summary'])
        token = json.loads(result_get_summary.text)
        token_keys = list(token["summary"].keys())
        assert token_keys == ['end_date', 'num_transactions', 'start_date', 'total']
        # Success! All tokens are in their places.

    @allure.description("VALID request => Checking value num_transactions")
    def test_summary_num_transactions(self):
        """
        Test validation num_transactions.
        1. Send a valid request (without options) for getting summary.
        2. Get the value of num_transactions.
        3. Get total_count from the list request.
        4. Checking if num_transactions is equal to total_count.
        """
        result_get_summary = Open_api_expense.get_summary_expense()
        check = result_get_summary.json()
        num_transactions = float(check.get('summary', {}).get('num_transactions', 0))

        result_get_list = Open_api_expense.get_expense_list(0, 0)
        check_data = result_get_list.json()
        total_count = check_data["meta"]["total_count"]
        assert num_transactions == total_count
        print("Success! Value of num transaction is correct")

    @allure.description("VALID request => Checking value total sum")
    def test_summary_total_value(self):
        """
        Test validation total value.
        1. Send a valid request (without options) for getting summary.
        2. Get the value of total sum.
        3. Count total sum from the list request.
        4. Checking if total sum is correct.
        """
        result_get_summary = Open_api_expense.get_summary_expense()
        check = result_get_summary.json()
        total_sum = float(check.get('summary', {}).get('total', 0))

        result_get_list = Open_api_expense.get_expense_list(0, 0)
        check_data = result_get_list.json()
        expenses_sum = 0.0
        for i in range(0, check_data["meta"]["current_count"]):
            expenses_sum += float(check_data["expenses"][i]["amount"])
        expenses_sum = round(100 * expenses_sum) / 100
        assert total_sum == expenses_sum
        print("Success! Total sum is correct")
