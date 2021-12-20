async function updateRequest( url ) {

	const fetchOptions = {method: "PUT"};

	const response = await fetch(url, fetchOptions);

	if (!response.ok) {
		const errorMessage = await response.json();
		throw new Error(errorMessage);
	}

	return response.json();
};

async function handleUpdateClick(e) {
    const thisItem = e.target.parentNode
    const thisItemId = thisItem.id
	const url = `/items/${thisItemId}`

	try {
		const updateResponse = await updateRequest(url);
        const updatedId = updateResponse.item_id
        const updatedItem = document.getElementById(updatedId)
        console.log(updateResponse)

    } catch (error) {
		console.error(error);
	};
};
async function deleteRequest( url ) {

	const fetchOptions = {method: "DELETE"};

	const response = await fetch(url, fetchOptions);

	if (!response.ok) {
		const errorMessage = await response.json();
		throw new Error(errorMessage);
	}

	return response.json();
};
async function handleDeleteClick(e) {
    const thisItem = e.target.parentNode
    const thisItemId = thisItem.id
	const url = `/items/${thisItemId}`

	try {
		const deleteResponse = await deleteRequest(url);
        const deletedId = deleteResponse.item_id
        const deletedItem = document.getElementById(deletedId)
        deletedItem.remove()

	} catch (error) {
		console.error(error);
	};
};

function displayData() {
	const tableData = document.getElementById("table-data");
    const formTitle = document.getElementById("form-title");
    formTitle.textContent = "Add Item"

	// Create a request variable and assign a new XMLHttpRequest object to it.
	var request = new XMLHttpRequest();

	// Open a new connection, using the GET request on the URL endpoint
	request.open("GET", "/items", true);

	request.onload = function () {
		// Begin accessing JSON data here
		// Begin accessing JSON data here
		var data = JSON.parse(this.response);

        if (request.status >= 200 && request.status < 400) {
            data.forEach(item => {
                const itemRow = document.createElement('tr')
                itemRow.setAttribute("id", item.item_id)

                const itemName = document.createElement('td');
                itemName.textContent = item.name;
                itemRow.appendChild(itemName);

                const itemDescription = document.createElement('td');
                itemDescription.textContent = item.description;
                itemRow.appendChild(itemDescription);

                const itemPrice = document.createElement('td');
                itemPrice.textContent = item.price;
                itemRow.appendChild(itemPrice);

                const updateButton = document.createElement('td');
                updateButton.setAttribute("class", "button bmargin");
                updateButton.textContent = "Update";
                updateButton.addEventListener('click', handleUpdateClick);
                itemRow.appendChild(updateButton);

                const itemDelete = document.createElement('td');
                itemDelete.setAttribute("class", "button delete bmargin");
                itemDelete.textContent = "Delete";
                itemDelete.addEventListener('click', handleDeleteClick)
                itemRow.appendChild(itemDelete);

                tableData.append(itemRow)
            });
          } else {
			console.log("error");
		};
	};
    request.send();
};


async function postFormDataAsJson({ url, formData }) {
	const plainFormData = Object.fromEntries(formData.entries());
	const formDataJsonString = JSON.stringify(plainFormData);

	const fetchOptions = {
		method: "POST",
		headers: {
			"Content-Type": "application/json",
			Accept: "application/json",
		},
		body: formDataJsonString,
	};

	const response = await fetch(url, fetchOptions);

	if (!response.ok) {
		const errorMessage = await response.text();
		throw new Error(errorMessage);
	}

	return response.json();
}

async function handleFormSubmit(event) {
	event.preventDefault();

	const form = event.currentTarget;
	const url = form.action;

	try {
        const tableData = document.getElementById("table-data");

		const formData = new FormData(form);
		const item = await postFormDataAsJson({ url, formData });


		console.log({ item });
        console.log( item.name );

        const itemRow = document.createElement('tr')
        itemRow.setAttribute("id", item.item_id)

        const itemName = document.createElement('td');
        itemName.textContent = item.name;
        itemRow.appendChild(itemName);
      
        const itemDescription = document.createElement('td');
        itemDescription.textContent = item.description;
        itemRow.appendChild(itemDescription);
      
        const itemPrice = document.createElement('td');
        itemPrice.textContent = item.price;
        itemRow.appendChild(itemPrice);

        const itemDelete = document.createElement('td');
        itemDelete.setAttribute("class", "button");
        itemDelete.textContent = "Delete";
        itemDelete.addEventListener('click', handleDeleteClick)
        itemRow.appendChild(itemDelete);

        tableData.append(itemRow)


	} catch (error) {
		console.error(error);
	}
}

const itemForm = document.getElementById("item-form");
itemForm.addEventListener("submit", handleFormSubmit);

displayData()