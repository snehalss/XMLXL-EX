"""empty message

Revision ID: c818e2cf17fc
Revises: 
Create Date: 2021-03-31 17:11:42.818812

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c818e2cf17fc'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=60), nullable=False),
    sa.Column('password_hash', sa.String(length=128), nullable=False),
    sa.Column('verified', sa.Boolean(), nullable=False),
    sa.Column('first_name', sa.String(length=40), nullable=False),
    sa.Column('last_name', sa.String(length=40), nullable=False),
    sa.Column('date_register', sa.DateTime(), nullable=False),
    sa.Column('ip_register', sa.String(length=45), nullable=False),
    sa.Column('company', sa.String(length=60), nullable=True),
    sa.Column('balance_qty', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_email'), 'user', ['email'], unique=True)
    op.create_table('excel_file',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('upload_date', sa.DateTime(), nullable=False),
    sa.Column('file_upload_name', sa.String(length=60), nullable=False),
    sa.Column('file_name', sa.String(length=30), nullable=False),
    sa.Column('validation_status', sa.String(length=20), nullable=False),
    sa.Column('is_valid', sa.Boolean(), nullable=False),
    sa.Column('validation_report', sa.Text(), nullable=False),
    sa.Column('processing_status', sa.String(length=20), nullable=False),
    sa.Column('is_processed', sa.Boolean(), nullable=False),
    sa.Column('no_of_records', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('file_name')
    )
    op.create_table('transaction',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('ref_transact', sa.String(length=40), nullable=False),
    sa.Column('transaction_status', sa.String(length=40), nullable=False),
    sa.Column('date_transact', sa.DateTime(), nullable=False),
    sa.Column('ip_transact', sa.String(length=45), nullable=False),
    sa.Column('purchase_qty', sa.Integer(), nullable=False),
    sa.Column('amt', sa.Numeric(precision=10, scale=2), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('transaction')
    op.drop_table('excel_file')
    op.drop_index(op.f('ix_user_email'), table_name='user')
    op.drop_table('user')
    # ### end Alembic commands ###
