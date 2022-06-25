from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class DBConnectionHandler:
    """Sqlalchemy database connection"""

    def __init__(
        self,
        # connection_string: str = "postgresql://tsguprjeiprhcs:175e95b3f4f7bfa505d278d77fa71e3a41f122420f9957d131cccf673fd62b58@ec2-34-236-94-53.compute-1.amazonaws.com:5432/d76jetv9q8tm70",
        connection_string: str = "postgres://ygccjjrhcuhehb:879e6cf0cd0098e94aed9ee74d16b56e554e86f541f5ce7a0289290a86dc1fab@ec2-54-157-16-196.compute-1.amazonaws.com:5432/d81btt8epi0uet",
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
