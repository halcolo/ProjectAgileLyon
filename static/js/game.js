var tasks = ['Tarea 1', 'Tarea 2', 'Tarea 3']; // Replace with eachtasks
var fibonacciNumbers = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]; // Fibonacci to 100

// Crear un formulario para cada tarea
for (var i = 0; i < tasks.length; i++) {
    var taskForm = document.createElement('form');
    taskForm.id = 'task' + i;
    taskForm.style.display = i === 0 ? 'block' : 'none'; // show first task

    var taskTitle = document.createElement('h2');
    taskTitle.textContent = tasks[i];
    taskForm.appendChild(taskTitle);

    // create Radio Buttons with FIbonacci numbers
    for (var j = 0; j < fibonacciNumbers.length; j++) {
        var radioButton = document.createElement('input');
        radioButton.type = 'radio';
        radioButton.name = 'card';
        radioButton.value = fibonacciNumbers[j];

        var label = document.createElement('label');
        label.textContent = fibonacciNumbers[j];

        taskForm.appendChild(radioButton);
        taskForm.appendChild(label);
    }

    document.getElementById('taskContainer').appendChild(taskForm);
}

// Add event listener to next button
document.getElementById('nextTask').addEventListener('click', function() {
    var currentTask = document.querySelector('form[style="display: block;"]');
    var nextTask = currentTask.nextElementSibling;

    if (nextTask) {
        currentTask.style.display = 'none';
        nextTask.style.display = 'block';
    } else {
        alert('Todas las tareas completadas!');
    }
});