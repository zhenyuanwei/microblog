"""added one column to users table3

Revision ID: c85a1f5ec257
Revises: cc25bf87b691
Create Date: 2017-08-15 08:58:24.591367

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c85a1f5ec257'
down_revision = 'cc25bf87b691'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('last_seen', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'last_seen')
    # ### end Alembic commands ###
