# VoiceGenie KPI Automation

Welcome to the VoiceGenie KPI Automation repository! This project automates the generation and presentation of daily Key Performance Indicators (KPIs) for the VoiceGenie product.

## 📊 Overview
VoiceGenie KPI Automation retrieves data from a MongoDB database, processes it, stores it in `daily_kpi.json`, and formats it for Slack messaging. This helps in monitoring business metrics efficiently.

## 🚀 Features
- **Automated KPI Calculation** – Extracts and computes KPI values automatically.
- **Fallback Mechanism** – Prompts for manual input when data is missing.
- **Compact Storage** – Efficiently stores daily KPI data in JSON format.
- **Modular Codebase** – Well-structured modules for better maintainability.
- **Historical KPI Reporting** – Allows generation of reports for past dates.
- **Scalability** – Easily integrates additional KPIs and automation features.

## 🛠️ Technologies Used
- **Programming Language:** Python 3.7+
- **Database:** MongoDB
- **Dependencies:** Pymongo

## 📂 Project Structure
```
voicegenie_kpi_project/
│-- db_connector.py      # Manages MongoDB connections and data retrieval
│-- kpi_calculator.py    # Computes KPI values
│-- file_handler.py      # Handles JSON data storage
│-- formatter.py         # Formats KPI output for Slack
│-- main.py              # Main script for execution
│-- daily_kpi.json       # Stores computed KPI data
│-- README.md            # Project documentation (this file)
```

## 📦 Installation & Execution

### 1️⃣ Clone the Repository
```bash
git clone <repository-url>
cd voicegenie_kpi_project
```

### 2️⃣ Install Dependencies
```bash
pip install pymongo
```

### 3️⃣ Ensure MongoDB is Running
Ensure MongoDB is running at `mongodb://localhost:27017`.

### 4️⃣ Run the Script
```bash
python main.py
```

### 5️⃣ (Optional) Set Up an Alias for Quick Execution
```bash
echo 'alias vg-kpi="python /path/to/main.py"' >> ~/.bashrc
source ~/.bashrc
```
Then, execute:
```bash
vg-kpi
```

## ⚙️ Configuration
- **Database Settings** – Modify `db_connector.py` to update database connection details.
- **KPI Customization** – Edit `kpi_calculator.py` to define new KPIs or modify existing calculations.
- **Slack Message Formatting** – Customize `formatter.py` to tailor Slack notifications.

## 📊 Sample Output
```
*KPI Report for 2025-01-27:*
*New Visitors:* 3
*New Signups:* 3
*Demo Calls:* 3
*Calls Without Errors:* 3
*Calls Connected:* 3
*Calls Longer Than 29 Sec:* 3
*Active Subscriptions:* 3
*Canceled Subscriptions:* 1
```

## 🔧 Troubleshooting

### ❌ Duplicate Key Error in MongoDB
If you encounter `E11000 duplicate key error`, clear existing data:
```python
from pymongo import MongoClient
client = MongoClient("mongodb://localhost:27017")
db = client["voicegenie"]
db["users"].delete_many({})
db["CallSessionHistories"].delete_many({})
db["subscriptions"].delete_many({})
```

### ⚠️ Missing Data Prompt
If data is missing, the script will prompt for manual input. Ensure MongoDB contains valid data to reduce prompts.

## 🚀 Future Enhancements
- Fully automate currently manual KPI retrieval.
- Integrate Slack API for direct report posting.
- Implement logging and advanced error handling.

## 🤝 Contributing
We welcome contributions! Feel free to fork this repository, submit pull requests, or suggest improvements.

## 👤 Author
**Ashutosh Tripathi**

## 📜 License
This project is licensed under the **MIT License**.

---
Thank you for using VoiceGenie KPI Automation!
