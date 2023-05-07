"""empty message

Revision ID: 004623cac4db
Revises: 9af535793a9b
Create Date: 2023-05-07 13:17:31.523718

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '004623cac4db'
down_revision = '9af535793a9b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('book_genre',
    sa.Column('book_id', sa.Integer(), nullable=False),
    sa.Column('genre_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['book_id'], ['book.id'], ),
    sa.ForeignKeyConstraint(['genre_id'], ['genre.id'], ),
    sa.PrimaryKeyConstraint('book_id', 'genre_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('book_genre')
    # ### end Alembic commands ###
