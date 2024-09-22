from src.interfaces.db import get_session


class SQLAlchemyRepo:
    def __init__(self, session: get_session):
        self.session = session
