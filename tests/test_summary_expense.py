import json
import random
import allure
from utils.checking import Checking
from utils.api import Open_api_expense
from utils.logger import Console_log

""" Summary expense """


@allure.epic("Get expense method [GET] v1/summary")
class Test_get_summary():
    @allure.description("VALID request (without options) => Checking response status code")
    def test_status_code(self):
        print("\n")
        print("|---------------------------------------------|")
        print("|       Start test validation status code     |")
        print("|---------------------------------------------|\n")
        print("1. Send valid request (without options) for getting summary")
        result_get_summary = Open_api_expense.get_summary_expense()
        print("2. Checking response status code")
        Checking.check_status_code(result_get_summary, 200)  # Expected status code: 200 Created

    @allure.description("VALID request => Checking tokens")
    def test_summary_tokens(self):
        print("\n")
        print("|-----------------------------------------------|")
        print("|       Start test validation request tokens    |")
        print("|-----------------------------------------------|\n")

        Console_log.print("1. Send valid request (without options) for getting summary")
        result_get_summary = Open_api_expense.get_summary_expense()
        Console_log.print("2. Checking request tokens")
        Checking.check_json_token(result_get_summary, ['summary'])
        token = json.loads(result_get_summary.text)
        token_keys = list(token["summary"].keys())
        assert token_keys == ['end_date', 'num_transactions', 'start_date', 'total']
        Console_log.print("Success! All tokens are on their places")

    @allure.description("VALID request => Checking value num_transactions")
    def test_summary_num_transactions(self):
        print("\n")
        print("|-------------------------------------------------|")
        print("|       Start test validation num_transactions    |")
        print("|-------------------------------------------------|\n")

        print("1. Send valid request (without options) for getting summary")
        result_get_summary = Open_api_expense.get_summary_expense()
        print("2. Get value of num_transactions")
        check = result_get_summary.json()
        num_transactions = check["summary"][0]["num_transactions"]
        print(num_transactions)
        print("3. Get total_count from list request")
        result_get_list = Open_api_expense.get_expense_list(0, 0)
        check_data = result_get_list.json()
        total_count = check_data["meta"]["total_count"]
        print(total_count)
        assert num_transactions == total_count
        print("Success! Value of num transaction is correct")

    @allure.description("VALID request => Checking value total sum")
    def test_summary_total_value(self):
        print("\n")
        print("|-------------------------------------------------|")
        print("|       Start test validation total value         |")
        print("|-------------------------------------------------|\n")

        print("1. Send valid request (without options) for getting summary")
        result_get_summary = Open_api_expense.get_summary_expense()
        print("2. Get value of total sum")
        check = result_get_summary.json()
        total_sum = float(check["summary"].get("total"))
        print("total" + str(total_sum))
        print("3. Count total sum from list request")
        result_get_list = Open_api_expense.get_expense_list(0, 0)
        check_data = result_get_list.json()
        expenses_sum = 0.0
        for i in range(0, check_data["meta"]["current_count"]):
            expenses_sum += float(check_data["expenses"][i]["amount"])
        expenses_sum = round(100*expenses_sum)/100
        assert total_sum == expenses_sum
        print("Success! Total sum is correct")

