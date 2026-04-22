"""add sales_logs table"""

from alembic import op
import sqlalchemy as sa

revision = "2024_10_03_add_sales_logs"
down_revision = "2024_10_02_add_crm"
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "sales_logs",
        sa.Column("id", sa.Integer(), primary_key=True, nullable=False),
        sa.Column("lead_id", sa.Integer(), nullable=False),
        sa.Column("message", sa.String(), nullable=False),
        sa.Column("tone", sa.String(length=30), nullable=False),
        sa.Column("chance_fechamento", sa.Float(), nullable=True),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.text("now()"), nullable=True),
        sa.ForeignKeyConstraint(["lead_id"], ["leads.id"], ondelete="CASCADE"),
    )


def downgrade():
    op.drop_table("sales_logs")
