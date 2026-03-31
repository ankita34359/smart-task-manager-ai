from models import db
from models.task import Task
from utils.ai import suggest_priority
from marshmallow import ValidationError
from schemas.task_schema import task_schema, tasks_schema
import logging

logger = logging.getLogger(__name__)

class TaskService:
    @staticmethod
    def create_task(data: dict) -> dict:
        validated_data = task_schema.load(data)
        
        existing_task = Task.query.filter_by(title=validated_data['title']).first()
        if existing_task:
            raise ValueError(f"Task with title '{validated_data['title']}' already exists.")

        if 'priority' not in data and 'description' in validated_data and validated_data['description']:
            suggested_priority = suggest_priority(validated_data['description'])
            if suggested_priority in ["LOW", "MEDIUM", "HIGH"]:
                validated_data['priority'] = suggested_priority

        new_task = Task(**validated_data)
        db.session.add(new_task)
        db.session.commit()
        return task_schema.dump(new_task)

    @staticmethod
    def get_all_tasks() -> list:
        tasks = Task.query.all()
        return tasks_schema.dump(tasks)

    @staticmethod
    def get_task_by_id(task_id: int) -> dict:
        task = Task.query.get(task_id)
        if not task:
            raise ValueError(f"Task with id {task_id} not found.")
        return task_schema.dump(task)

    @staticmethod
    def update_task(task_id: int, data: dict) -> dict:
        task = Task.query.get(task_id)
        if not task:
            raise ValueError(f"Task with id {task_id} not found.")

        validated_data = task_schema.load(data, partial=True)

        if 'title' in validated_data:
            existing_task = Task.query.filter_by(title=validated_data['title']).first()
            if existing_task and existing_task.id != task_id:
                raise ValueError(f"Task with title '{validated_data['title']}' already exists.")

        if 'status' in validated_data:
            new_status = validated_data['status']
            old_status = task.status
            
            valid_transitions = {
                'TODO': ['IN_PROGRESS'],
                'IN_PROGRESS': ['DONE'],
                'DONE': []
            }
            
            if new_status != old_status:
                if new_status not in valid_transitions.get(old_status, []):
                    raise ValueError(f"Invalid status transition from {old_status} to {new_status}. Allowed: {valid_transitions.get(old_status, [])}")
                task.status = new_status

        for key, value in validated_data.items():
            if key != 'status': 
                setattr(task, key, value)

        db.session.commit()
        return task_schema.dump(task)

    @staticmethod
    def delete_task(task_id: int) -> bool:
        task = Task.query.get(task_id)
        if not task:
            raise ValueError(f"Task with id {task_id} not found.")
        db.session.delete(task)
        db.session.commit()
        return True
