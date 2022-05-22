import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

load_dotenv()

USER = os.getenv("POSTGRES_USER")
PASSWORD = os.getenv("POSTGRES_PASSWORD")


class DBConnectionHandler:
    """Sqlalchemy database connection"""

    def __init__(
        self,
        connection_string: str = f"postgres://tsguprjeiprhcs:175e95b3f4f7bfa505d278d77fa71e3a41f122420f9957d131cccf673fd62b58@ec2-34-236-94-53.compute-1.amazonaws.com:5432/d76jetv9q8tm70",
    ):
        self.__connection_string = connection_string
        self.session = None

    def get_engine(self):
        """Return connection Engine"""
        return create_engine(self.__connection_string)

    def __enter__(self):
        engine = create_engine(self.__connection_string)
        session_maker = sessionmaker()
        self.session = session_maker(bind=engine)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()
