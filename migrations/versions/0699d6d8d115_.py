"""empty message

Revision ID: 0699d6d8d115
Revises: 7bc933054a98
Create Date: 2023-01-26 01:19:39.139569

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0699d6d8d115'
down_revision = '7bc933054a98'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('funcionarios', schema=None) as batch_op:
        batch_op.add_column(sa.Column('password_hash', sa.LargeBinary(length=120), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('funcionarios', schema=None) as batch_op:
        batch_op.drop_column('password_hash')

    # ### end Alembic commands ###
