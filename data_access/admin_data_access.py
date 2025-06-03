import model

from data_access.base_data_access import BaseDataAccess


class AdminDataAccess(BaseDataAccess):
    def __init__(self, db_path: str = None):
        super().__init__(db_path)

