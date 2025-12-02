document.getElementById("analyzeBtn").addEventListener("click", () => {
    const text = document.getElementById("tasksInput").value;

    let tasks;
    try {
        tasks = JSON.parse(text);
    } catch (e) {
        document.getElementById("results").textContent = "❌ Invalid JSON";
        return;
    }

    // Since backend is not available on GitHub Pages, show a demo message
    const container = document.getElementById("results");
    container.innerHTML = `
        ⚠ Task analysis is not available in this GitHub Pages demo.
        <br><br>
        Here is your input data as JSON:<br>
        <pre>${JSON.stringify(tasks, null, 2)}</pre>
    `;
});
