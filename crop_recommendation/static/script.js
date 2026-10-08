const form = document.getElementById("predictionForm");
const resultCard = document.getElementById("resultCard");
const emptyState = document.getElementById("emptyState");
const resultContent = document.getElementById("resultContent");
const loading = document.getElementById("loading");
const predictBtn = document.getElementById("predictBtn");

const fields = [
    "N",
    "P",
    "K",
    "temperature",
    "humidity",
    "ph",
    "rainfall"
];

form.addEventListener("submit", async (event) => {
    event.preventDefault();

    const data = {};

    for (const field of fields) {
        data[field] = document.getElementById(field).value;
    }

    loading.classList.remove("hidden");
    predictBtn.disabled = true;

    try {
        const response = await fetch("/predict", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(data)
        });

        const result = await response.json();

        if (!response.ok || !result.success) {
            throw new Error(result.message || "Prediction failed");
        }

        document.getElementById("cropName").textContent = result.crop;

        const confidence = result.confidence ?? 0;
        document.getElementById("confidenceText").textContent =
            `${confidence.toFixed(2)}%`;

        document.getElementById("confidenceBar").style.width =
            `${Math.min(confidence, 100)}%`;

        emptyState.classList.add("hidden");
        resultContent.classList.remove("hidden");

    } catch (error) {
        alert(error.message);
    } finally {
        loading.classList.add("hidden");
        predictBtn.disabled = false;
    }
});

function loadSample() {
    const sample = {
        N: 90,
        P: 42,
        K: 43,
        temperature: 20.88,
        humidity: 82,
        ph: 6.50,
        rainfall: 202.94
    };

    for (const field of fields) {
        document.getElementById(field).value = sample[field];
    }
}

function resetForm() {
    form.reset();

    emptyState.classList.remove("hidden");
    resultContent.classList.add("hidden");

    document.getElementById("confidenceText").textContent = "--%";
    document.getElementById("confidenceBar").style.width = "0%";
}
