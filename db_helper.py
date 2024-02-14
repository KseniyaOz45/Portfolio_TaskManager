from sqlalchemy import create_engine, Column, Integer, String, Date
from sqlalchemy.orm import declarative_base, Session

Base = declarative_base()


class Task(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String)
    description = Column(String)
    start_date = Column(Date)
    expiration_date = Column(Date)
    status = Column(String)


class DB_helper():
    def __init__(self):
        self.sqlite_database = "sqlite:///player.db"
        self.engine = create_engine(self.sqlite_database, echo=True)

    def create_tables(self):
        Base.metadata.create_all(bind=self.engine)

    def get_task_by_id(self, task_id):
        with Session(autoflush=True, bind=self.engine) as db:
            return db.query(Task).filter(Task.id == task_id).first()

    def create_new_task(self, data):
        try:
            task_name = data['task_name']
            task_description = data['task_desc']
            start_date = data['start_date']
            expiration_date = data['exp_date']
            status = data['status']

            task = Task(name=task_name, description=task_description, start_date=start_date,
                        expiration_date=expiration_date, status=status)

            with Session(autoflush=False, bind=self.engine) as db:
                db.add(task)
                db.commit()
            return 'Task successfully added!'
        except Exception as e:
            return f'Problem: {e}'

    def update_checked_task(self, data):
        try:
            task_id = data['id']
            task_name = data['task_name']
            task_description = data['task_desc']
            task_expiration_date = data['exp_date']
            task_status = data['status']

            with Session(autoflush=False, bind=self.engine) as db:
                task = self.get_task_by_id(task_id)
                task.name = task_name
                task.description = task_description
                task.expiration_date = task_expiration_date
                task.status = task_status
                db.commit()

            return 'Task successfully updated!'
        except Exception as e:
            return f'Problem: {e}'

    def delete_checked_task(self, task_id):
        try:
            with Session(autoflush=True, bind=self.engine) as db:
                task = self.get_task_by_id(task_id)
                db.delete(task)
                db.commit()
            return 'Task successfully deleted!'
        except Exception as e:
            return f'Problem: {e}'

    def get_completed_uncompleted_tasks(self, type):
        with Session(autoflush=True, bind=self.engine) as db:
            return db.query(Task).filter(Task.status == type).all()

    def delete_all_uncompleted_tasks(self):
        try:
            with Session(autoflush=True, bind=self.engine) as db:
                actual_tasks = self.get_completed_uncompleted_tasks('Uncomplete')
                for task in actual_tasks:
                    db.delete(task)
                db.commit()

            return 'All uncompleted tasks successfully deleted!'
        except Exception as e:
            return f'Problem: {e}'

    def delete_all_completed_tasks(self):
        try:
            with Session(autoflush=True, bind=self.engine) as db:
                complete_tasks = self.get_completed_uncompleted_tasks('Complete')
                for task in complete_tasks:
                    db.delete(task)
                db.commit()

            return 'All completed tasks successfully deleted!'
        except Exception as e:
            return f'Problem: {e}'
