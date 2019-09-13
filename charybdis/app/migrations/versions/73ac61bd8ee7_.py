"""empty message

Revision ID: 73ac61bd8ee7
Revises: 2afa51da4fe9
Create Date: 2019-09-12 12:33:55.930597

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '73ac61bd8ee7'
down_revision = '2afa51da4fe9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('project', sa.Column('slug', sa.String(), nullable=False))
    op.add_column('user', sa.Column('is_active', sa.Boolean(), server_default='true', nullable=True))
    op.add_column('user', sa.Column('password_hash', sa.String(), nullable=True))
    op.add_column('user', sa.Column('role_id', sa.Integer(), nullable=False))
    op.add_column('user', sa.Column('username', sa.String(), nullable=True))
    op.create_unique_constraint(None, 'user', ['username'])
    op.create_foreign_key(None, 'user', 'user_role', ['role_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'user', type_='foreignkey')
    op.drop_constraint(None, 'user', type_='unique')
    op.drop_column('user', 'username')
    op.drop_column('user', 'role_id')
    op.drop_column('user', 'password_hash')
    op.drop_column('user', 'is_active')
    op.drop_column('project', 'slug')
    # ### end Alembic commands ###
