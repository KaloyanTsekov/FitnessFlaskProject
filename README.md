# Fitness Organizer Flask

## About the project

This is very easy to use backend application based
on Python and Flask library.

## How it Works?

The application has 3 types of users - Regular users, Moderators and Admin.
It also has 3 types of roles - Regular, Moderator and Admin. This is crucial for the Business Logic.
There is AWS S3 integration. It helps to store profile pictures on every user.

### Regular users:

They are able to create/update/delete Workout routines and add/edit/delete Exercises in them.
Regular users also can watch videos created by the moderators.

### Moderators:
They are able to add/edit/delete Video content, that is available for Non-registered and registered users.

### Admin:
There is only one Admin user. He is able to promote/demote users to become moderators.

## Before we start
The requirements.txt contains all the required packages and libraries.
You can install them by using this command
```bash
pip install -r requirements.txt
```
Below you can find all variables that are used in the code.Don't forget to configure and prepare your own environment.
```bash
JWT_SECRET=""
DB_USER=""
DB_PASSWORD=""
DB_PORT=""
DB_NAME=""
TEST_DB_USER=""
TEST_DB_PASSWORD=""
TEST_DB_PORT=""
TEST_DB_NAME=""
FLASK_APP=""
AWS_KEY=""
AWS_SECRET_KEY=""
S3_REGION=""
S3_BUCKET_NAME=""
ADMIN_EMAIL_ADDRESS=""
SOURCE_EMAIL_ADDRESS=""
CHARSET=""
```

## URL List:
### URls + Methods that require Token:
```bash
    ("/admin/promote/", "PUT"),  
    ("/admin/demote/", "PUT"),
    ("/videos/", "POST"),
    ("/videos/<int:id>/", "PUT"),
    ("/videos/<int:id>/", "DELETE"),
    ("/workout/", "POST"),
    ("/workout/", "GET"),
    ("/workout/<int:id>/", "PUT"),
    ("/workout/<int:id>/", "DELETE"),
    ("/exercise/<int:id>/", "POST"),
    ("/exercise/<int:id>/", "GET"),
    ("/exercise/modify/<int:id>/", "PUT"),
    ("/exercise/modify/<int:id>/", "DELETE"),
    ("/user/photo/", "PUT"),
    ("/user/photo/", "DELETE"),
```

### URls + Methods that don't require Token:
```bash
    ("/register/", "POST"),
    ("/login/", "POST"),
    ("/register/moderator/", "POST"),
    ("/login/moderator/", "POST"),
    ("/login/admin/", "POST"),
    ("/videos/", "GET"),
```
### URls + Methods that require Admin Role:
```bash
    ("/login/admin/", "POST"),
```
### URls + Methods that require Admin Role + Login:
```bash
    ("/admin/promote/", "PUT"),  
    ("/admin/demote/", "PUT"),
```
### URls + Methods that require Moderator Role + Login:
```bash
    ("/videos/<int:id>/", "PUT"),
    ("/videos/<int:id>/", "DELETE"),
    ("/videos/", "POST"),
```

### URls + Methods that require Regular Role + Login:
```bash
    ("/workout/", "POST"),
    ("/workout/", "GET"),
    ("/workout/<int:id>/", "PUT"),
    ("/workout/<int:id>/", "DELETE"),
    ("/exercise/<int:id>/", "POST"),
    ("/exercise/<int:id>/", "GET"),
    ("/exercise/modify/<int:id>/", "PUT"),
    ("/exercise/modify/<int:id>/", "DELETE"),
```
## Future functionalities:

1. AWS SES - Welcome e-mail, using SMTP
2. Create Thumbnail images on AWS S3 PutObject event, for cost savings and storage optimization
3. Front-end part
4. Deployment on AWS 
