import React from 'react';
import TaskCard from './TaskCard';

const TaskBoard = ({ tasks, onUpdateStatus, onDelete }) => {
  const todoTasks = tasks.filter(t => t.status === 'TODO');
  const inProgressTasks = tasks.filter(t => t.status === 'IN_PROGRESS');
  const doneTasks = tasks.filter(t => t.status === 'DONE');

  const Column = ({ title, columnTasks }) => (
    <div className="board-column">
      <div className="column-header">
        {title}
        <span className="task-count">{columnTasks.length}</span>
      </div>
      {columnTasks.length === 0 ? (
        <div className="empty-state glass-panel">
          {title === 'To Do' ? 'Create your first task above 👆' : 'No tasks here'}
        </div>
      ) : (
        columnTasks.map(task => (
          <TaskCard 
            key={task.id} 
            task={task} 
            onUpdateStatus={onUpdateStatus}
            onDelete={onDelete}
          />
        ))
      )}
    </div>
  );

  return (
    <div className="board">
      <Column title="To Do" columnTasks={todoTasks} />
      <Column title="In Progress" columnTasks={inProgressTasks} />
      <Column title="Done" columnTasks={doneTasks} />
    </div>
  );
};

export default TaskBoard;
