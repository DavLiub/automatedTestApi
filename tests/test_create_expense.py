import json
import uuid
from datetime import datetime, timezone

import allure

from utils.checking import Checking
from utils.api import Open_api_expense
from requests import Response

from utils.json_gen import Random_json
from utils import logger
""" Creating,"""


@allure.epic("Create expense method [POST] v1/expense")
class Test_create_new_expense():
    @allure.description("Create expense -> method POST: VALID request")
    def test_create_new_expense(self):
        print("\n")
        print("|-------------------------------------------------|")
        print("|       Start test validation Status code         |")
        print("|                 (valid request)                 |")
        print("|-------------------------------------------------|\n")
        new_expense_uid = str(uuid.uuid4())
        json_create_new_expense = {
            "expense": {
                "amount": "100",
                "category": "category",
                "description": "description",
                "id": 0,
                "uid": new_expense_uid,
                # "created_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.%fZ")
                "created_at": "2024-01-13T15:50:40.752Z"
            }
        }
        print("1. Create new expense")
        result_new_list = Open_api_expense.create_new_expense(json_create_new_expense)
        Checking.check_status_code(result_new_list, 201)  # Expected status code: 201 Created
        print("2. Get expense with {expense_uid}")
        result_get_expense = Open_api_expense.get_expense_by_uid(new_expense_uid)
        print("3. Checking status code = 200")
        Checking.check_status_code(result_get_expense, 200)  # Expected status code: 200 OK

    @allure.description("Create expense -> method POST: INVALID request (without body)")
    def test_create_new_expense2(self):
        print("\n")
        print("|-------------------------------------------------|")
        print("|       Start test validation Status code         |")
        print("|               (invalid request)                 |")
        print("|-------------------------------------------------|\n")
        json_create_new_expense = None
        print("2. Checking status code = 400")
        result_new_list = Open_api_expense.create_new_expense(json_create_new_expense)
        print("3. Checking request tokens = ['description', 'status', 'message']")
        Checking.check_status_code(result_new_list, 400)  # Expected status code: 201 Created
        Checking.check_json_token(result_new_list, ['description', 'status', 'message'])


"""
Other testing will be possible when will be fixed method POST for creating
"""