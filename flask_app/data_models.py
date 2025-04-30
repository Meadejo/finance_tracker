"""
Holds the ORM models for SQLAlchemy.
"""

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Optional
import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from flask_app import db, login

# region BaseModels
Base = db.Model
class Common:
    """
    TODOC
    """

    id:                 Mapped[int]         = mapped_column(
                                            primary_key=True)
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
# endregion BaseModel

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
# endregion Enums

# region User
@dataclass
class User(UserMixin, Base, Common):
    """
    TODOC
    """
    __tablename__   = 'users'

    username:           Mapped[str]         = mapped_column(
                                            sa.String(64), index=True, unique=True)
    email:              Mapped[str]         = mapped_column(sa.String(64), index=True, unique=True)
    pass_hash:          Mapped[Optional[str]]       = mapped_column(sa.String(256))
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
class Account(Base, CommonEntity):
    """
    TODOC
    """
    __tablename__   = 'accounts'

    name:               Mapped[str]         = mapped_column(sa.String(64), unique=True)
    type_id:            Mapped[int]         = mapped_column()
    tag_ids:            Mapped[Optional[int]]       = mapped_column()
    institution_id:     Mapped[int]         = mapped_column()
    active:             Mapped[bool]        = mapped_column(default=True)
    account_number:     Mapped[Optional[int]]       = mapped_column()
    comment:            Mapped[Optional[str]]       = mapped_column()
    abbreviation:       Mapped[Optional[str]]       = mapped_column()
    date_open:          Mapped[datetime]            = mapped_column()
    date_close:         Mapped[Optional[datetime]]  = mapped_column()
    balance_beginning:  Mapped[int]         = mapped_column(default=0)
# endregion Account
