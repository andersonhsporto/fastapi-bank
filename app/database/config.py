import sqlparse as sqlparse
from sqlalchemy import create_engine, text
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

# DATABASE_URL = "mariadb+mariadbconnector://mariadb:mariadb@localhost:3306/mariadb"
DATABASE_URL = "mysql+pymysql://mariadb:secret@127.0.0.1:3306/mariadb"

engine = create_engine(DATABASE_URL, encoding="utf-8", echo=True)

with open("./resources/data.sql") as file:
    sql_raw = file.read()

sql_queries = sqlparse.split(
    sqlparse.format(sql_raw, strip_comments=True)
)

with engine.connect() as conn:
    for query in sql_queries:
        result = conn.execute(text(query))
        print(f"{result.rowcount} rows have been updated/selected.")

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
