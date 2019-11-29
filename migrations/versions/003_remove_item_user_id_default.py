"""remove Item.user_id default

Revision ID: 003
Revises: 002
Create Date: 2019-11-18 23:31:18.426003

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '003'
down_revision = '002'
branch_labels = None
depends_on = None


def upgrade():
    with op.batch_alter_table('item') as batch_op:
        batch_op.alter_column('user_id', server_default=None)


def downgrade():
    with op.batch_alter_table('item') as batch_op:
        op.alter_column('user_id', server_default='')
