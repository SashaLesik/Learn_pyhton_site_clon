""" news tables_3

Revision ID: 09abe73d070f
Revises: 74fdb77da403
Create Date: 2024-01-18 14:44:57.789943

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '09abe73d070f'
down_revision = '74fdb77da403'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('olx_site', sa.Column('origin_id', sa.String(), nullable=True))
    op.add_column('olx_site', sa.Column('number_of_views', sa.Integer(), nullable=True))
    op.create_unique_constraint(None, 'olx_site', ['origin_id'])
    op.drop_column('olx_site', 'number_of_looks')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('olx_site', sa.Column('number_of_looks', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'olx_site', type_='unique')
    op.drop_column('olx_site', 'number_of_views')
    op.drop_column('olx_site', 'origin_id')
    # ### end Alembic commands ###
