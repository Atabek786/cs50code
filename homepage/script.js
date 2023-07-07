// Display a welcome message when the page loads
window.onload = function() {
    var welcomeMessage = "Welcome to my weblog!";
    alert(welcomeMessage);
};

  // Fetch data from an API and display it on the page
fetch("https://api.example.com/posts")
.then(function(response) {
    return response.json();
})
.then(function(data) {
    // Process the data and display it on the page
    var postsContainer = document.getElementById("postsContainer");

    data.forEach(function(post) {
    var postElement = document.createElement("div");
    postElement.innerText = post.title;
    postsContainer.appendChild(postElement);
    });
})
.catch(function(error) {
    console.log("An error occurred:", error);
});
