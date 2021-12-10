from project.software.software import Software


class Hardware:
    def __init__(self, name: str, hardware_type: str, capacity: int, memory: int):
        self.name = name
        self.hardware_type = hardware_type
        self.capacity = capacity
        self.memory = memory
        self.software_components = []       # contain all software components installed on that hardware

    def install(self, software: Software):
        software_capacity_consumption = software.capacity_consumption
        software_memory_consumption = software.memory_consumption

        if self.memory < software_capacity_consumption or self.memory < software_memory_consumption:
            raise Exception('Software cannot be installed')

        self.software_components.append(software)

    def uninstall(self, software: Software):
        self.software_components.remove(software)