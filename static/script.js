async function registerComplaint() {
    const student_name = document.getElementById("name").value;
    const room_no = document.getElementById("room").value;
    const issue = document.getElementById("issue").value;

    const response = await fetch('/register', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            student_name,
            room_no,
            issue
        })
    });

    const data = await response.json();

    alert(data.message + "\nComplaint ID: " + data.complaint_id);
}

async function loadComplaints() {
    const response = await fetch('/complaints');
    const data = await response.json();

    let output = "";

    data.forEach(c => {
        output += `
            <div class="card">
                <h3>Complaint ID: ${c.id}</h3>
                <p><strong>Name:</strong> ${c.student_name}</p>
                <p><strong>Room:</strong> ${c.room_no}</p>
                <p><strong>Issue:</strong> ${c.issue}</p>
                <p><strong>Status:</strong> ${c.status}</p>
            </div>
        `;
    });

    document.getElementById("output").innerHTML = output;
}

async function searchComplaint() {
    const id = document.getElementById("searchId").value;

    const response = await fetch(`/search/${id}`);

    const output = document.getElementById("output");

    if (response.status === 404) {
        output.innerHTML = "<h3>Complaint Not Found</h3>";
        return;
    }

    const c = await response.json();

    output.innerHTML = `
        <div class="card">
            <h3>Complaint ID: ${c.id}</h3>
            <p><strong>Name:</strong> ${c.student_name}</p>
            <p><strong>Room:</strong> ${c.room_no}</p>
            <p><strong>Issue:</strong> ${c.issue}</p>
            <p><strong>Status:</strong> ${c.status}</p>
        </div>
    `;
}

async function resolveComplaint() {
    const id = document.getElementById("resolveId").value;

    const response = await fetch(`/resolve/${id}`, {
        method: 'PUT'
    });

    const data = await response.json();

    alert(data.message);

    loadComplaints();
}