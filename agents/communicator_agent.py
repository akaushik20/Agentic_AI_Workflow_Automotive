
from datetime import datetime

class ComunicationAgent:
    def __init__(self, state):
        self.state = state
        self.insight = self.state.get('battery_insight', {})
        self.plan = self.state.get('service_plan', {})
        self.appointment = self.state.get('appointment', {})

    def summary_insight(self):
        soh = self.insight.get("latest_soh", "Unknown")
        anomalies = self.insight.get("anomalies", [])
        decline = self.insight.get("decline_types", {})
        avg_loss = self.insight.get("average_loss_per_cycle", "Unknown")

        summary = f"""Battery State of Health (SoH): {soh}%.\n
        The system detected {len(anomalies)} anomalies and an average SoH decline of {avg_loss} per cycle.\n"""

        return summary
    
    def summarize_plan(self):
        return self.plan.get("action", "No clear service recommendation found.")
    
    def summarize_appointment(self):
        if self.appointment.get("status") == "scheduled":
            dealer = self.appointment.get("dealer", "Unknown Dealer")
            slot = self.appointment.get("slot", "Unknown Slot")
            method = self.appointment.get("method", "Unknown Method")
            return f"Appointment scheduled with {dealer} on {slot} via {method}."
        else:
            return "No appointment scheduled."
    
    def email_summary(self):

        if self.appointment.get("status") != "scheduled":
            self.state["user_message"] = "No appointment scheduled, email summary not generated."
            return self.state
                
        insight_summary = self.summary_insight()
        plan_summary = self.summarize_plan()
        appointment_summary = self.summarize_appointment()

        email_content = f"""
        Subject: Battery Health and Service Summary

        Dear User,

        Here is the summary of your vehicle's battery health and service plan:

        Battery Insight:
        {insight_summary}

        Service Plan:
        {plan_summary}

        Appointment Details:
        {appointment_summary}

        Best regards,
        Your Vehicle Maintenance Team
        """
        self.state["user_message"] = email_content
        return self.state
    
if __name__ == "__main__":
    mock_state = {
        "battery_insight": {
            "status": "moderate degradation",
            "recommendation": "Monitor battery health closely.",
            "anomalies": ["2023-01-15", "2023-03-22"],
            "average_loss_per_cycle": 0.15,
            "decline_types": {
                "fast_avg_drop": 0.25,
                "slow_avg_drop": 0.1
            },
            "anomalies_count": 2,
            "highlight_dates": ["2023-02-10", "2023-04-05"],
            "latest_soh": 85.5
        },
        "service_plan": {
            "action": "Schedule service within the next month. Focus on battery health monitoring.",
            "urgency": "medium",
            "source_status": "moderate degradation"
        },
        "appointment": {
            "status": "scheduled",
            "dealer": "Dealer_B",
            "slot": datetime(2023, 11, 15, 11, 0),
            "method": "auto-selected by scheduler agent"
        }
    }
    agent = ComunicationAgent(mock_state)
    updated_state = agent.email_summary()
    print(updated_state["user_message"])
        