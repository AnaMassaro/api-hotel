"""empty message

Revision ID: 022e09590f00
Revises: f92a06135002
Create Date: 2021-12-01 12:40:23.032836

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '022e09590f00'
down_revision = 'f92a06135002'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('bedrooms', 'enabled')
    op.drop_column('bedrooms', 'status')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('bedrooms', sa.Column('status', sa.BOOLEAN(), autoincrement=False, nullable=True))
    op.add_column('bedrooms', sa.Column('enabled', sa.BOOLEAN(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
