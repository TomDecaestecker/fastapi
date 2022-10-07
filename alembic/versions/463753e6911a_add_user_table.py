"""add user table

Revision ID: 463753e6911a
Revises: 5c154ad1ec7f
Create Date: 2022-10-07 14:54:43.746010

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '463753e6911a'
down_revision = '5c154ad1ec7f'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('users',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('email', sa.String(), nullable=False),
                    sa.Column('password', sa.String(), nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True),
                              server_default=sa.text('now()'), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email'))
    pass


def downgrade() -> None:
    op.drop_table('users')
    pass
