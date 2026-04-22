"""add leads tables"""

from alembic import op
import sqlalchemy as sa
import enum

revision = "2024_10_01_add_leads"
down_revision = None      # ajuste se houver migration anterior
branch_labels = None
depends_on = None


class LeadStatus(enum.Enum):
    quente = "quente"
    morno = "morno"
    frio = "frio"
    fechado = "fechado"


def upgrade():
    op.create_table(
        "leads",
        sa.Column("id", sa.Integer(), primary_key=True, nullable=False),
        sa.Column("nome", sa.String(length=120), nullable=False),
        sa.Column("whatsapp", sa.String(length=30), nullable=False, unique=True),
        sa.Column("origem", sa.String(length=80), nullable=True),
        sa.Column("status", sa.Enum(LeadStatus), nullable=False, server_default="frio"),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.text("now()"), nullable=True),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=True),
    )
    op.create_index(op.f("ix_leads_whatsapp"), "leads", ["whatsapp"], unique=True)
    op.create_index(op.f("ix_leads_status"), "leads", ["status"], unique=False)

    op.create_table(
        "tags",
        sa.Column("id", sa.Integer(), primary_key=True, nullable=False),
        sa.Column("name", sa.String(length=30), nullable=False, unique=True),
    )
    op.create_table(
        "lead_tag",
        sa.Column("lead_id", sa.Integer(), nullable=False),
        sa.Column("tag_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(["lead_id"], ["leads.id"], ondelete="CASCADE"),
        sa.ForeignKeyConstraint(["tag_id"], ["tags.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("lead_id", "tag_id"),
    )


def downgrade():
    op.drop_table("lead_tag")
    op.drop_table("tags")
    op.drop_index(op.f("ix_leads_status"), table_name="leads")
    op.drop_index(op.f("ix_leads_whatsapp"), table_name="leads")
    op.drop_table("leads")
