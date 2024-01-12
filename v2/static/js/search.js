document.getElementById("searchForm").addEventListener("submit", function (event) {
    event.preventDefault();
    let username = document.getElementById("username").value;
    fetch('/search', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ username: username }),
    })
        .then(response => response.json())
        .then(data => {
            console.log('Success:', data);
            // Update the DOM with the search results here

        })
        .catch((error) => {
            console.error('Error:', error);
        });
});