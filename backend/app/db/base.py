# Import all the models, so that Base has them before being
# imported by Alembic
from backend.app.models.base import Base  # noqa
from backend.app.models.db import *  # noqa
