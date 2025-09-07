import pandas as pd

class ServicePlannerAgent:

    def __init__(self, state):
        """
        Initializes the Service Planner Agent with shared workflow state.
        Requires 'battery_insight' key in the state.
        """
        self.state = state
        self.insight = self.state.get('battery_insight', {})
    
    def plan_service(self):

        status = self.insight.get("status", "unknown")

        if status == "rapid degradation":
            action = "Immediate service required. Prioritize battery inspection and replacement."
            urgency = "high"
            source_status = status
        elif status == "moderate degradation":
            action = "Schedule service within the next month. Focus on battery health monitoring."
            urgency = "medium"
            source_status = status
        elif status == "normal degradation":
            action = "Routine service as per schedule. No immediate action needed."
            urgency = "low"
            source_status = status
        else:
            action = "Unable to determine action due to missing status."
            urgency = "unknown"
            source_status = status
        service_plan = {
            "action": action,
            "urgency": urgency,
            "source_status": source_status
        }
        return service_plan
    def plan(self):
        decision = self.plan_service()
        self.state["service_plan"] = decision
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
        }
    }
    agent = ServicePlannerAgent(mock_state)
    updated_state = agent.plan()
    print("Service Plan")
    for key, value in updated_state["service_plan"].items():
        print(f"{key}: {value}")


    
        