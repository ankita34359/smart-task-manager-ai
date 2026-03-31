from flask import Blueprint, request, jsonify
from services.task_service import TaskService
from marshmallow import ValidationError
import logging

logger = logging.getLogger(__name__)
task_bp = Blueprint('tasks', __name__)

@task_bp.route('', methods=['POST'])
def create_task():
    try:
        data = request.get_json() or {}
        task = TaskService.create_task(data)
        return jsonify(task), 201
    except ValidationError as err:
        return jsonify({"error": "Validation Error", "messages": err.messages}), 400
    except ValueError as err:
        return jsonify({"error": "Bad Request", "message": str(err)}), 400
    except Exception as e:
        logger.exception("Unexpected error in create_task")
        return jsonify({"error": "Internal Server Error"}), 500

@task_bp.route('', methods=['GET'])
def get_tasks():
    try:
        tasks = TaskService.get_all_tasks()
        return jsonify(tasks), 200
    except Exception as e:
        logger.exception("Unexpected error in get_tasks")
        return jsonify({"error": "Internal Server Error"}), 500

@task_bp.route('/<int:task_id>', methods=['GET'])
def get_task(task_id):
    try:
        task = TaskService.get_task_by_id(task_id)
        return jsonify(task), 200
    except ValueError as err:
        return jsonify({"error": "Not Found", "message": str(err)}), 404
    except Exception as e:
        logger.exception("Unexpected error in get_task")
        return jsonify({"error": "Internal Server Error"}), 500

@task_bp.route('/<int:task_id>', methods=['PUT', 'PATCH'])
def update_task(task_id):
    try:
        data = request.get_json() or {}
        task = TaskService.update_task(task_id, data)
        return jsonify(task), 200
    except ValidationError as err:
        return jsonify({"error": "Validation Error", "messages": err.messages}), 400
    except ValueError as err:
        return jsonify({"error": "Bad Request", "message": str(err)}), 400
    except Exception as e:
        logger.exception("Unexpected error in update_task")
        return jsonify({"error": "Internal Server Error"}), 500

@task_bp.route('/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    try:
        TaskService.delete_task(task_id)
        return jsonify({"message": "Task deleted successfully"}), 200
    except ValueError as err:
        return jsonify({"error": "Not Found", "message": str(err)}), 404
    except Exception as e:
        logger.exception("Unexpected error in delete_task")
        return jsonify({"error": "Internal Server Error"}), 500
