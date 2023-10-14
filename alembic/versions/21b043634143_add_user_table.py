"""add user table

Revision ID: 21b043634143
Revises: f3aa7db2d766
Create Date: 2023-10-14 02:25:50.048800

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "21b043634143"
down_revision: Union[str, None] = "f3aa7db2d766"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
