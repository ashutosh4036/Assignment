def format_kpi_message(kpi_data):
    message = ""
    for key, value in kpi_data.items():
        comparison = value.get('comparison', "")
        message += f"*{key.replace('_', ' ').title()}:* {value['value']} ({comparison})\n"
    return message