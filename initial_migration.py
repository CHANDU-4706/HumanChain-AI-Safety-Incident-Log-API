"""Initial migration

Revision ID: initial_migration
Revises: 
Create Date: 2024-02-20

"""
from alembic import op
import sqlalchemy as sa
from datetime import datetime

# revision identifiers, used by Alembic.
revision = 'initial_migration'
down_revision = None
branch_labels = None
depends_on = None

def upgrade() -> None:
    # Create enum type for severity
    op.execute("CREATE TYPE severitylevel AS ENUM ('Low', 'Medium', 'High')")
    
    # Create incidents table
    op.create_table(
        'incidents',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('title', sa.String(length=255), nullable=False),
        sa.Column('description', sa.Text(), nullable=False),
        sa.Column('severity', sa.Enum('Low', 'Medium', 'High', name='severitylevel'), nullable=False),
        sa.Column('reported_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )
    
    # Create index on id
    op.create_index(op.f('ix_incidents_id'), 'incidents', ['id'], unique=False)
    
    # Insert sample data
    op.execute("""
    INSERT INTO incidents (title, description, severity) VALUES
    ('Unexpected Model Output', 'AI model generated potentially harmful content during testing phase', 'High'),
    ('Training Data Bias', 'Discovered significant bias in training dataset affecting model decisions', 'Medium'),
    ('Resource Overconsumption', 'AI system consumed excessive computational resources during operation', 'Low')
    """)

def downgrade() -> None:
    # Drop table and index
    op.drop_index(op.f('ix_incidents_id'), table_name='incidents')
    op.drop_table('incidents')
    
    # Drop enum type
    op.execute("DROP TYPE severitylevel") 