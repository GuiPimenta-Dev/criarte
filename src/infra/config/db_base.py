from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class DBConnectionHandler:
    """Sqlalchemy database connection"""

    def __init__(
        self,
        # connection_string: str = "sqlite:///storage.db",
        connection_string: str = "postgresql://u33e8fbnmaqtf:p50c8d0272f61fb2f222daeac64419a12b895c061ae78d0420315686dd8e199a3@c75md5273sp6lj.cluster-czrs8kj4isg7.us-east-1.rds.amazonaws.com:5432/d2p259nu3fk1gj",
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
