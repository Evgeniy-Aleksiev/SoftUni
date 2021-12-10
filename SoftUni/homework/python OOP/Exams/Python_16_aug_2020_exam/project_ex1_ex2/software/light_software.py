from project.software.software import Software


class LightSoftware(Software):
    _SOFTWARE_TYPE = 'Light'

    def __init__(self, name: str, capacity_consumption: int, memory_consumption: int):
        capacity_consumption_fifty_percent_more = round((capacity_consumption * 0.5) + capacity_consumption)
        memory_consumption_fifty_percent_less = round(memory_consumption * 0.5)

        super().__init__(name, self._SOFTWARE_TYPE, capacity_consumption_fifty_percent_more,
                         memory_consumption_fifty_percent_less)