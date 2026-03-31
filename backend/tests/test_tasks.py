import pytest

def test_health_check(client):
    response = client.get('/health')
    assert response.status_code == 200

def test_create_task(client):
    response = client.post('/api/tasks', json={
        "title": "New Task",
        "description": "Urgent task to do"
    })
    assert response.status_code == 201
    data = response.get_json()
    assert data["title"] == "New Task"
    assert data["priority"] == "HIGH"  # Mock AI logic 'Urgent' -> HIGH
    assert data["status"] == "TODO"

    # Test duplicate title
    response2 = client.post('/api/tasks', json={
        "title": "New Task",
    })
    assert response2.status_code == 400

def test_create_task_invalid_input(client):
    # Empty title
    response = client.post('/api/tasks', json={
        "title": "   "
    })
    assert response.status_code == 400
    
    # Invalid status
    response = client.post('/api/tasks', json={
        "title": "Task2",
        "status": "INVALID_STATUS"
    })
    assert response.status_code == 400

def test_status_transitions(client):
    response = client.post('/api/tasks', json={"title": "Transition Task"})
    task_id = response.get_json()["id"]

    # Valid transition TODO -> IN_PROGRESS
    response = client.put(f'/api/tasks/{task_id}', json={"status": "IN_PROGRESS"})
    assert response.status_code == 200
    assert response.get_json()["status"] == "IN_PROGRESS"

    # Valid transition IN_PROGRESS -> DONE
    response = client.put(f'/api/tasks/{task_id}', json={"status": "DONE"})
    assert response.status_code == 200

    # Invalid transition DONE -> TODO
    response = client.put(f'/api/tasks/{task_id}', json={"status": "TODO"})
    assert response.status_code == 400

def test_update_task_fields(client):
    response = client.post('/api/tasks', json={"title": "Update Me"})
    task_id = response.get_json()["id"]

    response = client.put(f'/api/tasks/{task_id}', json={"title": "Updated Title", "priority": "HIGH"})
    assert response.status_code == 200
    assert response.get_json()["title"] == "Updated Title"

def test_delete_task(client):
    response = client.post('/api/tasks', json={"title": "To be deleted"})
    task_id = response.get_json()["id"]

    delete_resp = client.delete(f'/api/tasks/{task_id}')
    assert delete_resp.status_code == 200
    
    get_resp = client.get(f'/api/tasks/{task_id}')
    assert get_resp.status_code == 404
