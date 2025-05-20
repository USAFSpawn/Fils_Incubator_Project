// 🐣 Incubator Dashboard - Graph Data Handler (graph.js)
// ✅ Fetches sensor data from API
// ✅ Updates temperature & humidity graphs dynamically

document.addEventListener("DOMContentLoaded", function () {
    const ctxTemp = document.getElementById("tempChart").getContext("2d");
    const ctxHumidity = document.getElementById("humidityChart").getContext("2d");

    const tempChart = new Chart(ctxTemp, {
        type: "line",
        data: {
            labels: [],
            datasets: [{
                label: "Temperature (°F)",
                borderColor: "#ff5733",
                backgroundColor: "rgba(255, 87, 51, 0.5)",
                data: [],
            }]
        },
        options: {
            responsive: true,
            scales: {
                x: { title: { display: true, text: "Time" } },
                y: { title: { display: true, text: "Temperature (°F)" }, min: 80, max: 105 }
            }
        }
    });

    const humidityChart = new Chart(ctxHumidity, {
        type: "line",
        data: {
            labels: [],
            datasets: [{
                label: "Humidity (%)",
                borderColor: "#33bfff",
                backgroundColor: "rgba(51, 191, 255, 0.5)",
                data: [],
            }]
        },
        options: {
            responsive: true,
            scales: {
                x: { title: { display: true, text: "Time" } },
                y: { title: { display: true, text: "Humidity (%)" }, min: 30, max: 70 }
            }
        }
    });

    function updateGraphs() {
        fetch("/api/sensors")
            .then(response => response.json())
            .then(data => {
                const timestamp = new Date().toLocaleTimeString();
                tempChart.data.labels.push(timestamp);
                tempChart.data.datasets[0].data.push(data.temperature);
                humidityChart.data.labels.push(timestamp);
                humidityChart.data.datasets[0].data.push(data.humidity);

                if (tempChart.data.labels.length > 30) tempChart.data.labels.shift();
                if (humidityChart.data.labels.length > 30) humidityChart.data.labels.shift();

                tempChart.update();
                humidityChart.update();
            });
    }

    setInterval(updateGraphs, 5000); // Update every 5 seconds
});
