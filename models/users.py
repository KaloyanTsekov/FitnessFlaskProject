from database import db
from models.enumerates import UserRole


class AbstractBaseUserModel(db.Model):
    __abstract__ = True
    pk = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(20), nullable=False)
    last_name = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)


class RegularUser(AbstractBaseUserModel):
    __tablename__ = 'regular_user'
    role = db.Column(db.Enum(UserRole), default=UserRole.regular, nullable=False)
    videos = db.relationship("VideoModel", backref="video_model", lazy="dynamic")

class ModeratorUser(AbstractBaseUserModel):
    __tablename__ = 'moderator_user'
    role = db.Column(db.Enum(UserRole), default=UserRole.regular, nullable=False)


class AdminUser(AbstractBaseUserModel):
    __tablename__ = 'admin_user'
    role = db.Column(db.Enum(UserRole), default=UserRole.admin, nullable=False)
