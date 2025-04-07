document.addEventListener("DOMContentLoaded", function(){
    document.getElementById("search_form").addEventListener("submit", async function (e) {
        e.preventDefault();

        var formData = new FormData(e.target);
        var data = Object.fromEntries(formData);

        alert(JSON.stringify(data))
    })
})