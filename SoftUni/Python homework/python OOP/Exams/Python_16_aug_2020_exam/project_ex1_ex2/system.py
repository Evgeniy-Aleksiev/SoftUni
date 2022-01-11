from project.hardware.heavy_hardware import HeavyHardware
from project.hardware.power_hardware import PowerHardware
from project.software.express_software import ExpressSoftware
from project.software.light_software import LightSoftware


def install_software(software, sw_capacity, sw_memory, sw_list, hardware, hw_capacity, hw_memory):
    if sw_capacity <= hw_capacity and sw_memory <= hw_memory:
        sw_list.append(software)
        hardware.install(software)
        return

    raise Exception('Software cannot be installed')


def check_if_exist(component_list, component_name):
    for component in component_list:
        if component.name == component_name:
            return component
    return False


def get_total_memory_consumption(software: list, hw_memory_sym: int):
    sw_consumption = sum([sw.memory_consumption for sw in software])
    return f'{sw_consumption} / {hw_memory_sym}'


def get_total_capacity_consumption(software: list, hw_capacity_memory: int):
    sw_consumption = sum([sw.capacity_consumption for sw in software])
    return f'{sw_consumption} / {hw_capacity_memory}'


class System:
    _hardware = []
    _software = []

    @staticmethod
    def register_power_hardware(name: str, capacity: int, memory: int):
        power_hardware = PowerHardware(name, capacity, memory)
        System._hardware.append(power_hardware)

    @staticmethod
    def register_heavy_hardware(name: str, capacity: int, memory: int):
        heavy_hardware = HeavyHardware(name, capacity, memory)
        System._hardware.append(heavy_hardware)

    @staticmethod
    def register_express_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        for hardware in System._hardware:
            if hardware.name == hardware_name:
                express_software = ExpressSoftware(name, capacity_consumption, memory_consumption)
                install_software(express_software, capacity_consumption, memory_consumption,
                                 System._software, hardware, hardware.capacity, hardware.memory)
                return

        return 'Hardware does not exist'

    @staticmethod
    def register_light_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        for hardware in System._hardware:
            if hardware.name == hardware_name:
                light_software = LightSoftware(name, capacity_consumption, memory_consumption)
                install_software(light_software, capacity_consumption, memory_consumption,
                                 System._software, hardware, hardware.capacity, hardware.memory)
                return

        return 'Hardware does not exist'

    @staticmethod
    def release_software_component(hardware_name: str, software_name: str):
        hardware = check_if_exist(System._hardware, hardware_name)
        software = check_if_exist(System._software, software_name)

        if hardware and software:
            hardware.uninstall(software)
            System._software.remove(software)
            return

        return 'Some of the components do not exist'

    @staticmethod
    def analyze():
        number_of_hardware_components = len(System._hardware)
        number_of_software_components = len(System._software)

        memory_consumption = get_total_memory_consumption(System._software, sum([m.memory for m in System._hardware]))
        capacity_consumption = get_total_capacity_consumption(System._software, sum([c.capacity for c in System._hardware]))

        return f"""System Analysis
Hardware Components: {number_of_hardware_components}
Software Components: {number_of_software_components}
Total Operational Memory: {memory_consumption}
Total Capacity Taken: {capacity_consumption}"""

    @staticmethod
    def system_split():
        message, software, hardware = '', System._software, System._hardware

        for hw in hardware:
            express_sw = len([sw for sw in hw.software_components if sw.software_type == 'Express'])
            light_sw = len([sw for sw in hw.software_components if sw.software_type == 'Light'])
            memory_consumption = get_total_memory_consumption(hw.software_components, hw.memory)
            capacity_consumption = get_total_capacity_consumption(hw.software_components, hw.capacity)
            components = [x.name for x in hw.software_components]

            message += f'Hardware Component - {hw.name}\n'
            message += f'Express Software Components: {express_sw}\n'
            message += f'Light Software Components: {light_sw}\n'
            message += f'Memory Usage: {memory_consumption}\n'
            message += f'Capacity Usage: {capacity_consumption}\n'
            message += f'Type: {hw.hardware_type}\n'
            message += f"Software Components: {', '.join(components) if components else 'None'}\n"

        return message.strip()
