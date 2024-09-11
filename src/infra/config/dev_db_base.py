from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class DevDBConnectionHandler:
    """Sqlalchemy database connection"""

    def __init__(self, connection_string: str = "sqlite:///storage.db"):
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
