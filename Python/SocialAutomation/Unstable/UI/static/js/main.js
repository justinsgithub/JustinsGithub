const displayCollections = async (mountPoint) => {
    const urlToFetch = `/collections`;
    try {
        const response = await fetch(urlToFetch);
        const jsonResponse = await response.json();
        const collections = jsonResponse.collections;

    table = document.createElement('table');
    
    thead =  document.createElement('thead');
    tr1 = document.createElement('tr');
    th1 = document.createElement('th');
    th1.textContent = "State"
    tr1.appendChild(th1);
    thead.appendChild(tr1);
    table.appendChild(thead);

    tbody = document.createElement('tbody')        
    
        collections.forEach(collection => {
            tr = document.createElement('tr');
            td = document.createElement('td')
            td.textContent = collection
            tr.appendChild(td);
            tbody.appendChild(tr);
        });

    table.appendChild(tbody);

    mountPoint.appendChild(table);

  } catch (err) {
    console.log(err);
  }
}



const main = () =>{
    const app = document.getElementById('app');
    const header = document.createElement('h1');
    header.textContent = "User Database Collections"
    header.style.textAlign = "center";
    app.appendChild(header);

    displayCollections(app);
}

main();
