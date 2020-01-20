from app.models import db
from app.models.user import User
from app.models.organisation import Organisation
from sqlalchemy import inspect

from app.models.model_mixin import ModelMixin


class OrganisationMembers(ModelMixin):

    _tablename_ = "organisation_members"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column('user_id', db.Integer, db.ForeignKey(User.id, ondelete='CASCADE'), nullable=False)
    organisation_id = db.Column("organisation_id", db.Integer, db.ForeignKey(Organisation.id, ondelete='CASCADE'), nullable=False)
    is_admin = db.Column("is_admin", db.Boolean, default=False)

    def __init__(self, user_id, organisation_id, is_admin):
        """ initialize with name, member and namespace """  
        self.user_id = user_id
        self.organisation_id = organisation_id
        self.is_admin = is_admin