class Gym:
    def __init__(self):
        self.customers = []
        self.trainers = []
        self.equipment = []
        self.plans = []
        self.subscriptions = []

    def add_customer(self, customer):
        if customer in self.customers:
            return
        self.customers.append(customer)

    def add_trainer(self, trainer):
        if trainer in self.trainers:
            return
        self.trainers.append(trainer)

    def add_equipment(self, equipment):
        if equipment in self.equipment:
            return
        self.equipment.append(equipment)

    def add_plan(self, plan):
        if plan in self.plans:
            return
        self.plans.append(plan)

    def add_subscription(self, subscription):
        if subscription in self.subscriptions:
            return
        self.subscriptions.append(subscription)

    def subscription_info(self, subscription_id):
        subscription = self.__get_obj_by_id(self.subscriptions, subscription_id)
        customer = self.__get_obj_by_id(self.customers, subscription_id)
        trainer = self.__get_obj_by_id(self.trainers, subscription_id)
        equipment = self.__get_obj_by_id(self.equipment, subscription_id)
        plan = self.__get_obj_by_id(self.plans, subscription_id)

        result = str(subscription) + '\n'
        result += str(customer) + '\n'
        result += str(trainer) + '\n'
        result += str(equipment) + '\n'
        result += str(plan)

        return result

    @staticmethod
    def __get_obj_by_id(objects, obj_id):
        for obj in objects:
            if obj.id == obj_id:
                return obj
