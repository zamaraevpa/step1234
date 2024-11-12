import os


def get_postgres_database_uri():
    sql_user = os.getenv("SQL_USER")

    if "SQL_PASSWORD" in os.environ:
        sql_password = os.getenv("SQL_PASSWORD")
        print("DB password was read from env")
    elif "SQL_PASSWORD_FILE" in os.environ:
        password_file_path = os.getenv('SQL_PASSWORD_FILE')
        if password_file_path and os.path.isfile(password_file_path):
            with open(password_file_path) as f:
                sql_password = f.read().strip()
                print("DB password was read from secret file")
        else:
            raise ValueError("Path to SQL password file is not set or file does not exist")

    sql_host = os.getenv("SQL_HOST")
    sql_port = os.getenv("SQL_PORT")
    sql_database = os.getenv("SQL_DATABASE")
    return f"postgresql://{sql_user}:{sql_password}@{sql_host}:{sql_port}/{sql_database}"