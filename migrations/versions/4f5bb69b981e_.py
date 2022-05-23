"""empty message

Revision ID: 4f5bb69b981e
Revises: f59ee7fc55ec
Create Date: 2022-05-23 17:25:26.247178

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4f5bb69b981e'
down_revision = 'f59ee7fc55ec'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('planets',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('model', sa.String(length=120), nullable=False),
    sa.Column('manufacturer', sa.String(length=120), nullable=False),
    sa.Column('climate', sa.String(length=120), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('model'),
    sa.UniqueConstraint('model')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('planets')
    # ### end Alembic commands ###
