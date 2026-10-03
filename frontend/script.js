* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: Arial, sans-serif;
    background: #0f172a;
    color: #f8fafc;
    min-height: 100vh;
}

.container {
    width: 92%;
    max-width: 1200px;
    margin: auto;
    padding: 30px 0;
}

/* Header */

header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 30px;
}

header h1 {
    font-size: 32px;
    margin-bottom: 8px;
}

header p {
    color: #94a3b8;
}

.status {
    background: #1e293b;
    padding: 10px 16px;
    border-radius: 30px;
    color: #cbd5e1;
    font-size: 14px;
}

.status span {
    display: inline-block;
    width: 9px;
    height: 9px;
    background: #22c55e;
    border-radius: 50%;
    margin-right: 7px;
}

/* Cards */

.card {
    background: #1e293b;
    border: 1px solid #334155;
    border-radius: 18px;
    padding: 25px;
    margin-bottom: 25px;
}

.card h2 {
    font-size: 21px;
    margin-bottom: 7px;
}

.subtitle {
    color: #94a3b8;
    font-size: 14px;
    margin-bottom: 25px;
}

/* Form */

.form-grid {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 20px;
}

.input-group {
    display: flex;
    flex-direction: column;
}

.input-group label {
    font-size: 14px;
    color: #cbd5e1;
    margin-bottom: 8px;
}

.input-group input,
.input-group select {
    padding: 13px;
    border-radius: 10px;
    border: 1px solid #475569;
    background: #0f172a;
    color: white;
    outline: none;
    font-size: 14px;
}

.input-group input:focus,
.input-group select:focus {
    border-color: #38bdf8;
}

/* Button */

button {
    width: 100%;
    margin-top: 25px;
    padding: 15px;
    border: none;
    border-radius: 11px;
    background: #38bdf8;
    color: #082f49;
    font-size: 16px;
    font-weight: bold;
    cursor: pointer;
    transition: 0.2s;
}

button:hover {
    transform: translateY(-2px);
    opacity: 0.9;
}

/* Dashboard Grid */

.dashboard-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 25px;
}

/* Prediction */

.prediction-card {
    text-align: center;
}

.circle-wrapper {
    display: flex;
    justify-content: center;
    margin: 30px 0;
}

.prediction-circle {
    width: 210px;
    height: 210px;
    border-radius: 50%;
    background: conic-gradient(
        #38bdf8 0deg,
        #38bdf8 220deg,
        #334155 220deg,
        #334155 360deg
    );
    display: flex;
    justify-content: center;
    align-items: center;
}

.circle-content {
    width: 170px;
    height: 170px;
    border-radius: 50%;
    background: #0f172a;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
}

.circle-content span {
    font-size: 43px;
    font-weight: bold;
}

.circle-content small {
    color: #94a3b8;
    margin-top: 5px;
}

#predictionMessage {
    color: #94a3b8;
}

/* Metrics */

.metric-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 15px;
    margin-top: 25px;
}

.metric {
    background: #0f172a;
    padding: 18px;
    border-radius: 12px;
    border: 1px solid #334155;
}

.metric span {
    display: block;
    color: #94a3b8;
    font-size: 13px;
    margin-bottom: 8px;
}

.metric strong {
    font-size: 21px;
}

/* Chart */

.chart {
    margin-top: 20px;
}

.chart-row {
    margin-bottom: 18px;
}

.chart-label {
    display: flex;
    justify-content: space-between;
    margin-bottom: 7px;
    font-size: 14px;
}

.chart-background {
    width: 100%;
    height: 12px;
    background: #0f172a;
    border-radius: 10px;
    overflow: hidden;
}

.chart-bar {
    height: 100%;
    background: #38bdf8;
    border-radius: 10px;
    transition: width 0.7s ease;
}

/* Summary */

.summary-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 15px;
}

.summary-grid div {
    background: #0f172a;
    padding: 15px;
    border-radius: 12px;
}

.summary-grid span {
    display: block;
    color: #94a3b8;
    font-size: 12px;
    margin-bottom: 7px;
}

.summary-grid strong {
    font-size: 15px;
}

/* Footer */

footer {
    text-align: center;
    color: #64748b;
    padding: 15px 0;
    font-size: 13px;
}

/* Responsive */

@media (max-width: 800px) {

    header {
        flex-direction: column;
        align-items: flex-start;
        gap: 15px;
    }

    .form-grid,
    .dashboard-grid {
        grid-template-columns: 1fr;
    }

    .summary-grid {
        grid-template-columns: repeat(2, 1fr);
    }
}

@media (max-width: 500px) {

    header h1 {
        font-size: 25px;
    }

    .summary-grid {
        grid-template-columns: 1fr;
    }

    .prediction-circle {
        width: 180px;
        height: 180px;
    }

    .circle-content {
        width: 145px;
        height: 145px;
    }

    .circle-content span {
        font-size: 35px;
    }
}