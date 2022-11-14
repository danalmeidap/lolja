"""relationship

Revision ID: 4fa78a1a0cb8
Revises: 64e946e0f23b
Create Date: 2022-11-11 15:14:27.349424

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4fa78a1a0cb8'
down_revision = '64e946e0f23b'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('product', schema=None) as batch_op:
        batch_op.create_foreign_key('fk_user', 'user', ['user_id'], ['id'])

    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('password', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('phonee', sa.String(), nullable=True))
        batch_op.drop_column('phone')

    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('phone', sa.VARCHAR(), nullable=True))
        batch_op.drop_column('phonee')
        batch_op.drop_column('password')

    with op.batch_alter_table('product', schema=None) as batch_op:
        batch_op.drop_constraint('fk_user', type_='foreignkey')

    # ### end Alembic commands ###
