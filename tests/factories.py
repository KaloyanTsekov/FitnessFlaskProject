import factory

from database import db
from models import UserRole, AdminUser, RegularUser, ModeratorUser, WorkoutModel


class BaseFactory(factory.Factory):
    @classmethod
    def create(cls, **kwargs):
        object = super().create(**kwargs)
        db.session.add(object)
        db.session.flush()
        return object


#TODO Refactor to use one base class
class AdminUserFactory(BaseFactory):
    class Meta:
        model = AdminUser
    pk = factory.Sequence(lambda n: n)
    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")
    email = factory.Faker("email")
    password = factory.Faker("password")
    role = UserRole.admin


class ModeratorUserFactory(BaseFactory):
    class Meta:
        model = ModeratorUser
    pk = factory.Sequence(lambda n: n)
    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")
    email = factory.Faker("email")
    password = factory.Faker("password")
    role = UserRole.moderator


class RegularUserFactory(BaseFactory):
    class Meta:
        model = RegularUser
    pk = 1
    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")
    email = factory.Faker("email")
    password = factory.Faker("password")
    role = UserRole.regular


class WorkoutFactory(BaseFactory):
    class Meta:
        model = WorkoutModel
    id = 1
    name = factory.Faker("first_name")
    category = "chest"
    day = "monday"
    users_pk = 1
