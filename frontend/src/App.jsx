import React, { useState, useEffect } from 'react';
import { LayoutList } from 'lucide-react';
import { taskService } from './services/api';
import TaskBoard from './components/TaskBoard';
import TaskForm from './components/TaskForm';

function App() {
  const [tasks, setTasks] = useState([]);
  const [error, setError] = useState('');

  const fetchTasks = async () => {
    try {
      const data = await taskService.getTasks();
      setTasks(data);
    } catch (err) {
      console.error("Failed to fetch tasks", err);
      setError("Unable to load tasks from server. Make sure the backend is running.");
    }
  };

  useEffect(() => {
    fetchTasks();
  }, []);

  const handleAddTask = async (taskData) => {
    setError('');
    try {
      const newTask = await taskService.createTask(taskData);
      setTasks([...tasks, newTask]);
    } catch (err) {
      if (err.response?.data?.messages) {
        const msgs = err.response.data.messages;
        const formatted = Object.keys(msgs).map(k => `${k}: ${msgs[k]}`).join(' | ');
        setError(`Validation Error: ${formatted}`);
      } else {
        const msg = err.response?.data?.message || err.response?.data?.error || "Failed to create task";
        setError(msg);
      }
      throw err; // throw to stop form reset
    }
  };

  const handleUpdateStatus = async (taskId, status) => {
    setError('');
    try {
      const updatedTask = await taskService.updateTaskStatus(taskId, status);
      setTasks(tasks.map(t => t.id === taskId ? updatedTask : t));
    } catch (err) {
      const msg = err.response?.data?.message || "Failed to update status";
      setError(msg);
    }
  };

  const handleDeleteTask = async (taskId) => {
    setError('');
    try {
      await taskService.deleteTask(taskId);
      setTasks(tasks.filter(t => t.id !== taskId));
    } catch (err) {
      setError("Failed to delete task");
    }
  };

  return (
    <div className="app-container">
      <header className="header">
        <h1>
          <LayoutList size={36} style={{ display: 'inline', verticalAlign: '-6px', marginRight: '12px', color: '#60a5fa' }} />
          Smart Task Manager
        </h1>
        <p>AI-powered priority assignment and strict workflow transitions</p>
      </header>

      <main>
        <TaskForm onAddTask={handleAddTask} apiError={error} />
        <TaskBoard 
          tasks={tasks} 
          onUpdateStatus={handleUpdateStatus} 
          onDelete={handleDeleteTask} 
        />
      </main>
    </div>
  );
}

export default App;
