"""add user ownership to students

Revision ID: cbf6273f4fbb
Revises: 
Create Date: 2026-11-01 22:34:41.234846

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'cbf6273f4fbb'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None




def upgrade() -> None:
    # 1. Add user_id as nullable temporarily
    op.add_column(
        "students",
        sa.Column("user_id", sa.Integer(), nullable=True)
    )

    # 2. Assign existing students to User ID 1
    op.execute(
        "UPDATE students SET user_id = 1"
    )

    # 3. Add foreign key constraint
    op.create_foreign_key(
        "fk_students_user_id_users",
        "students",
        "users",
        ["user_id"],
        ["id"]
    )

    # 4. Make user_id mandatory
    op.alter_column(
        "students",
        "user_id",
        existing_type=sa.Integer(),
        nullable=False
    )


def downgrade() -> None:
    op.drop_constraint(
        "fk_students_user_id_users",
        "students",
        type_="foreignkey"
    )

    op.drop_column("students", "user_id")
