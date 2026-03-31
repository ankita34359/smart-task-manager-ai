import React from 'react';
import { Trash2, CheckCircle, ArrowRightCircle } from 'lucide-react';

const TaskCard = ({ task, onUpdateStatus, onDelete }) => {
  const isTodo = task.status === 'TODO';
  const isInProgress = task.status === 'IN_PROGRESS';

  return (
    <div className="task-card glass-panel" data-priority={task.priority}>
      <div className="task-header">
        <h3 className="task-title">{task.title}</h3>
        <span className={`priority-badge priority-${task.priority}`}>
          {task.priority}
        </span>
      </div>
      
      {task.description && (
        <p className="task-desc">{task.description}</p>
      )}

      <div className="task-actions">
        <div className="action-buttons">
          {isTodo && (
            <button 
              className="btn-small next"
              onClick={() => onUpdateStatus(task.id, 'IN_PROGRESS')}
              title="Start Progress"
            >
              <ArrowRightCircle size={14} className="mr-1" style={{ display: 'inline', marginRight: '4px', verticalAlign: 'middle' }}/>
              Start
            </button>
          )}
          {isInProgress && (
            <button 
              className="btn-small next"
              onClick={() => onUpdateStatus(task.id, 'DONE')}
              title="Mark Done"
            >
              <CheckCircle size={14} style={{ display: 'inline', marginRight: '4px', verticalAlign: 'middle' }}/>
              Complete
            </button>
          )}
        </div>
        
        <button 
          className="btn-icon delete"
          onClick={() => onDelete(task.id)}
          title="Delete Task"
        >
          <Trash2 size={16} />
        </button>
      </div>
    </div>
  );
};

export default TaskCard;
