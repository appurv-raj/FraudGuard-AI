<h1 align="center">💳 FraudGuard AI - Credit Card Fraud Detection System</h1>

<p align="center">
AI-powered fraud risk assessment system built using Machine Learning and Flask.
</p>

<hr>

<h2>🚀 Project Overview</h2>

<p>
FraudGuard AI is a web-based fraud detection system that predicts the probability of a transaction being fraudulent. 
It uses a trained CatBoost classification model and provides a risk score with visual feedback including a progress bar and probability chart.
</p>

<p>
The system separates display inputs (like Transaction ID) from predictive features and extracts only relevant data such as the hour from transaction time for modeling.
</p>

<hr>

<h2>🛠 Technology Stack</h2>

<ul>
<li><b>Backend:</b> Python, Flask</li>
<li><b>Machine Learning:</b> CatBoost, Scikit-learn</li>
<li><b>Data Processing:</b> Pandas, NumPy</li>
<li><b>Frontend:</b> HTML, CSS, JavaScript</li>
<li><b>Visualization:</b> Chart.js</li>
<li><b>Deployment:</b> Render, Gunicorn</li>
</ul>

<hr>

<h2>🧠 Architecture / Workflow</h2>

<p>
User inputs transaction details → Flask backend processes the data → Relevant features are structured into a DataFrame → 
CatBoost model predicts fraud probability → Risk score (0–100%) is generated → 
Results are displayed with visual risk indicators.
</p>

<hr>

<h2>📊 Dataset Used</h2>

<p>
The model was trained on a Credit Card Fraud Detection dataset containing structured transaction features such as:
</p>

<ul>
<li>Transaction Amount</li>
<li>Merchant ID</li>
<li>Transaction Type</li>
<li>Location</li>
<li>Date & Time</li>
<li>Fraud Label (Binary)</li>
</ul>

<p>
The dataset was used for supervised binary classification (Fraud / Not Fraud).
</p>

<hr>

<h2>✨ Key Features</h2>

<ul>
<li>Probability-based fraud scoring (not just binary prediction)</li>
<li>Interactive risk visualization (Donut Chart + Progress Bar)</li>
<li>Realistic transaction simulation interface</li>
<li>Responsive modern UI</li>
<li>Clean feature engineering (hour extraction from time)</li>
</ul>

<hr>

<h2>📈 Future Scope & Scalability</h2>

<p>
Currently, the project is a functional prototype. In future iterations, it can be scaled into a cloud-based microservice, 
integrated with real-time payment APIs, enhanced with behavioral profiling, and optimized for handling high-volume transaction streams.
</p>

<hr>

<h2>🎯 Target Users</h2>

<p>
Banks, fintech startups, payment gateways, e-commerce platforms, and financial institutions. 
End users benefit through improved transaction security and fraud prevention.
</p>

<hr>

<h2>⚙️ How to Run Locally</h2>

<pre>
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
pip install -r requirements.txt
python main.py
</pre>

<p>
Then open: <b>http://127.0.0.1:5000</b>
</p>

<hr>

<h2>📌 License</h2>

<p>
This project uses open-source libraries including Flask, CatBoost, Pandas, NumPy, Scikit-learn, and Chart.js.
</p>

<hr>

<p align="center">
Built for Hackathon | Machine Learning + Web Deployment
</p>
