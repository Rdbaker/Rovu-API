"""Adds event.start_datetime and event.end_datetime

Revision ID: de77d4164a20
Revises: 993142283a07
Create Date: 2016-10-31 21:18:17.501251

"""

# revision identifiers, used by Alembic.
revision = 'de77d4164a20'
down_revision = '993142283a07'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('events', sa.Column('end_datetime', sa.DateTime(), nullable=True))
    op.add_column('events', sa.Column('start_datetime', sa.DateTime(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('events', 'start_datetime')
    op.drop_column('events', 'end_datetime')
    ### end Alembic commands ###
