import random
from utils.http_method import Http_method

expense_url = "http://localhost:8000/v1/expense"
summary_url = "http://localhost:8000/v1/summary"

""" === Open API testing methods === """
class Open_api_expense():

    """ Method POST --create new expense record """
    @staticmethod
    def create_new_expense(json):
        """
            Create a new expense record.

            Args:
                json (dict): JSON data for the expense record.

            Returns:
                requests.Response: The response object.
        """

        post_url = expense_url
        print(post_url)
        result_post = Http_method.post(post_url, json)
        result_post.encoding = "utf-8"
        print(result_post.text)
        return result_post

    """ Method GET --return expense list """
    @staticmethod
    def get_expense_list(offset=None, limit=None):
        """
        Get the list of expenses.

        Args:
            offset (int): Offset for pagination.
            limit (int): Limit for pagination.

        Returns:
            requests.Response: The response object.
        """
        params = {}
        # Add parameters if they are passed
        if offset is not None:
            params['offset'] = offset
        if limit is not None:
            params['limit'] = limit
        # Forming a URL with parameters, if any
        if params:
            get_url = expense_url + '?' + '&'.join([f'{key}={value}' for key, value in params.items()])
        else:
            get_url = expense_url
        print(get_url)
        result_get = Http_method.get(get_url)
        print(result_get.text)
        result_get.encoding = "utf-8"
        return result_get

    """ Method GET --return expense record by {expense_uid} """
    @staticmethod
    def get_expense_by_uid(expense_uid):
        """
        Get an expense record by UID.

        Args:
            expense_uid (str): UID of the expense record.

        Returns:
            requests.Response: The response object.
        """

        get_url = expense_url+"/"+expense_uid
        print(get_url)
        result_get = Http_method.get(get_url)
        print(result_get.text)
        result_get.encoding = "utf-8"
        return result_get

    """ Method PUT --update expense record by {expense_uid} """
    @staticmethod
    def put_update_expense(expense_uid, body):
        """
        Update an expense record by UID.

        Args:
            expense_uid (str): UID of the expense record to update.
            body (dict): Updated JSON data for the expense record.

        Returns:
            requests.Response: The response object.
        """
        put_url = expense_url+"/"+expense_uid
        print(put_url)
        result_put = Http_method.put(put_url, body)
        result_put.encoding = "utf-8"
        print(result_put.text)
        return result_put

    """ Method DELETE --delete expense record by {expense_uid} """
    @staticmethod
    def delete_expense(expense_uid):
        """
        Delete an expense record by UID.

        Args:
            expense_uid (str): UID of the expense record to delete.

        Returns:
            requests.Response: The response object.
        """
        delete_url = expense_url+"/"+expense_uid
        print(delete_url)
        result_delete = Http_method.delete(delete_url)
        result_delete.encoding="utf-8"
        print(result_delete.text)
        return result_delete

    """ Method GET --return summary expenses """

    @staticmethod
    def get_summary_expense(end_date=None, start_date=None):
        """
        Get summary expenses.

        Args:
            end_date (str): End date for filtering.
            start_date (str): Start date for filtering.

        Returns:
            requests.Response: The response object.
        """
        params = {}
        # Add parameters if they are passed
        if end_date is not None:
            params['end_date'] = end_date
        if start_date is not None:
            params['start_date'] = start_date
        # Forming a URL with parameters, if any
        if params:
            get_url = summary_url + '?' + '&'.join([f'{key}={value}' for key, value in params.items()])
        else:
            get_url = summary_url
        print(get_url)
        result_get = Http_method.get(get_url)
        print(result_get.text)
        result_get.encoding = "utf-8"
        return result_get

    """ Method GET --return random uid from list """

    @staticmethod
    def get_random_expense_uid():
        """
        Get a random UID from the expense list.

        Returns:
            str: Random UID.
        """
        result_get_expense = Open_api_expense.get_expense_list(0, 0)
        check_data = result_get_expense.json()
        current_count = check_data["meta"]["current_count"]
        return check_data["expenses"][random.randint(0, current_count-1)]["uid"]

    @staticmethod
    def get_total_count_from_list():
        """
        Get the total count of expenses.

        Returns:
            int: Total count of expenses.
        """
        result_get_expense = Open_api_expense.get_expense_list(0, 0)
        check_data = result_get_expense.json()
        current_count = check_data["meta"]["current_count"]
        return check_data["meta"]["total_count"]

    @staticmethod
    def get_min_date_in_list():
        """
        Get the minimum date in the expense list.

        Returns:
            str: Minimum date.
        """
        result_get_expense = Open_api_expense.get_expense_list(0, 0)
        check_data = result_get_expense.json()
        if "expenses" in check_data and len(check_data["expenses"]) > 0:
            created_at_values = [expense["created_at"] for expense in check_data["expenses"]]
            min_created_at = min(created_at_values)
            return min_created_at
        return None

    @staticmethod
    def get_max_date_in_list():
        """
        Get the maximum date in the expense list.

        Returns:
            str: Maximum date.
        """
        result_get_expense = Open_api_expense.get_expense_list(0, 0)
        check_data = result_get_expense.json()
        if "expenses" in check_data and len(check_data["expenses"]) > 0:
            created_at_values = [expense["created_at"] for expense in check_data["expenses"]]
            max_created_at = max(created_at_values)
            return max_created_at
        return None

