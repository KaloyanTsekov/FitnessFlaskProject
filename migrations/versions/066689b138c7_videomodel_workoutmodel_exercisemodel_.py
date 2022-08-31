"""VideoModel, WorkoutModel, ExerciseModel in exercises.py and BodySection, DaysFromTheWeekend enumerators in enumerates.py added

Revision ID: 066689b138c7
Revises: 35569fcb7c62
Create Date: 2022-08-27 20:36:44.207289

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "066689b138c7"
down_revision = "35569fcb7c62"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "exercise_model",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(length=35), nullable=False),
        sa.Column("weight", sa.Float(), nullable=False),
        sa.Column("series", sa.Integer(), nullable=False),
        sa.Column("reps", sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "video_model",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(length=35), nullable=False),
        sa.Column(
            "category",
            sa.Enum(
                "legs", "arms", "shoulders", "chest", "back", "abs", name="bodysection"
            ),
            nullable=False,
        ),
        sa.Column("youtube_link", sa.String(length=255), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "workout_model",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(length=35), nullable=False),
        sa.Column(
            "category",
            sa.Enum(
                "legs", "arms", "shoulders", "chest", "back", "abs", name="bodysection"
            ),
            nullable=False,
        ),
        sa.Column(
            "day",
            sa.Enum(
                "monday",
                "tuesday",
                "wednesday",
                "thursday",
                "friday",
                "saturday",
                "sunday",
                name="daysfromtheweekend",
            ),
            nullable=False,
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("workout_model")
    op.drop_table("video_model")
    op.drop_table("exercise_model")
    # ### end Alembic commands ###
