from db_connector import DBConnector
from kpi_calculator import KPICalculator
from file_handler import FileHandler
from formatter import format_kpi_message

if __name__ == "__main__":
    
    db = DBConnector()
    kpi_calculator = KPICalculator()
    file_handler = FileHandler()

    
    db.insert_dummy_data()

    
    users = db.fetch_data("users", {})
    calls = db.fetch_data("CallSessionHistories", {})
    subscriptions = db.fetch_data("subscriptions", {})

    
    kpis = {
        "new_visitors": {"value": kpi_calculator.calculate_new_visitors(users)},
        "new_signups": {"value": kpi_calculator.calculate_new_signups(users)},
        "demo_calls": {"value": kpi_calculator.calculate_demo_calls(calls)},
        "calls_without_errors": {"value": kpi_calculator.calculate_calls_without_errors(calls)},
        "calls_connected": {"value": kpi_calculator.calculate_calls_connected(calls)},
        "calls_longer_than_29_sec": {"value": kpi_calculator.calculate_calls_longer_than_29_sec(calls)},
        "active_subscriptions": {"value": kpi_calculator.calculate_active_subscriptions(subscriptions)},
        "canceled_subscriptions": {"value": kpi_calculator.calculate_canceled_subscriptions(subscriptions)}
    }

    
    file_handler.update_kpi("2025-01-27", kpis)

    
    message = format_kpi_message(kpis)
    print("KPI Message for Slack:\n")
    print(message)