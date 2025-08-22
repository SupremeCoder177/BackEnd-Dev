console.log("Hello world");

const add = document.getElementById("add-post");

add.onclick = () => {
    fetch("http://localhost:5000/post",
        {
            "context-type" : "application/json",
            "method": "GET"
        }
    )
    .catch(err => console.log(err))
}