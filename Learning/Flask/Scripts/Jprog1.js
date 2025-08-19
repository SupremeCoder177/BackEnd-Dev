function get_data(){
	fetch("http://localhost:5000", { method : "GET"})
	.then(res => res.json())
	.then(data => console.log(data))
	.catch(err => console.log(err))
}

function post_data(){
	fetch("http://localhost:5000", {
		method : "POST",
		headers: {
            "Content-Type": "application/json"   // <-- must be here
        },
		body : JSON.stringify({ name: "John Doe", age: 22, address: "Baker Street 123", email: "John12D@msn.net"})
	})
	.then(res => res.json())
	.then(data => console.log(data))
	.catch(err => console.log(err))
}

get_data()
post_data()