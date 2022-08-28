from database import db
from models.enumerates import BodySection, DaysFromTheWeekend


class AbstractExerciseModel(db.Model):
    __abstract__ = True
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(35), nullable=False)


class AbstractCategoryModel(db.Model):
    __abstract__ = True
    category = db.Column(db.Enum(BodySection), nullable=False)


class VideoModel(AbstractExerciseModel, AbstractCategoryModel):
    youtube_link = db.Column(db.String(255), nullable=False) #TODO Refactor with moderator
    users_pk = db.Column(db.Integer, db.ForeignKey("moderator_user.pk"), nullable=False)
    user = db.relationship("ModeratorUser")


class WorkoutModel(AbstractExerciseModel, AbstractCategoryModel):
    day = db.Column(db.Enum(DaysFromTheWeekend), nullable=False)
    users_pk = db.Column(db.Integer, db.ForeignKey("regular_user.pk"), nullable=False)
    user = db.relationship("RegularUser")



class ExerciseModel(AbstractExerciseModel):
    weight = db.Column(db.Float, nullable=False)
    series = db.Column(db.Integer, nullable=False)
    reps = db.Column(db.Integer, nullable=False)
    workout_pk = db.Column(db.Integer, db.ForeignKey("workout_model.id", ondelete='CASCADE'), nullable=False)
    user = db.relationship("WorkoutModel")
