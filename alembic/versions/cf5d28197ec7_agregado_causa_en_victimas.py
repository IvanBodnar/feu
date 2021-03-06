"""Agregado causa en victimas

Revision ID: cf5d28197ec7
Revises: 5a99f49b3969
Create Date: 2016-07-27 17:50:46.412491

"""

# revision identifiers, used by Alembic.
revision = 'cf5d28197ec7'
down_revision = '5a99f49b3969'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    #op.drop_table('spatial_ref_sys')
    op.add_column('victimas', sa.Column('causa', sa.String(length=20), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('victimas', 'causa')
    op.create_table('spatial_ref_sys',
    sa.Column('srid', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('auth_name', sa.VARCHAR(length=256), autoincrement=False, nullable=True),
    sa.Column('auth_srid', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('srtext', sa.VARCHAR(length=2048), autoincrement=False, nullable=True),
    sa.Column('proj4text', sa.VARCHAR(length=2048), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('srid', name='spatial_ref_sys_pkey')
    )
    ### end Alembic commands ###
