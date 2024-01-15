import json

import allure
import requests

from utils.logger import Logger

""" === HTTP methods list ==="""
class Http_method:
    headers = {'Content-Type' : 'application/json'}
    cookie = ""

    @staticmethod
    def get(url):
        with allure.step("GET"):
            Logger.add_request(url, method='GET')
            result = requests.get(url, headers=Http_method.headers, cookies=Http_method.cookie)
            Logger.add_response(result)
            return result

    @staticmethod
    def post(url, body):
        with allure.step("POST"):
            Logger.add_request(url, method='POST', body=body)
            result = requests.post(url, json=body, headers=Http_method.headers, cookies=Http_method.cookie)
            Logger.add_response(result)
            return result

    @staticmethod
    def put(url, body):
        with allure.step("PUT"):
            Logger.add_request(url, method='PUT', body=body)
            result = requests.put(url, json=body, headers=Http_method.headers, cookies=Http_method.cookie)
            Logger.add_response(result)
            return result

    @staticmethod
    def delete(url):
        with allure.step("DELETE"):
            Logger.add_request(url, method='DELETE')
            result = requests.delete(url, headers=Http_method.headers, cookies=Http_method.cookie)
            Logger.add_response(result)
            return result