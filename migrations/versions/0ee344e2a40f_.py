"""Removes NOT NULL constraints from events.[eb_id|eb_name_html|eb_url]

Revision ID: 0ee344e2a40f
Revises: f5f1634285bb
Create Date: 2016-11-08 19:05:45.406952

"""

# revision identifiers, used by Alembic.
revision = '0ee344e2a40f'
down_revision = 'f5f1634285bb'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('events', 'eb_id',
               existing_type=sa.VARCHAR(length=90),
               nullable=True)
    op.alter_column('events', 'eb_name_html',
               existing_type=sa.VARCHAR(length=255),
               nullable=True)
    op.alter_column('events', 'eb_url',
               existing_type=sa.VARCHAR(length=255),
               nullable=True)
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('events', 'eb_url',
               existing_type=sa.VARCHAR(length=255),
               nullable=False)
    op.alter_column('events', 'eb_name_html',
               existing_type=sa.VARCHAR(length=255),
               nullable=False)
    op.alter_column('events', 'eb_id',
               existing_type=sa.VARCHAR(length=90),
               nullable=False)
    ### end Alembic commands ###