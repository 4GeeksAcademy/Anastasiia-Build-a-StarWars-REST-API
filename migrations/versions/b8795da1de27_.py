"""empty message

Revision ID: b8795da1de27
Revises: d7b6118a238f
Create Date: 2023-12-23 16:49:51.632733

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b8795da1de27'
down_revision = 'd7b6118a238f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('FavoritePeople',
    sa.Column('userId', sa.Integer(), nullable=False),
    sa.Column('peopleId', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['peopleId'], ['people.id'], ),
    sa.ForeignKeyConstraint(['userId'], ['user.id'], ),
    sa.PrimaryKeyConstraint('userId', 'peopleId')
    )
    op.create_table('FavoritePlanets',
    sa.Column('userId', sa.Integer(), nullable=False),
    sa.Column('planetsId', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['planetsId'], ['planets.id'], ),
    sa.ForeignKeyConstraint(['userId'], ['user.id'], ),
    sa.PrimaryKeyConstraint('userId', 'planetsId')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('FavoritePlanets')
    op.drop_table('FavoritePeople')
    # ### end Alembic commands ###