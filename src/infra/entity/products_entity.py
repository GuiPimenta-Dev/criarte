from datetime import datetime

from sqlalchemy import Boolean, Column, Date, DateTime, Float, String
from src.infra.config import Base


class ProductEntity(Base):
    """Products Entity"""

    __tablename__ = "products"

    id = Column(String, primary_key=True)
    type = Column(String, nullable=False)
    printed_name = Column(String, nullable=False)
    theme = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    sex = Column(String, nullable=False)
    payment = Column(String, nullable=False)
    observations = Column(String, nullable=True)
    day = Column(Date, nullable=False)
    client_name = Column(String, nullable=False)
    client_address = Column(String, nullable=False)
    client_state = Column(String, nullable=False)
    cover_status = Column(Boolean, nullable=False)
    core_status = Column(Boolean, nullable=False)
    timestamp = Column(DateTime, nullable=False, default=datetime.now())

    def __repr__(self):
        return f"""Product: [
                            {self.id = },
                            {self.type = },
                            {self.printed_name = },
                            {self.theme = },
                            {self.price = },
                            {self.sex = },
                            {self.payment = },
                            {self.observations = },
                            {self.day = },
                            {self.client_name = },
                            {self.client_address = },
                            {self.client_state = },
                            {self.cover_status = },
                            {self.core_status = },
                            {self.timestamp = }
                            ]"""
