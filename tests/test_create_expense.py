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
        """
        Create a new expense with a valid POST request.

        Steps:
        1. Create a new expense with valid JSON data.
        2. Check if the status code of the response is 201 (Created).
        3. Get the newly created expense by UID.
        4. Check if the status code of the response is 200 (OK).
        """
        new_expense_uid = str(uuid.uuid4())
        json_create_new_expense = {
            "expense": {
                "amount": "100",
                "category": "category",
                "description": "description",
                "id": 0,
                "uid": new_expense_uid,
                "created_at": "2024-01-13T15:50:40.752Z"
            }
        }
        result_new_list = Open_api_expense.create_new_expense(json_create_new_expense)
        Checking.check_status_code(result_new_list, 201)  # Expected status code: 201 Created
        result_get_expense = Open_api_expense.get_expense_by_uid(new_expense_uid)
        Checking.check_status_code(result_get_expense, 200)  # Expected status code: 200 OK

    @allure.description("Create expense -> method POST: INVALID request (without body)")
    def test_create_new_expense2(self):
        """
        Create a new expense with an invalid POST request (without body).

        Steps:
        1. Attempt to create a new expense with body=None.
        2. Check if the status code of the response is 400 (Bad Request).
        3. Check if the response contains the expected error tokens: ['description', 'status', 'message'].
        """
        json_create_new_expense = None
        result_new_list = Open_api_expense.create_new_expense(json_create_new_expense)
        Checking.check_status_code(result_new_list, 400)
        Checking.check_json_token(result_new_list, ['description', 'status', 'message'])

    @allure.description("Create expense -> method POST: INVALID request (without body)")
    def test_create_incomplete_json(self):
        """
        Create a new expense with an invalid POST request (without body).

        Steps:
        Steps:
        1. Create a new expense with valid JSON data.
        2. Check if the status code of the response is 400 (Bad Request).
        3. Check if the response contains the expected error tokens: ['description', 'status', 'message'].
        """
        new_expense_uid = str(uuid.uuid4())
        json_create_new_expense = {
            "expense": {
                "amount": "100",
                "id": 0,
                "uid": new_expense_uid,
            }
        }
        result_new_list = Open_api_expense.create_new_expense(json_create_new_expense)
        Checking.check_status_code(result_new_list, 400)
        Checking.check_json_token(result_new_list, ['description', 'status', 'message'])


    """
    Other testing will be possible when will be fixed method POST for creating
    """
