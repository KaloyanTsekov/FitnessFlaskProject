from flask_testing import TestCase

from config import create_app
from database import db
from models import WorkoutModel
from tests.factories import AdminUserFactory, RegularUserFactory, WorkoutFactory, ModeratorUserFactory
from tests.helpers import generate_token

ENDPOINTS_DATA_TOKEN_REQUIRED = (
    ("/admin/promote/", "PUT"),
    ("/admin/demote/", "PUT"),
    ("/videos/", "POST"),
    ("/videos/1/", "PUT"),
    ("/videos/1/", "DELETE"),
    ("/workout/", "POST"),
    ("/workout/", "GET"),
    ("/workout/1/", "PUT"),
    ("/workout/1/", "DELETE"),
    ("/exercise/1/", "POST"),
    ("/exercise/1/", "GET"),
    ("/exercise/modify/1/", "PUT"),
    ("/exercise/modify/1/", "DELETE"),
    ("/user/photo/", "PUT"),
    ("/user/photo/", "DELETE")
)

ENDPOINTS_DATA_NO_TOKEN = (
    ("/register/", "POST"),
    ("/login/", "POST"),
    ("/register/moderator/", "POST"),
    ("/login/moderator/", "POST"),
    ("/login/admin/", "POST"),
    ("/videos/", "GET"),)

class TestApp(TestCase):
    def create_app(self):
        return create_app("config.TestConfig")

    def setUp(self):
        db.init_app(self.app)
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def iterate_endpoints(
            self,
            endpoints_data,
            status_code_method,
            expected_resp_body,
            headers=None,
            payload=None,
    ):
        if not headers:
            headers = {}
        if not payload:
            payload = {}

        resp = None
        for url, method in endpoints_data:
            if method == "GET":
                resp = self.client.get(url, headers=headers)
            elif method == "POST":
                resp = self.client.post(url, headers=headers)
            elif method == "PUT":
                resp = self.client.put(url, headers=headers)
            elif method == "DELETE":
                resp = self.client.delete(url, headers=headers)
            status_code_method(resp)
            self.assertEqual(resp.json, expected_resp_body)

    def test_login_required(self):
        self.iterate_endpoints(
            ENDPOINTS_DATA_TOKEN_REQUIRED, self.assert_401, {"message": "Missing token"}
        )

    def test_invalid_token_raises(self):
        headers = {"Authorization": "Bearer eyJ"}
        self.iterate_endpoints(
            ENDPOINTS_DATA_TOKEN_REQUIRED, self.assert_401, {"message": "Invalid token"}, headers
        )

    def test_regular_register_schema_request_raises_missing_first_name(self):
        data = {"last_name": "Test", "email": "test@abv.bg", "password": "Zz12>!.Qw"}
        headers = {"Content-Type": "application/json"}
        url = "/register/"

        resp = self.client.post(url, headers=headers, json=data)
        self.assert400(resp)
        assert resp.json == {"message": {"first_name": ["Missing data for required field."]}}

    def test_regular_register_schema_request_raises_missing_last_name(self):
        data = {"first_name": "Test", "email": "test@abv.bg", "password": "Zz12>!.Qw"}
        headers = {"Content-Type": "application/json"}
        url = "/register/"

        resp = self.client.post(url, headers=headers, json=data)
        self.assert400(resp)
        assert resp.json == {"message": {"last_name": ["Missing data for required field."]}}

    def test_regular_register_schema_request_raises_missing_email(self):
        data = {"first_name": "Test", "last_name": "Test", "password": "Zz12>!.Qw"}
        headers = {"Content-Type": "application/json"}
        url = "/register/"

        resp = self.client.post(url, headers=headers, json=data)
        self.assert400(resp)
        assert resp.json == {"message": {"email": ["Missing data for required field."]}}

    def test_regular_register_schema_request_raises_missing_password(self):
        data = {"first_name": "Test", "last_name": "Test", "email": "test@abv.bg"}
        headers = {"Content-Type": "application/json"}
        url = "/register/"

        resp = self.client.post(url, headers=headers, json=data)
        self.assert400(resp)
        assert resp.json == {"message": {"password": ["Missing data for required field."]}}

    def test_regular_login_schema_request_raises_missing_password(self):
        data = {"email": "test@abv.bg"}
        headers = {"Content-Type": "application/json"}
        url = "/login/"

        resp = self.client.post(url, headers=headers, json=data)
        self.assert400(resp)
        assert resp.json == {"message": {"password": ["Missing data for required field."]}}

    def test_regular_login_schema_request_raises_missing_email(self):
        data = {"password": "Zz12>!.Qw"}
        headers = {"Content-Type": "application/json"}
        url = "/login/"

        resp = self.client.post(url, headers=headers, json=data)
        self.assert400(resp)
        assert resp.json == {"message": {"email": ["Missing data for required field."]}}

    def test_moderator_register_schema_request_raises_missing_first_name(self):
        data = {"last_name": "Test", "email": "test@abv.bg", "password": "Zz12>!.Qw"}
        headers = {"Content-Type": "application/json"}
        url = "/register/moderator/"

        resp = self.client.post(url, headers=headers, json=data)
        self.assert400(resp)
        assert resp.json == {"message": {"first_name": ["Missing data for required field."]}}

    def test_moderator_register_schema_request_raises_missing_last_name(self):
        data = {"first_name": "Test", "email": "test@abv.bg", "password": "Zz12>!.Qw"}
        headers = {"Content-Type": "application/json"}
        url = "/register/moderator/"

        resp = self.client.post(url, headers=headers, json=data)
        self.assert400(resp)
        assert resp.json == {"message": {"last_name": ["Missing data for required field."]}}

    def test_moderator_register_schema_request_raises_missing_email(self):
        data = {"first_name": "Test", "last_name": "Test", "password": "Zz12>!.Qw"}
        headers = {"Content-Type": "application/json"}
        url = "/register/moderator/"

        resp = self.client.post(url, headers=headers, json=data)
        self.assert400(resp)
        assert resp.json == {"message": {"email": ["Missing data for required field."]}}

    def test_moderator_register_schema_request_raises_missing_password(self):
        data = {"first_name": "Test", "last_name": "Test", "email": "test@abv.bg"}
        headers = {"Content-Type": "application/json"}
        url = "/register/moderator/"

        resp = self.client.post(url, headers=headers, json=data)
        self.assert400(resp)
        assert resp.json == {"message": {"password": ["Missing data for required field."]}}

    def test_moderator_login_schema_request_raises_missing_password(self):
        data = {"email": "test@abv.bg"}
        headers = {"Content-Type": "application/json"}
        url = "/login/moderator/"

        resp = self.client.post(url, headers=headers, json=data)
        self.assert400(resp)
        assert resp.json == {"message": {"password": ["Missing data for required field."]}}

    def test_moderator_login_schema_request_raises_missing_email(self):
        data = {"password": "Zz12>!.Qw"}
        headers = {"Content-Type": "application/json"}
        url = "/login/moderator/"

        resp = self.client.post(url, headers=headers, json=data)
        self.assert400(resp)
        assert resp.json == {"message": {"email": ["Missing data for required field."]}}

    def test_admin_login_schema_request_raises_missing_password(self):
        data = {"email": "test@abv.bg"}
        headers = {"Content-Type": "application/json"}
        url = "/login/admin/"

        resp = self.client.post(url, headers=headers, json=data)
        self.assert400(resp)
        assert resp.json == {"message": {"password": ["Missing data for required field."]}}

    def test_admin_login_schema_request_raises_missing_email(self):
        data = {"password": "Zz12>!.Qw"}
        headers = {"Content-Type": "application/json"}
        url = "/login/admin/"

        resp = self.client.post(url, headers=headers, json=data)
        self.assert400(resp)
        assert resp.json == {"message": {"email": ["Missing data for required field."]}}

    def test_admin_promotion_schema_raises(self):
        user = AdminUserFactory()
        token = generate_token(user)
        data = {}
        headers = {"Content-Type": "application/json", "Authorization": f"Bearer {token}" }
        url = "/admin/promote/"
        resp = self.client.put(url, headers=headers, json=data)
        self.assert400(resp)
        assert resp.json == {"message": {"email": ["Missing data for required field."]}}

    def test_admin_demotion_schema_raises(self):
        user = AdminUserFactory()
        token = generate_token(user)
        data = {}
        headers = {"Content-Type": "application/json", "Authorization": f"Bearer {token}" }
        url = "/admin/demote/"
        resp = self.client.put(url, headers=headers, json=data)
        self.assert400(resp)
        assert resp.json == {"message": {"email": ["Missing data for required field."]}}

    def test_exercise_creation_ok(self):
        user = RegularUserFactory()
        WorkoutFactory()
        token = generate_token(user)
        data = {"name": "test", "weight": 23.5, "series": 5, "reps": 5}
        headers = {"Content-Type": "application/json", "Authorization": f"Bearer {token}" }
        url = "/exercise/1/"
        resp = self.client.post(url, headers=headers, json=data)
        assert resp.status_code == 201
        #assert resp.json == {"message": {"name": ["Missing data for required field."]}}

    def test_exercise_schema_request_missing_name_raises(self):
        user = RegularUserFactory()
        WorkoutFactory()
        token = generate_token(user)
        data = {"weight": 23.5, "series": 5, "reps": 5}
        headers = {"Content-Type": "application/json", "Authorization": f"Bearer {token}" }
        url = "/exercise/1/"
        resp = self.client.post(url, headers=headers, json=data)
        assert resp.json == {"message": {"name": ["Missing data for required field."]}}

    def test_exercise_creation_missing_weight_raises(self):
        user = RegularUserFactory()
        WorkoutFactory()
        token = generate_token(user)
        data = {"name": "test", "series": 5, "reps": 5}
        headers = {"Content-Type": "application/json", "Authorization": f"Bearer {token}" }
        url = "/exercise/1/"
        resp = self.client.post(url, headers=headers, json=data)
        assert resp.json == {"message": {"weight": ["Missing data for required field."]}}

    def test_exercise_creation_wrong_weight_data_raises(self):
        user = RegularUserFactory()
        WorkoutFactory()
        token = generate_token(user)
        data = {"name": "test", "weight": "string", "series": 5, "reps": 5}
        headers = {"Content-Type": "application/json", "Authorization": f"Bearer {token}" }
        url = "/exercise/1/"
        resp = self.client.post(url, headers=headers, json=data)
        assert resp.json == {'message': {'weight': ['Not a valid number.']}}

    def test_exercise_creation_missing_series_raises(self):
        user = RegularUserFactory()
        WorkoutFactory()
        token = generate_token(user)
        data = {"name": "test", "weight": 5.5, "reps": 5}
        headers = {"Content-Type": "application/json", "Authorization": f"Bearer {token}"}
        url = "/exercise/1/"
        resp = self.client.post(url, headers=headers, json=data)
        assert resp.json == {"message": {"series": ["Missing data for required field."]}}

    def test_exercise_creation_missing_reps_raises(self):
        user = RegularUserFactory()
        WorkoutFactory()
        token = generate_token(user)
        data = {"name": "test", "weight": 5.5, "series": 5}
        headers = {"Content-Type": "application/json", "Authorization": f"Bearer {token}"}
        url = "/exercise/1/"
        resp = self.client.post(url, headers=headers, json=data)
        assert resp.json == {"message": {"reps": ["Missing data for required field."]}}

    def test_create_workout_ok(self):
        user = RegularUserFactory()
        token = generate_token(user)
        data = {"name": "test", "category": "chest", "day": "monday"}
        headers = {"Content-Type": "application/json", "Authorization": f"Bearer {token}"}
        url = "/workout/"
        resp = self.client.post(url, headers=headers, json=data)
        assert resp.status_code == 201

    def test_check_db_create_workout_ok(self):
        workouts = WorkoutModel.query.all()
        assert len(workouts) == 0
        user = RegularUserFactory()
        token = generate_token(user)
        data = {"name": "test", "category": "chest", "day": "monday"}
        headers = {"Content-Type": "application/json", "Authorization": f"Bearer {token}"}
        url = "/workout/"
        resp = self.client.post(url, headers=headers, json=data)
        assert resp.status_code == 201
        workouts = WorkoutModel.query.all()
        assert len(workouts) == 1

    def test_delete_workout_ok(self):
        workouts = WorkoutModel.query.all()
        assert len(workouts) == 0
        user = RegularUserFactory()
        token = generate_token(user)
        workout = WorkoutFactory()
        workouts = WorkoutModel.query.all()
        assert len(workouts) == 1
        id = workout.id
        headers = {"Content-Type": "application/json", "Authorization": f"Bearer {token}"}
        url = f"/workout/{id}/"
        resp = self.client.delete(url, headers=headers)
        assert resp.status_code == 200

    def test_create_video_ok(self):
        moderator = ModeratorUserFactory()
        token = generate_token(moderator)
        data = {"name": "video", "category": "chest", "youtube_link": "somelink"}
        headers = {"Content-Type": "application/json", "Authorization": f"Bearer {token}"}
        url = "/videos/"
        resp = self.client.post(url, headers=headers, json=data)
        assert resp.status_code == 201

