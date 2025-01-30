class KPICalculator:
    def prompt_fallback(self, kpi_name):
       
        return int(input(f"Enter the value for {kpi_name}: "))

    def calculate_new_visitors(self, users):
        if not users:
            return self.prompt_fallback("new visitors")
        return len([user for user in users if user.get('signup_date') == '2025-01-27'])

    def calculate_new_signups(self, users):
        if not users:
            return self.prompt_fallback("new signups")
        return len([user for user in users if user.get('is_signed_up')])

    def calculate_demo_calls(self, calls):
        if not calls:
            return self.prompt_fallback("demo calls")
        return len([call for call in calls if call.get('campaignId') == 'demo'])

    def calculate_calls_without_errors(self, calls):
        if not calls:
            return self.prompt_fallback("calls without errors")
        return len([call for call in calls if call.get('error') is None])

    def calculate_calls_connected(self, calls):
        if not calls:
            return self.prompt_fallback("calls connected")
        return len([call for call in calls if call.get('status') == 'connected'])

    def calculate_calls_longer_than_29_sec(self, calls):
        if not calls:
            return self.prompt_fallback("calls longer than 29 seconds")
        return len([call for call in calls if call.get('duration') > 29])

    def calculate_active_subscriptions(self, subscriptions):
        if not subscriptions:
            return self.prompt_fallback("active subscriptions")
        return len([sub for sub in subscriptions if sub.get('status') == 'active'])

    def calculate_canceled_subscriptions(self, subscriptions):
        if not subscriptions:
            return self.prompt_fallback("canceled subscriptions")
        return len([sub for sub in subscriptions if sub.get('status') == 'canceled'])