function display(){
    console.log("Carson is a cool guy")
    let displayResources = document.querySelector("#display-resources");
    displayResources.textContent =
      "Loading data from JSON source...";
    fetch("http://127.0.0.1:5000/find_state/" + document.getElementById("search").value)
        .then(response => response.json())
        .then(result => {
            console.log(result) // Prints result from response.json() in getRequest
            console.log(result.length) // Prints result from response.json() in getRequest

            console.log("Andrew is a cool guy")
            let output =
               "<table><thead><tr><th>Facility_Name</th><th>State</th><th>Pop_Tested_Positive</th><th>Pop_Deaths</th><th>Staff_Tested_Pos</th><th>Staff_Deaths</th></thead><tbody>";
            for (let i in result) {
               console.log(result[i])
               output +=
                   "<tr><td>" +
                   result[i].cfname +
                   "</td><td>" +
                   result[i].state +
                   "</td><td>" +
                  result[i].posPop +
                   "</td><td>" +
                    result[i].deathPop +
                    "</td><td>" +
                    result[i].posStaff +
                    "</td><td>" +
                    result[i].deathStaff +
                    "</td></tr>";
            }
            output += "</tbody></table>";
            displayResources.innerHTML = output;
            $('#display-resources').DataTable({"iDisplayLength" : 10,});
    }).catch((err) => {console.log(err);})

}