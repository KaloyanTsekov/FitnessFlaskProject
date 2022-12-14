import boto3
from decouple import config


class SESService:
    def __init__(self):
        key = config("AWS_KEY")
        secret = config("AWS_SECRET_KEY")
        self.region = config("S3_REGION")
        self.bucket = config("S3_BUCKET_NAME")
        self.ses = boto3.client(
            "ses",
            region_name=self.region,
            aws_access_key_id=key,
            aws_secret_access_key=secret,
        )

    def send_email(self, moderator_email):
        response = self.ses.send_email(
            Destination={
                "ToAddresses": [
                    config("ADMIN_EMAIL_ADDRESS"),
                ],
            },
            Message={
                "Body": {
                    "Text": {
                        "Charset": config("CHARSET"),
                        "Data": f"Hello, Admin!\n\nHere it comes a new promotion Request for user: {moderator_email}",
                    }
                },
                "Subject": {
                    "Charset": config("CHARSET"),
                    "Data": "New Moderator User Request!",
                },
            },
            Source=config("SOURCE_EMAIL_ADDRESS"),
        )
        return response
