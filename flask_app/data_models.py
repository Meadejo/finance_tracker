"""
Holds the ORM models for SQLAlchemy.
"""

from datetime import datetime, timezone, timedelta
import secrets
from typing import Optional
from flask import url_for
import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from flask_app import db, login

# region Base+Mixins
Base = db.Model
class Common:
    """
    TODOC
    """

    id:                 Mapped[int]         = mapped_column(
                                            primary_key=True)
    active:             Mapped[bool]        = mapped_column(default=True)
    created_at:         Mapped[datetime]    = mapped_column(
                                            default=lambda: datetime.now(timezone.utc))
    updated_at:         Mapped[datetime]    = mapped_column(
                                            default=lambda: datetime.now(timezone.utc),
                                            onupdate=lambda: datetime.now(timezone.utc))

class CommonEntity(Common):
    """
    TODOC
    """

    name:               Mapped[str]         = mapped_column(sa.String(64), index=True, unique=True)

class PaginatedAPIMixin(object):
    """
    TODOC
    """
    @staticmethod
    def to_collection_dict(query, page, per_page, endpoint, **kwargs):
        """
        TODOC
        """
        resources = db.paginate(query, page=page, per_page=per_page, error_out=False)
        data = {
            'items': [item.to_dict() for item in resources.items],
            '_meta': {
                'page': page,
                'per_page': per_page,
                'total_pages': resources.pages,
                'total_items': resources.total
            },
            '_links': {
                'self': url_for(endpoint, page=page, per_page=per_page,
                                **kwargs),
                'next': url_for(endpoint, page=page + 1, per_page=per_page,
                                **kwargs) if resources.has_next else None,
                'prev': url_for(endpoint, page=page - 1, per_page=per_page,
                                **kwargs) if resources.has_prev else None
            }
        }
        return data
# endregion Base+Mixins

# region Enums
# These aren't _TECHNICALLY_ enums, but they may as well be.
class CategoryType(Base, CommonEntity):
    """
    TODOC
    """
    __tablename__   = 'category_types'

class TransactionType(Base, CommonEntity):
    """
    TODOC
    """
    __tablename__   = 'transaction_types'

class TransactionStatus(Base, CommonEntity):
    """
    TODOC
    """
    __tablename__   = 'transaction_statuses'

class Tag(Base, CommonEntity):
    """
    TODOC
    """
    __tablename__   = 'tags'
    def to_list_edit(self):
        """
        Used when shaping items to view on admin/list_edit.html
        """
        return [self.name]
# endregion Enums

# region User
class User(UserMixin, Base, Common):
    """
    TODOC
    """
    __tablename__   = 'users'

    username:           Mapped[str]         = mapped_column(
                                            sa.String(64), index=True, unique=True)
    email:              Mapped[str]         = mapped_column(sa.String(64), index=True, unique=True)
    pass_hash:          Mapped[Optional[str]]       = mapped_column(sa.String(256))
    token:              Mapped[Optional[str]]       = mapped_column(sa.String(32), 
                                                                    index=True, unique=True)
    token_expiration:   Mapped[Optional[datetime]]
    last_seen:          Mapped[Optional[datetime]]  = mapped_column(
                                            default=lambda: datetime.now(timezone.utc))

    def __repr__(self):
        return "User: " + format(self.username)

    def display_name(self):
        """
        TODOC
        """
        return format(self.username).title()

    def set_password(self, password):
        """
        TODOC
        """
        self.pass_hash = generate_password_hash(password)

    def check_password(self, password):
        """
        TODOC
        """
        return check_password_hash(self.pass_hash, password)

    def get_token(self, expires_in=3600):
        """
        TODOC
        """
        now = datetime.now(timezone.utc)
        if self.token and self.token_expiration.replace(
                tzinfo=timezone.utc) > now + timedelta(seconds=60):
            return self.token
        self.token = secrets.token_hex(16)
        self.token_expiration = now + timedelta(seconds=expires_in)
        db.session.add(self)
        return self.token

    def revoke_token(self):
        """
        TODOC
        """
        self.token_expiration = datetime.now(timezone.utc) - timedelta(
            seconds=1)

    @staticmethod
    def check_token(token):
        """
        TODOC
        """
        user = db.session.scalar(sa.select(User).where(User.token == token))
        if user is None or user.token_expiration.replace(
                tzinfo=timezone.utc) < datetime.now(timezone.utc):
            return None
        return user

@login.user_loader
def load_user(id):
    """
    TODOC
    """
    return db.session.get(User, int(id))
# endregion User

# region Institution
class Institution(Base, CommonEntity):
    """
    TODOC
    """
    __tablename__   = 'institutions'

    name:               Mapped[str]         = mapped_column(sa.String(64), unique=True)
    tag_ids:            Mapped[Optional[int]]       = mapped_column()
# endregion Institution

# region Account
class Account(PaginatedAPIMixin, Base, CommonEntity):
    """
    TODOC
    """
    __tablename__   = 'accounts'

    type_id:            Mapped[int]         = mapped_column()
    tag_ids:            Mapped[Optional[int]]       = mapped_column()
    institution_id:     Mapped[int]         = mapped_column()
    account_number:     Mapped[Optional[int]]       = mapped_column()
    comment:            Mapped[Optional[str]]       = mapped_column()
    abbreviation:       Mapped[Optional[str]]       = mapped_column()
    date_open:          Mapped[datetime]            = mapped_column()
    date_close:         Mapped[Optional[datetime]]  = mapped_column()
    balance_beginning:  Mapped[int]         = mapped_column(default=0)

    def to_dict(self):
        """
        TODOC
        """
        data = {
            'id':                   self.id,
            'name':                 self.name,
            # 'active':               self.active,
            'type_id':              self.type_id,
            # 'tags':                 None,
            'institution_id':       self.institution_id,
            # 'account_number':       self.account_number,
            # 'comment':              self.comment,
            # 'abbreviation':         self.abbreviation,
            'date_created':         self.created_at.replace(
                tzinfo=timezone.utc).isoformat(),
            # 'last_updated':         self.updated_at.replace(
            #     tzinfo=timezone.utc).isoformat(),
            # 'date_open':            self.date_open.replace(
            #     tzinfo=timezone.utc).isoformat(),
            # 'date_close':           self.date_close.replace(
            #     tzinfo=timezone.utc).isoformat(),
            # 'balance_beginning':    self.balance_beginning,
            '_links':               {
                'self':                 url_for('api.get_account', id=self.id)
                # 'institution':          url_for('api.get_institution', id=self.institution_id),
                # TODO Finish Him!!! (The _links set.)
            }
        }

        return data

    def from_dict(self, data):
        """
        TODOC
        """
        for field in [
            'name',
            'account_number',
            'comment',
            'abbreviation',
            'date_open',
            'date_close',
            'balance_beginning'
        ]:
            if field in data:
                setattr(self, field, data[field])
        # TODO Finish ... Her?? I guess?
# endregion Account
