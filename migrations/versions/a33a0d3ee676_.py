"""empty message

Revision ID: a33a0d3ee676
Revises: e4304b68fdb8
Create Date: 2020-02-27 04:21:23.718865

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a33a0d3ee676'
down_revision = 'e4304b68fdb8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('family', sa.Column('public_id', sa.String(length=50), nullable=True))
    op.create_unique_constraint(None, 'family', ['public_id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'family', type_='unique')
    op.drop_column('family', 'public_id')
    # ### end Alembic commands ###
