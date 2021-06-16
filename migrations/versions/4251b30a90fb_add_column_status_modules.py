"""add column status modules

Revision ID: 4251b30a90fb
Revises: 97c41170a436
Create Date: 2021-06-15 20:48:20.400697

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4251b30a90fb'
down_revision = '97c41170a436'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('modules', sa.Column('status', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('modules', 'status')
    # ### end Alembic commands ###