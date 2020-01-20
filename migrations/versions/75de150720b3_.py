"""empty message

Revision ID: 75de150720b3
Revises: 2af754f3a297
Create Date: 2020-01-20 19:19:48.780653

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '75de150720b3'
down_revision = '2af754f3a297'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('role',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('uuid', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('name', sa.String(length=256), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name', name='org_unique_name'),
    sa.UniqueConstraint('uuid')
    )
    op.drop_table('organisation_members')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('organisation_members',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('organisation_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('is_admin', sa.BOOLEAN(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['organisation_id'], ['organisation.id'], name='organisation_members_organisation_id_fkey', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name='organisation_members_user_id_fkey', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id', name='organisation_members_pkey')
    )
    op.drop_table('role')
    # ### end Alembic commands ###
