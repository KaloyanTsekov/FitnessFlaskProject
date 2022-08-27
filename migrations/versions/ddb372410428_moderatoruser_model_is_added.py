"""ModeratorUser model is added

Revision ID: ddb372410428
Revises: c1aef9c3a772
Create Date: 2022-08-27 19:24:50.631457

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ddb372410428'
down_revision = 'c1aef9c3a772'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('moderator_user',
    sa.Column('pk', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=20), nullable=False),
    sa.Column('last_name', sa.String(length=20), nullable=False),
    sa.Column('email', sa.String(length=50), nullable=False),
    sa.Column('password', sa.String(length=255), nullable=False),
    sa.Column('role', sa.Enum('regular', 'moderator', 'admin', name='moderator'), nullable=False),
    sa.PrimaryKeyConstraint('pk'),
    sa.UniqueConstraint('email')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('moderator_user')
    # ### end Alembic commands ###