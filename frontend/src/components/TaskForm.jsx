import React, { useState } from 'react';
import { PlusCircle, AlertCircle, CheckCircle2 } from 'lucide-react';

const TaskForm = ({ onAddTask, apiError }) => {
  const [title, setTitle] = useState('');
  const [description, setDescription] = useState('');
  const [loading, setLoading] = useState(false);
  const [successMsg, setSuccessMsg] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!title.trim()) return;
    
    setLoading(true);
    setSuccessMsg('');
    try {
      await onAddTask({ title, description });
      setTitle('');
      setDescription('');
      setSuccessMsg('Task created successfully');
      setTimeout(() => setSuccessMsg(''), 3000);
    } catch (err) {
      // Error is handled by parent, keep form data
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="task-form-container glass-panel">
      {apiError && (
        <div className="error-msg">
          <AlertCircle size={18} />
          {apiError}
        </div>
      )}

      {successMsg && (
        <div className="success-msg">
          <CheckCircle2 size={18} />
          {successMsg}
        </div>
      )}
      
      <form className="task-form" onSubmit={handleSubmit}>
        <div className="form-group">
          <label htmlFor="title">Task Title *</label>
          <input 
            type="text" 
            id="title"
            className="form-control"
            value={title}
            onChange={(e) => setTitle(e.target.value)}
            placeholder="What needs to be done?"
            required
            autoComplete="off"
          />
        </div>
        
        <div className="form-group">
          <label htmlFor="description">Description (Optional)</label>
          <textarea 
            id="description"
            className="form-control"
            value={description}
            onChange={(e) => setDescription(e.target.value)}
            placeholder="Add details... Our AI will suggest a priority!"
          />
        </div>

        <button type="submit" className="btn" disabled={!title.trim() || loading}>
          <PlusCircle size={18} />
          {loading ? 'Creating...' : 'Create Task'}
        </button>
      </form>
    </div>
  );
};

export default TaskForm;
