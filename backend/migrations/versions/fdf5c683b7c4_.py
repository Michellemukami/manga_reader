"""empty message

Revision ID: fdf5c683b7c4
Revises: cee4e2707d80
Create Date: 2021-04-07 19:24:29.905600

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fdf5c683b7c4'
down_revision = 'cee4e2707d80'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('manga_chap_details',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('manga_details_id', sa.Integer(), nullable=False),
    sa.Column('manga_chap_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['manga_chap_id'], ['manga_chapter.id'], ),
    sa.ForeignKeyConstraint(['manga_details_id'], ['manga_details.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('manga_details', sa.Column('title', sa.String(length=100), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('manga_details', 'title')
    op.drop_table('manga_chap_details')
    # ### end Alembic commands ###
