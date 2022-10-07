"""add content column to post table

Revision ID: 5c154ad1ec7f
Revises: b1d29e23fefd
Create Date: 2022-10-07 14:48:07.651052

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5c154ad1ec7f'
down_revision = 'b1d29e23fefd'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
