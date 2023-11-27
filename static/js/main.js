document.getElementById('newGame').addEventListener('click', function() {
    document.getElementById('gameForm').style.display = 'block';
    document.getElementById('joinForm').style.display = 'none';
});

document.getElementById('joinGame').addEventListener('click', function() {
    document.getElementById('joinForm').style.display = 'block';
    document.getElementById('gameForm').style.display = 'none';
});

document.getElementById('addTask').addEventListener('click', function(event) {
    // Create a new text field element
    event.preventDefault();
    var taskContainer = document.getElementById('taskContainer');
    var taskCount = taskContainer.getElementsByTagName('input').length;
    
    if (taskCount < 10) {
        var newTaskField = document.createElement('input');
        newTaskField.type = 'text';
        newTaskField.name = 'task' + (taskCount + 1);
        newTaskField.id = 'task' + (taskCount + 1);
        
        // Append the new text field to the document
        taskContainer.appendChild(newTaskField);
        taskContainer.appendChild(document.createElement('br'));
    }
});