import json
import random
import uuid
from datetime import datetime, timezone

class Random_json():
    @staticmethod
    def json_for_create_new_expense():
        random_amount = round(random.uniform(1.0, 100000.0), 2)
        random_category = "Category" + str(random.randint(1, 10))
        random_description = "Description" + str(random.randint(1, 100))
        random_id = random.randint(1, 1000)
        random_uid = str(uuid.uuid4())
        random_created_at = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.%fZ")

        random_json = {
            "expense": {
                "amount": "{:.2f}".format(random_amount),
                "category": random_category,
                "description": random_description,
                "id": random_id,
                "uid": random_uid,
                "created_at": random_created_at
            }
        }
        return random_json

# Пример использования
random_json_data = Random_json.json_for_create_new_expense()
print(json.dumps(random_json_data, indent=2))
