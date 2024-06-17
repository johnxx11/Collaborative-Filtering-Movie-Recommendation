class KNN:
    def __init__(self, user_id: int, sim: float):
        self.user_id = user_id
        self.sim = sim

    def get_sim(self) -> float:
        return self.sim

    def get_user_id(self) -> int:
        return self.user_id