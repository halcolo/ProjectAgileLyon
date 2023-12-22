//
/**
 * Represents a collection of edit buttons for each task.
 * @type {NodeList}
 */
var editButtons = document.querySelectorAll('[id*="taskEdit"]');
editButtons.forEach(function(button) {
    button.addEventListener('click', function(event) {
        event.preventDefault(); // Prevent the default action
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
        // Get the value from the input with id "TaskId"
        
    });
});

/**
 * Updates the users' scores list in the HTML document.
 * 
 * @param {Array} users - An array of user objects.
 */
function usersFunction(users) {
    usersScoresList = document.getElementById('usersScores');
    usersScoresList.innerHTML = ''; // Clear the list before adding new items
    usersScoresList.innerHTML += '<ul id="" class="list-group list-group-flush">';
    users.forEach(function(user) {
        var scoreText = user.score === 0 ? 'No score' : '✅';
        var nameText = user.name === 'coffee' ? '☕️' + user.name : user.name;
        usersScoresList.innerHTML += '<li class="list-group-item">' + nameText + ' ' + scoreText + '</li>';
    });
    usersScoresList.innerHTML += '</ul>';
}
