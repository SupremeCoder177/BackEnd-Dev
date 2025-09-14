document.getElementById("submit").onclick = function() {
    const username = document.getElementById("username").value;
    const password = document.getElementById("user-password").value;

    if(username && password){
        fetch("/login-user",
            {
                method: "POST",
                body: {'name' : username, 'password' : password}
            }
        ).then(res => res.json())
        .then(data => {
            console.log(data);
        });
    }
}