def main_handler(event, context):
    ip = event.get("headers", {}).get("X-Forwarded-For", "")
    return {"statusCode": 200, "body": ip }
