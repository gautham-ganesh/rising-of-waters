document.getElementById('predictionForm').addEventListener('submit', async (e) => {
    e.preventDefault();

    const resultDiv = document.getElementById('result');
    const riskLevel = document.getElementById('riskLevel');
    const probText = document.getElementById('probabilityText');
    resultDiv.style.display = 'none';

    const payload = {
        temp: document.getElementById('temp').value,
        humidity: document.getElementById('humidity').value,
        cloud_cover: document.getElementById('cloud_cover').value,
        annual_rainfall: document.getElementById('annual_rainfall').value,
        jan_feb: document.getElementById('jan_feb').value,
        mar_may: document.getElementById('mar_may').value,
        jun_sep: document.getElementById('jun_sep').value,
        oct_dec: document.getElementById('oct_dec').value,
        avg_june: document.getElementById('avg_june').value,
        sub_index: document.getElementById('sub_index').value
    };

    try {
        const response = await fetch('/predict', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(payload)
        });

        const result = await response.json();
        
        resultDiv.style.display = 'block';
        if (result.flood) {
            resultDiv.className = 'danger';
            riskLevel.innerText = 'WARNING: HIGH FLOOD RISK DETECTED';
            probText.innerText = `Flood Probability: ${result.flood_probability.toFixed(2)}% | Safety Chance: ${result.no_flood_probability.toFixed(2)}%`;
        } else {
            resultDiv.className = 'success';
            riskLevel.innerText = 'STATUS: SAFE - LOW FLOOD RISK';
            probText.innerText = `Flood Probability: ${result.flood_probability.toFixed(2)}% | Safety Chance: ${result.no_flood_probability.toFixed(2)}%`;
        }
    } catch (err) {
        resultDiv.style.display = 'block';
        resultDiv.className = 'danger';
        riskLevel.innerText = 'Error processing API request.';
        probText.innerText = '';
        console.error(err);
    }
});
