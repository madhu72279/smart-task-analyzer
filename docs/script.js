document.getElementById("analyzeBtn").addEventListener("click", async () => {
    const text = document.getElementById("tasksInput").value;

    let tasks;
    try {
        tasks = JSON.parse(text);
    } catch (e) {
        document.getElementById("results").textContent = "❌ Invalid JSON";
        return;
    }

    try {
        const response = await fetch("http://127.0.0.1:8000/tasks/analyze/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(tasks)
        });

        const data = await response.json();
        document.getElementById("results").textContent =
            JSON.stringify(data, null, 2);

    } catch (error) {
        document.getElementById("results").textContent =
            "❌ Could not reach backend";
    }
});
