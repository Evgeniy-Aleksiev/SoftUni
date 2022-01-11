from project.hardware.hardware import Hardware


class PowerHardware(Hardware):
    _HARDWARE_TYPE = 'Power'

    def __init__(self, name: str, capacity: int, memory: int):
        power_hardware_memory = round((memory * 0.75) + memory)

        super().__init__(name, self._HARDWARE_TYPE, round(capacity * 0.25), power_hardware_memory)