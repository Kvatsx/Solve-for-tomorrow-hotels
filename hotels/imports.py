from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine("postgres://cuhpqttlfncjia:ab42abc2241221dcd463d198a2c561fe0d1398137ac9945c1c749c5a932a088d@ec2-52-204-232-46.compute-1.amazonaws.com:5432/d2qn5k3635hjih")
db = scoped_session(sessionmaker(bind=engine))

def main():
    create_tables()


def create_tables():

    # Clean Database
    # db.execute("DROP TABLE Users;")

    # Create Tables
    db.execute('''
        CREATE TABLE Users (
            id SERIAL PRIMARY KEY,
            name VARCHAR NOT NULL,
            email VARCHAR NOT NULL UNIQUE,
            password VARCHAR NOT NULL
        );
    ''')

    db.commit()

if __name__ == "__main__":
    main()