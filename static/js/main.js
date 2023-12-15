// document.getElementById('newTaskButton').addEventListener('click', function() {
//     document.getElementById('newTaskForm').style.display = 'block';
//     document.getElementById('joinTaskForm').style.display = 'none';
// });

// document.getElementById('joinTask').addEventListener('click', function() {
//     document.getElementById('joinTaskForm').style.display = 'block';
//     document.getElementById('newTaskForm').style.display = 'none';
// });

// document.getElementById('editButton').addEventListener('click', function(event) {
//     event.preventDefault(); // Prevent the default action
//     console.log('edit button clicked');
//     document.getElementById('playPoker').style.display = 'block';

//     // Your code here
// });
var editButtons = document.querySelectorAll('[id*="taskEdit"]');
editButtons.forEach(function(button) {
    button.addEventListener('click', function(event) {
        event.preventDefault(); // Prevent the default action
        console.log('edit button clicked');
        var buttonId = button.id;
        // Getting the number from the button id
        var number = buttonId.match(/\d+/)[0];
        var gameJoinId = 'taskJoin' + number;
        var joinCode = document.getElementById(gameJoinId).textContent;
        var taskNameId = 'taskName' + number;
        var taskName = document.getElementById(taskNameId).textContent;
        // Getting the form elements
        document.getElementById('TaskId').value = joinCode;
        document.getElementById('TaskName').value = taskName;
        document.getElementById('playPoker').style.display = 'block';
    });
});

// document.getElementById('addTask').addEventListener('click', function(event) {
//     // Create a new text field element
//     event.preventDefault();
//     var taskContainer = document.getElementById('taskContainer');
//     var taskCount = taskContainer.getElementsByTagName('input').length;

//     if (taskCount < 10) {
//         var newTaskField = document.createElement('input');
//         newTaskField.type = 'text';
//         newTaskField.name = 'task' + (taskCount + 1);
//         newTaskField.id = 'task' + (taskCount + 1);

//         // Append the new text field to the document
//         taskContainer.appendChild(newTaskField);
//         taskContainer.appendChild(document.createElement('br'));
//     }
// });
