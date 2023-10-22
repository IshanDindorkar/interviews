"""
Singleton Design Pattern:
The Singleton pattern ensures that a class has only one instance and provides a
global point of access to it. It is used when you want to limit object creation
for a class to only one instance.
"""
from loguru import logger


class DatabaseConnection:
    _instance = None

    @staticmethod
    def get_instance(username: str, password: str):
        if DatabaseConnection._instance is None:
            DatabaseConnection._instance = DatabaseConnection(username=username, password=password)
        return DatabaseConnection._instance

    def __init__(self, username: str, password: str):
        if DatabaseConnection._instance is not None:
            logger.error("DatabaseConnection is Singleton class, cannot be re-instantiated")
        else:
            self._username = username
            self._password = password

    @property
    def username(self):
        return self._username

    @property
    def password(self):
        return self._password


def main():
    db_conn = DatabaseConnection.get_instance(username="abc", password="def")
    logger.debug(f"Username: {db_conn.username}")
    logger.debug(f"Password: {db_conn.password}")

    dup_db_conn = DatabaseConnection(username="abc", password="def")  # this will lead to an error!


if __name__ == "__main__":
    main()

# EOF
