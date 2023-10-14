"""add content column to posts table

Revision ID: f3aa7db2d766
Revises: 1a0ab504f402
Create Date: 2023-10-14 02:21:30.921139

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "f3aa7db2d766"
down_revision: Union[str, None] = "1a0ab504f402"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("posts", sa.Column("content", sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column("posts", "content")
    pass
