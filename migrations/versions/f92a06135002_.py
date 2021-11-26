"""empty message

Revision ID: f92a06135002
Revises: 60021926ec18
Create Date: 2021-11-25 20:53:38.250705

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f92a06135002'
down_revision = '60021926ec18'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('bookings',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('id_user', sa.Integer(), nullable=True),
    sa.Column('id_bedroom', sa.Integer(), nullable=True),
    sa.Column('start_date', sa.Date(), nullable=True),
    sa.Column('end_date', sa.Date(), nullable=True),
    sa.Column('status', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['id_bedroom'], ['bedrooms.id'], ),
    sa.ForeignKeyConstraint(['id_user'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('schedules')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('schedules',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('id_user', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('id_bedroom', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('start_date', sa.DATE(), autoincrement=False, nullable=True),
    sa.Column('end_date', sa.DATE(), autoincrement=False, nullable=True),
    sa.Column('status', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['id_bedroom'], ['bedrooms.id'], name='schedules_id_bedroom_fkey'),
    sa.ForeignKeyConstraint(['id_user'], ['users.id'], name='schedules_id_user_fkey'),
    sa.PrimaryKeyConstraint('id', name='schedules_pkey')
    )
    op.drop_table('bookings')
    # ### end Alembic commands ###
