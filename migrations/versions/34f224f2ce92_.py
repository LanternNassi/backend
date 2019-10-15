"""empty message

Revision ID: 34f224f2ce92
Revises: 1f87208a9d1e
Create Date: 2019-09-26 10:26:06.911770

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '34f224f2ce92'
down_revision = '1f87208a9d1e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint('customer_unique_name', 'organisation', ['name'])
    op.alter_column('organisation_members', 'organisation_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('organisation_members', 'user_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.drop_constraint('organisation_members_organisation_id_fkey', 'organisation_members', type_='foreignkey')
    op.drop_constraint('organisation_members_user_id_fkey', 'organisation_members', type_='foreignkey')
    op.create_foreign_key(None, 'organisation_members', 'user', ['user_id'], ['id'], ondelete='CASCADE')
    op.create_foreign_key(None, 'organisation_members', 'organisation', ['organisation_id'], ['id'], ondelete='CASCADE')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'organisation_members', type_='foreignkey')
    op.drop_constraint(None, 'organisation_members', type_='foreignkey')
    op.create_foreign_key('organisation_members_user_id_fkey', 'organisation_members', 'user', ['user_id'], ['id'])
    op.create_foreign_key('organisation_members_organisation_id_fkey', 'organisation_members', 'organisation', ['organisation_id'], ['id'])
    op.alter_column('organisation_members', 'user_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('organisation_members', 'organisation_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.drop_constraint('customer_unique_name', 'organisation', type_='unique')
    # ### end Alembic commands ###
