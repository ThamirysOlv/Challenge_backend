"""empty message

Revision ID: 8903f49179c9
Revises: d97bd4fa1858
Create Date: 2022-02-03 12:22:55.785747

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '8903f49179c9'
down_revision = 'd97bd4fa1858'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('receitas', 'categoria',
               existing_type=mysql.VARCHAR(length=200),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('receitas', 'categoria',
               existing_type=mysql.VARCHAR(length=200),
               nullable=False)
    # ### end Alembic commands ###
