"""add crm_notes table"""

from alembic import op
import sqlalchemy as sa
import enum

revision = "2024_10_02_add_crm"
down_revision = "2024_10_01_add_leads"
branch_labels = None
depends_on = None


class Stage(enum.Enum):
    novo_lead = "novo_lead"
    contato = "contato"
    proposta = "proposta"
    negociacao = "negociacao"
    fechado = "fechado"


def upgrade():
    op.create_table(
        "crm_notes",
        sa.Column("id", sa.Integer(), primary_key=True, nullable=False),
        sa.Column("lead_id", sa.Integer(), nullable=False),
        sa.Column("stage", sa.Enum(Stage), nullable=False),
        sa.Column("note", sa.String(), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.text("now()"), nullable=True),
        sa.ForeignKeyConstraint(["lead_id"], ["leads.id"], ondelete="CASCADE"),
    )


def downgrade():
    op.drop_table("crm_notes")
