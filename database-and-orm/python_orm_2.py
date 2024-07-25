# This is an sqlalchemy script for creating user profile table, and also populate some data into the table
import sqlalchemy as sq
from sqlalchemy import select
from sqlalchemy.orm import Session
from sqlalchemy.orm import declarative_base


Base = declarative_base()


class UserProfile(Base):
    """User profile table"""

    __tablename__ = "profile"

    id = sq.Column(sq.Integer, primary_key=True)
    fullname = sq.Column(sq.String(30), nullable=False)
    username = sq.Column(sq.String(20), nullable=False, unique=True)
    bio = sq.Column(sq.Text, nullable=True)

    # def __repr__(self):
    #     return f"repr {self.username}'s profile with an id of {self.id}"
    
    def __str__(self):
        return f"{self.username}'s profile with an id of {self.id}"
    

engine = sq.create_engine("sqlite://")
Base.metadata.create_all(engine)

sess = Session(engine)

user_1 = UserProfile(fullname="Usman Musa", username="Shehu",bio="A software engineer")
user_2 = UserProfile(fullname="Muhammad Usman", username="Tukur")
user_3 = UserProfile(fullname="Aisha Musa", username="Mami")
user_4 = UserProfile(fullname="Hadiza Ibrahim", username="Deejah")
user_5 = UserProfile(fullname="Yusuf Musa", username="Myusuf",bio="Doctor of science")

sess.add_all([user_1, user_2, user_3, user_4, user_5])
sess.commit()

stmt = select(UserProfile).where(UserProfile.username.in_(["Shehu", "Myusuf"]))
print()
print('Filtering user from database:')
for user in sess.scalars(stmt):
    print(f"  {user}\n\t{user.username}, {user.id}, {user.fullname}\n")

print()
print('Querying users from database:')
for usr in sess.query(UserProfile).all():
    print(f"  {usr.id}. {usr.fullname} ({usr.username})")
print()
