"""empty message

Revision ID: e03a7b2b9c3a
Revises: 33ebc71fcf82
Create Date: 2022-05-23 18:40:34.851924

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'e03a7b2b9c3a'
down_revision = '33ebc71fcf82'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('planets', sa.Column('terrain', sa.String(length=120), nullable=True))
    op.drop_column('planets', 'manufacturer')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('planets', sa.Column('manufacturer', mysql.VARCHAR(length=120), nullable=True))
    op.drop_column('planets', 'terrain')
    # ### end Alembic commands ###
