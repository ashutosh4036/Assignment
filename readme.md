VoiceGenie KPI Automation - 

Overview

This repository contains a script that automates the generation and presentation of daily Key Performance Indicators (KPIs) for the VoiceGenie product. The script retrieves data from a simulated MongoDB database, processes it, stores it compactly in daily_kpi.json, and formats it for Slack messaging.

Features

Automated KPI Calculation: Extracts and computes KPI values automatically.

Fallback Mechanism: Prompts for manual input when data is missing.

Compact Storage: Stores daily KPI data efficiently in a JSON file.

Modular Codebase: Structured into separate modules for maintainability.

Historical KPI Generation: Supports generating KPI reports for past dates.

Easy Integration: Future-ready for additional KPIs and automation enhancements.

File Structure

voicegenie_kpi_project/
|-- db_connector.py      # Handles MongoDB connections and data retrieval
|-- kpi_calculator.py    # Computes KPI values
|-- file_handler.py      # Manages the JSON file storing KPI data
|-- formatter.py         # Formats KPI output for Slack
|-- main.py              # Main execution script
|-- daily_kpi.json       # Stores computed KPI data
|-- README.md            # Documentation (this file)

Prerequisites

Python 3.7+

MongoDB installed and running locally

Required dependencies:

pip install pymongo

Installation & Execution

1. Clone the Repository

git clone <repository-url>
cd voicegenie_kpi_project

2. Set Up MongoDB

Ensure MongoDB is running at mongodb://localhost:27017.

3. Run the Script

python main.py

4. (Optional) Set Alias for Quick Execution

echo 'alias vg-kpi="python /path/to/main.py"' >> ~/.bashrc
source ~/.bashrc

Then, execute:

vg-kpi

Configuration

Database Settings: Modify db_connector.py to update connection details.

KPI Customization: Update kpi_calculator.py to add or modify calculations.

Message Formatting: Customize formatter.py for Slack output formatting.

Sample Output

*KPI Report for 2025-01-27:*
*New Visitors:* 3
*New Signups:* 3
*Demo Calls:* 3
*Calls Without Errors:* 3
*Calls Connected:* 3
*Calls Longer Than 29 Sec:* 3
*Active Subscriptions:* 3
*Canceled Subscriptions:* 1

Troubleshooting

1. Duplicate Key Error in MongoDB

If you encounter E11000 duplicate key error, clear existing data:

from pymongo import MongoClient
client = MongoClient("mongodb://localhost:27017")
db = client["voicegenie"]
db["users"].delete_many({})
db["CallSessionHistories"].delete_many({})
db["subscriptions"].delete_many({})

2. Missing Data Prompt

If data is missing, the script will prompt for manual input. Ensure MongoDB has valid data to minimize prompts.

Future Enhancements

Automate currently manual KPI retrieval.

Integrate Slack API for direct message posting.

Implement logging and advanced error handling.

Contributing

Feel free to fork this repository and submit pull requests for improvements.

Author

Ashutosh Tripathi

License

This project is licensed under the MIT License.