const form = document.getElementById("predictionForm");
const predictButton = document.getElementById("predictButton");


async function loadMetrics() {

    try {

        const response = await fetch("/api/metrics");

        const metrics = await response.json();

        const models = Object.entries(metrics);

        let bestModel = null;
        let bestRMSE = Infinity;

        models.forEach(([modelName, values]) => {

            if (
                typeof values === "object" &&
                values.RMSE !== undefined
            ) {

                if (values.RMSE < bestRMSE) {
                    bestRMSE = values.RMSE;
                    bestModel = {
                        name: modelName,
                        values: values
                    };
                }

            }

        });


        // Best model metrics

        if (bestModel) {

            document.getElementById("r2Value").textContent =
                (bestModel.values.R2 * 100).toFixed(2) + "%";

            document.getElementById("rmseValue").textContent =
                bestModel.values.RMSE.toFixed(2);

            document.getElementById("maeValue").textContent =
                bestModel.values.MAE.toFixed(2);

            document.getElementById("modelName").textContent =
                bestModel.name;
        }


        // Model comparison chart

        createModelChart(models);

    } catch (error) {

        console.error("Could not load metrics:", error);

    }
}



function createModelChart(models) {

    const chart = document.getElementById("modelChart");

    chart.innerHTML = "";

    const validModels = models.filter(
        ([name, values]) =>
            typeof values === "object" &&
            values.RMSE !== undefined
    );

    if (validModels.length === 0) {
        chart.innerHTML = "<p>No model metrics available.</p>";
        return;
    }


    const maxRMSE = Math.max(
        ...validModels.map(
            ([name, values]) => values.RMSE
        )
    );


    validModels.forEach(([name, values]) => {

        const percentage =
            (values.RMSE / maxRMSE) * 100;


        const row = document.createElement("div");

        row.className = "chart-row";

        row.innerHTML = `
            <div class="chart-label">
                <span>${name}</span>
                <strong>${values.RMSE.toFixed(2)}</strong>
            </div>

            <div class="chart-background">
                <div
                    class="chart-bar"
                    style="width: ${percentage}%"
                ></div>
            </div>
        `;

        chart.appendChild(row);

    });
}




form.addEventListener("submit", async function (event) {

    event.preventDefault();

    predictButton.disabled = true;
    predictButton.textContent = "Predicting...";


    const inputData = {

        Distance_km:
            parseFloat(
                document.getElementById("distance").value
            ),

        Weather:
            document.getElementById("weather").value,

        Traffic_Level:
            document.getElementById("traffic").value,

        Time_of_Day:
            document.getElementById("timeOfDay").value,

        Vehicle_Type:
            document.getElementById("vehicle").value,

        Preparation_Time_min:
            parseInt(
                document.getElementById("preparation").value
            ),

        Courier_Experience_yrs:
            parseFloat(
                document.getElementById("experience").value
            )
    };


    try {

        const response = await fetch("/api/predict", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify(inputData)

        });


        const result = await response.json();


        if (!response.ok) {

            throw new Error(
                result.detail || "Prediction failed"
            );

        }


        // ===============================
        // Show Prediction
        // ===============================

        const prediction =
            result.predicted_delivery_time_min;


        document.getElementById(
            "predictionValue"
        ).textContent = prediction;


        document.getElementById(
            "predictionMessage"
        ).textContent =
            "Estimated delivery time based on the provided order details.";


        // ===============================
        // Update Circle
        // ===============================

        const maxTime = 120;

        let percentage =
            Math.min((prediction / maxTime) * 360, 360);


        document.querySelector(
            ".prediction-circle"
        ).style.background = `
            conic-gradient(
                #38bdf8 ${percentage}deg,
                #334155 ${percentage}deg
            )
        `;


        // ===============================
        // Prediction Summary
        // ===============================

        document.getElementById(
            "summaryDistance"
        ).textContent =
            inputData.Distance_km + " km";


        document.getElementById(
            "summaryWeather"
        ).textContent =
            inputData.Weather;


        document.getElementById(
            "summaryTraffic"
        ).textContent =
            inputData.Traffic_Level;


        document.getElementById(
            "summaryTime"
        ).textContent =
            inputData.Time_of_Day;


        document.getElementById(
            "summaryVehicle"
        ).textContent =
            inputData.Vehicle_Type;


        document.getElementById(
            "summaryPreparation"
        ).textContent =
            inputData.Preparation_Time_min + " min";


        document.getElementById(
            "summaryExperience"
        ).textContent =
            inputData.Courier_Experience_yrs + " years";


    } catch (error) {

        console.error(error);

        alert(
            "Prediction failed: " + error.message
        );

    }


    predictButton.disabled = false;
    predictButton.textContent =
        "Predict Delivery Time";

});


// ===============================
// Initial Load
// ===============================

loadMetrics();