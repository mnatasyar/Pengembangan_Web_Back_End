
fetch("dataj.json")
.then(function(response){
    return response.json();
})
.then(function(dataj){
    let placeholder = document.querySelector("#datajson");
    let out = "";
    for (let dataj of dataj){
        out += `
            <tr>
                <td>${dataj.id}</td>
                <td>${dataj.name}</td>
                <td>${dataj.username}</td>
                <td>${dataj.email}</td>
                <td>${dataj.address}</td>
            </tr>
        `;
    }
    placeholder.innerHTML = out;
});