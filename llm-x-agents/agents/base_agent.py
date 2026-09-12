class BaseSpecialistAgent:
    def __init__(self, agent_id: str, competency: str):
        self.agent_id = agent_id
        self.competency = competency
        self.integrity_score = 1.00

    def execute_routine(self, payload: dict) -> dict:
        return {
            "agent_id": self.agent_id,
            "competency": self.competency,
            "status": "executed",
            "integrity": self.integrity_score
        }
