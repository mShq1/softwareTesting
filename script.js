const addTaskBtn = document.getElementById('addTaskBtn');
const taskInput = document.getElementById('taskInput');
const taskList = document.getElementById('taskList');

addTaskBtn.addEventListener('click', () => {
  const text = taskInput.value.trim();

//   if (text === '') {
//     alert('Введите текст задачи');
//     return;
//   }

  const li = document.createElement('li');
  li.textContent = text;

  const deleteBtn = document.createElement('button');
  deleteBtn.textContent = 'Удалить';
  deleteBtn.classList.add('delete-btn');
  deleteBtn.onclick = () => li.remove();

//   li.addEventListener('click', () => {
//     li.classList.toggle('done');
//   });

  li.appendChild(deleteBtn);
  taskList.appendChild(li);
//   taskInput.value = '';
});
