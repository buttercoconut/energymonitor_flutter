"""Alembic migration script for initial tables."""

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = "0001_initial"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "users",
        sa.Column("id", sa.Integer, primary_key=True, index=True),
        sa.Column("email", sa.String, unique=True, index=True, nullable=False),
        sa.Column("hashed_password", sa.String, nullable=False),
        sa.Column("is_active", sa.Boolean, default=True),
        sa.Column("created_at", sa.DateTime, default=sa.func.now()),
    )

    op.create_table(
        "buildings",
        sa.Column("id", sa.Integer, primary_key=True, index=True),
        sa.Column("name", sa.String, unique=True, nullable=False),
        sa.Column("address", sa.String),
        sa.Column("created_at", sa.DateTime, default=sa.func.now()),
    )

    op.create_table(
        "energy_records",
        sa.Column("id", sa.Integer, primary_key=True, index=True),
        sa.Column("user_id", sa.Integer, sa.ForeignKey("users.id")),
        sa.Column("building_id", sa.Integer, sa.ForeignKey("buildings.id")),
        sa.Column("timestamp", sa.DateTime, default=sa.func.now(), index=True),
        sa.Column("consumption_kwh", sa.Float, nullable=False),
    )

    op.create_table(
        "energy_tips",
        sa.Column("id", sa.Integer, primary_key=True, index=True),
        sa.Column("title", sa.String, nullable=False),
        sa.Column("description", sa.String),
        sa.Column("created_at", sa.DateTime, default=sa.func.now()),
    )


def downgrade():
    op.drop_table("energy_tips")
    op.drop_table("energy_records")
    op.drop_table("buildings")
    op.drop_table("users")
