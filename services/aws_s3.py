import boto3
from botocore.exceptions import ClientError
from decouple import config
from werkzeug.exceptions import InternalServerError


class S3Service:
    def __init__(self):
        key = config("AWS_KEY")
        secret = config("AWS_SECRET_KEY")
        self.region = config("S3_REGION")
        self.bucket = config("S3_BUCKET_NAME")
        self.s3 = boto3.client(
            "s3",
            region_name=self.region,
            aws_access_key_id=key,
            aws_secret_access_key=secret,
        )

    def upload_photo(self, path, key):
        try:
            self.s3.upload_file(path, self.bucket, key)
            return f"https://{self.bucket}.s3.{self.region}.amazonaws.com/{key}"
        except ClientError:
            raise InternalServerError("S3 is not available at the moment")

    def delete_photo(self, object_name):
        try:
            self.s3.delete_object(Bucket=self.bucket, Key=object_name)
            return f"{object_name}: has been deleted"
        except ClientError:
            raise InternalServerError("S3 is not available at the moment")


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
