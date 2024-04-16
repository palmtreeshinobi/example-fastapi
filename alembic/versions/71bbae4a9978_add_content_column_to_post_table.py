"""add content column to post table

Revision ID: 71bbae4a9978
Revises: 13f366374737
Create Date: 2024-04-16 11:40:04.016641

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '71bbae4a9978'
down_revision: Union[str, None] = '13f366374737'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String, nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
