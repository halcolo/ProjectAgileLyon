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
 * Updates the player' scores list in the HTML document.
 *
 * @param {Array} player - An array of player objects.
 */
function playerFunction(player) {
    playerScoresList = document.getElementById('playerScores');
    playerScoresList.innerHTML = ''; // Clear the list before adding new items
    playerScoresList.innerHTML += '<ul id="" class="list-group list-group-flush">';
    player.forEach(function(player) {
        var scoreText = player.score === 0 ? 'Pending' : '✅';
        var nameText = player.name === 'coffee' ? '☕️' + player.name : player.name;
        playerScoresList.innerHTML += '<li class="list-group-item">' + nameText + ' ' + scoreText + '</li>';
    });
    playerScoresList.innerHTML += '</ul>';
}


/**
 * Validates the selected file based on its extension and size, and parses its content as JSON.
 * @param {HTMLInputElement} input - The input element representing the file input.
 * @returns {void}
 */
function validateFile(input) {
    const allowedExtensions = ['json'];
    const maxSize = 5 * 1024 * 1024; // 5MB

    const file = input.files[0];
    const fileName = file.name;
    const fileSize = file.size;

    const fileExtension = fileName.split('.').pop();

    if (!allowedExtensions.includes(fileExtension)) {
       alert('Invalid file extension. Only JSON files are allowed.');
       input.value = '';
       return;
    }

    if (fileSize > maxSize) {
       alert('File size exceeds the maximum limit of 5MB.');
       input.value = '';
       return;
    }

    const reader = new FileReader();
    reader.onload = function(event) {
        try {
            const fileContent = event.target.result;
            const jsonData = JSON.parse(fileContent);

            // Check if the file has the expected format
            if (Array.isArray(jsonData) && jsonData.length > 0) {
                const firstItem = jsonData[0];
                if (typeof firstItem === 'object' && firstItem.hasOwnProperty('name') && firstItem.hasOwnProperty('gameMode')) {
                    // File has the expected format
                    console.log('File has the expected format.');
                    const jsonString = JSON.stringify(fileContent);
                    // Create a hidden input field to hold the JSON string
                    var hiddenInput = document.createElement("input");
                    hiddenInput.setAttribute("type", "hidden");
                    hiddenInput.setAttribute("name", "jsonData");
                    hiddenInput.setAttribute("value", jsonString);

                    // Append the hidden input field to the form
                    var form = document.getElementById("fileNameUpload").closest("form");
                    form.appendChild(hiddenInput);

                    // Submit the fojsonStringrm
                    // form.submit();
                } else {
                    console.log('File does not have the expected format.');
                }
            } else {
                console.log('File does not have the expected format.');
                throw new Error('Invalid file format.');
            }
        } catch (error) {
            alert('Error parsing the file:', error);
            input.value = '';
        }
    };
    reader.readAsText(file);
}
