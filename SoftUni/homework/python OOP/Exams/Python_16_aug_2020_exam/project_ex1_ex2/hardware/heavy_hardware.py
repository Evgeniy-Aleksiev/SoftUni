from project.hardware.hardware import Hardware


class HeavyHardware(Hardware):
    _HARDWARE_TYPE = 'Heavy'

    def __init__(self, name: str, capacity: int, memory: int):
        super().__init__(name, self._HARDWARE_TYPE, capacity * 2, round(memory * 0.75))
