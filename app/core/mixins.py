from datetime import datetime

from sqlalchemy import DATETIME, func
from sqlalchemy.orm import Mapped, mapped_column


class TimestampMixin:

    created_at: Mapped[datetime] = mapped_column(DATETIME(timezone=True),
                                                 server_default=func.now(),
                                                 nullable=False)

    updated_at: Mapped[datetime] =  mapped_column(DATETIME(timezone=True),
                                                  nullable=True,
                                                  onupdate=func.now())