"""Add photo_url in AbstractBaseUserModel for the S3 integration

Revision ID: e2dfb516e97b
Revises: 93b7cda173ef
Create Date: 2022-08-29 22:24:48.476815

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "e2dfb516e97b"
down_revision = "93b7cda173ef"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "admin_user", sa.Column("photo_url", sa.String(length=255), nullable=True)
    )
    op.add_column(
        "moderator_user", sa.Column("photo_url", sa.String(length=255), nullable=True)
    )
    op.add_column(
        "regular_user", sa.Column("photo_url", sa.String(length=255), nullable=True)
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("regular_user", "photo_url")
    op.drop_column("moderator_user", "photo_url")
    op.drop_column("admin_user", "photo_url")
    # ### end Alembic commands ###
