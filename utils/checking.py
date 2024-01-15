"""  Methods for checking responses """
import json

from requests import Response


class Checking():

    """ Method for checking Status code any response """
    @staticmethod
    def check_status_code(response, status_code):
        """
        Check if the response status code matches the expected status code.

        Args:
            response (Response): The response object.
            status_code (int): The expected status code.

        Returns:
            None
        """
        assert status_code == response.status_code
        print("Success! Status code ("+str(response.status_code)+") is correct")

    """ Method for checking required fields in response"""
    @staticmethod
    def check_json_token(response, expected_value):
        """
        Check if all required fields are present in the JSON response.

        Args:
            response (Response): The response object.
            expected_value (list): List of expected fields.

        Returns:
            None
        """
        token = json.loads(response.text)
        assert list(token) == expected_value
        print("Success! All required fields are present")


    """ Method for checking values required fields in response"""
    @staticmethod
    def check_json_value(response, field_name, expected_value):
        """
        Check if the value of the specified field in the JSON response matches the expected value.

        Args:
            response (Response): The response object.
            field_name (str): The name of the field to check.
            expected_value (str): The expected value of the field.

        Returns:
            None
        """

        check = response.json()
        check_info = check.get(field_name)
        assert check_info == expected_value
        print("Success! Value of " + field_name + " is correct!")


    """ Method for checking values required fields in response by included words"""
    @staticmethod
    def check_json_search_word_in_value(response, field_name, search_word):
        """
        Check if the specified word is present in the value of the specified field in the JSON response.

        Args:
            response (Response): The response object.
            field_name (str): The name of the field to check.
            search_word (str): The word to search for in the field value.

        Returns:
            None
        """
        check = response.json()
        check_info = check.get(field_name)
        if search_word in check_info:
            print("Success! Word '" + search_word + "' is present!")
        else:
            print("FAIL! Word '" + search_word + "' is absent!")
