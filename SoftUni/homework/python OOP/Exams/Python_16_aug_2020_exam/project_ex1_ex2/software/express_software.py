from project.software.software import Software


class ExpressSoftware(Software):
    _SOFTWARE_TYPE = 'Express'

    def __init__(self, name: str, capacity_consumption: int, memory_consumption: int):
        super().__init__(name, self._SOFTWARE_TYPE, capacity_consumption, memory_consumption * 2)
