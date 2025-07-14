let chart = null;

document.getElementById("applyFilters").addEventListener("click", function () {
  const country = document.getElementById("countrySelect").value;
  const year = document.getElementById("yearSelect").value;
  const energy = document.getElementById("energyTypeSelect").value;
  const chartType = document.getElementById("chartTypeSelect").value;
  const metricOptions = document.getElementById("metricSelect").selectedOptions;

  const metrics = Array.from(metricOptions).map(option => option.value);

  if (metrics.length === 0) {
    alert("Por favor seleccione al menos una métrica.");
    return;
  }

  fetch("/get_data", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({ country, year, energy, metrics })
  })
    .then(response => response.json())
    .then(data => {
      const labels = data.metrics;
      const values = data.values;

      const ctx = document.getElementById("myChart").getContext("2d");

      if (chart) {
        chart.destroy();
      }

      chart = new Chart(ctx, {
        type: chartType,
        data: {
          labels: labels,
          datasets: [{
            label: "Valor",
            data: values,
            backgroundColor: [
              "#4CAF50", "#2196F3", "#FF9800", "#9C27B0", "#E91E63", "#03A9F4", "#FF5722"
            ],
            borderColor: "#333",
            borderWidth: 1
          }]
        },
        options: {
          responsive: true,
          maintainAspectRatio: false,
          plugins: {
            legend: {
              position: chartType === 'pie' || chartType === 'doughnut' ? 'bottom' : 'top'
            }
          },
          scales: chartType === 'bar' || chartType === 'line' ? {
            y: {
              beginAtZero: true
            }
          } : {}
        }
      });
    })
    .catch(error => {
      console.error("Error al obtener datos:", error);
      alert("Ocurrió un error al cargar los datos.");
    });
});
