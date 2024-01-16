const observer = new MutationObserver(function (mutationsList) {
    for (let mutation of mutationsList) {
        if (mutation.type === 'childList') {
            // Update the DOM with the search results here
        }
    }
});

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
            // Perform DOM manipulation here
            observer.observe(document.body, { childList: true, subtree: true });
        })
        .catch((error) => {
            console.error('Error:', error);
        });
});