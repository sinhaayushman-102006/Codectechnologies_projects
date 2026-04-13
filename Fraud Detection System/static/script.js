// ================= LOGIN =================
async function login() {
  const res = await fetch('/login', {
    method: 'POST',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify({
      username: document.getElementById("user").value,
      password: document.getElementById("pass").value
    })
  });

  const data = await res.json();
  alert(data.status === "success" ? "Login Success" : "Login Failed");
}

// ================= PREDICT =================
async function predict() {
  const amount = document.getElementById("amount").value;
  const time = document.getElementById("time").value;

  const result = document.getElementById("result");
  result.innerHTML = "⏳ Processing...";

  try {
    const res = await fetch('/predict', {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({ amount, time })
    });

    const data = await res.json();

    result.innerHTML =
      data.prediction === 1
        ? `⚠️ Fraud (${data.probability.toFixed(2)})`
        : `✅ Legit (${(1 - data.probability).toFixed(2)})`;

    showSHAP(data.shap);

  } catch (err) {
    result.innerHTML = "❌ Backend error";
  }
}

// ================= SHAP =================
function showSHAP(values) {
  const ctx = document.getElementById("shapChart");

  new Chart(ctx, {
    type: 'bar',
    data: {
      labels: values.map((_, i) => 'F' + i),
      datasets: [{
        label: "Feature Impact",
        data: values
      }]
    }
  });
}

// ================= CSV UPLOAD =================
async function uploadCSV() {
  const file = document.getElementById("file").files[0];

  const form = new FormData();
  form.append("file", file);

  await fetch('/upload', {
    method: 'POST',
    body: form
  });

  alert("Batch prediction completed!");
}

// ================= LIVE STREAM =================
const evt = new EventSource('/stream');

evt.onmessage = (e) => {
  const data = JSON.parse(e.data);
  const li = document.createElement("li");

  li.innerHTML = `₹${data.amount} → ${data.prediction ? "⚠️ Fraud" : "✅ Safe"}`;

  document.getElementById("liveFeed").prepend(li);
};
