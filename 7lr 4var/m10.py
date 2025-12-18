from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine("sqlite:///students.db")
Base = declarative_base()

class Student(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

new_student = Student(name="Георгий", age=24)

session.add(new_student)
session.commit()

students = session.query(Student).all()
for s in students:
    print(s.id, s.name, s.age)

session.close()