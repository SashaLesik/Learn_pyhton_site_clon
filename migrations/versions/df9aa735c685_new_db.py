"""new db

Revision ID: df9aa735c685
Revises: 
Create Date: 2024-01-10 20:53:59.198909

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = 'df9aa735c685'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('olx_site', sa.Column('url', sa.String(), nullable=True))
    op.add_column('olx_site', sa.Column('date_registered', sa.DateTime(), nullable=True))
    op.add_column('olx_site', sa.Column('date_of_last_visit', sa.DateTime(), nullable=True))
    op.add_column('olx_site', sa.Column('date_posted', sa.DateTime(), nullable=True))
    op.alter_column('olx_site', 'phone_number',
               existing_type=sa.INTEGER(),
               type_=sa.String(),
               existing_nullable=True)
    op.drop_constraint('olx_site_picture_key', 'olx_site', type_='unique')
    op.create_unique_constraint(None, 'olx_site', ['url'])
    op.drop_column('olx_site', 'registration_date')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('olx_site', sa.Column('registration_date', postgresql.TIMESTAMP(), autoincrement=False, nullable=False))
    op.drop_constraint(None, 'olx_site', type_='unique')
    op.create_unique_constraint('olx_site_picture_key', 'olx_site', ['picture'])
    op.alter_column('olx_site', 'phone_number',
               existing_type=sa.String(),
               type_=sa.INTEGER(),
               existing_nullable=True)
    op.drop_column('olx_site', 'date_posted')
    op.drop_column('olx_site', 'date_of_last_visit')
    op.drop_column('olx_site', 'date_registered')
    op.drop_column('olx_site', 'url')
    # ### end Alembic commands ###
