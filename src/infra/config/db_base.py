from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class DBConnectionHandler:
    """Sqlalchemy database connection"""

    def __init__(
        self,
        # connection_string: str = "postgresql://ygccjjrhcuhehb:879e6cf0cd0098e94aed9ee74d16b56e554e86f541f5ce7a0289290a86dc1fab@ec2-54-157-16-196.compute-1.amazonaws.com:5432/d81btt8epi0uet",
        connection_string: str = "postgresql://uqqnleofaktyiu:7a49ed95e253e9789b81831a1df3ada326001d32071dbcd5d7f61824b47a041f@ec2-54-160-109-68.compute-1.amazonaws.com:5432/dcsagqqhi2igg6",
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
