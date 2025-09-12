document.getElementById("fileInput").addEventListener("change", function() {

    const file = this.files[0];
    if(file){
        document.getElementById("preview").src = URL.createObjectURL(file);
    }

})

document.getElementById("preview").addEventListener("load", function() {
    this.style.width = "auto";
})

document.getElementById("post").onclick = () => {
    
    const text = document.getElementById("text").value;
    const img = document.getElementById("preview").value;
    
    if(text && img){

        const data = {
            name: '',
            email: '',
            body: text    
        }


    }
}