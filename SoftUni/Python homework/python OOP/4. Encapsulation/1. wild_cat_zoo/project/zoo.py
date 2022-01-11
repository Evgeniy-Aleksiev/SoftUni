class Zoo:
    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.name = name
        self.budget = budget
        self.animal_capacity = animal_capacity
        self.workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    @property
    def budget(self):
        return self.__budget

    @budget.setter
    def budget(self, value):
        self.__budget = value

    @property
    def animal_capacity(self):
        return self.__animal_capacity

    @animal_capacity.setter
    def animal_capacity(self, value):
        self.__animal_capacity = value

    @property
    def workers_capacity(self):
        return self.__workers_capacity

    @workers_capacity.setter
    def workers_capacity(self, value):
        self.__workers_capacity = value

    def add_animal(self, animal, price):
        if self.budget < price:
            return 'Not enough budget'
        if len(self.animals) >= self.animal_capacity:
            return 'Not enough space for animal'

        self.budget -= price
        self.animals.append(animal)
        return f'{animal.name} the {animal.__class__.__name__} added to the zoo'

    def hire_worker(self, worker):
        if len(self.workers) >= self.workers_capacity:
            return 'Not enough space for worker'

        self.workers.append(worker)
        return f'{worker.name} the {worker.__class__.__name__} hired successfully'

    def fire_worker(self, worker_name):
        for worker in self.workers:
            if worker.name == worker_name:
                self.workers.remove(worker)
                return f'{worker_name} fired successfully'

        return f'There is no {worker_name} in the zoo'

    def pay_workers(self):
        total_salary_sum = sum([x.salary for x in self.workers])

        if total_salary_sum > self.budget:
            return 'You have no budget to pay your workers. They are unhappy'

        self.budget -= total_salary_sum
        return f'You payed your workers. They are happy. Budget left: {self.budget}'

    def tend_animals(self):
        budget_to_take_care = sum([x.money_for_care for x in self.animals])

        if budget_to_take_care > self.budget:
            return 'You have no budget to tend the animals. They are unhappy.'

        self.budget -= budget_to_take_care
        return f'You tended all the animals. They are happy. Budget left: {self.budget}'

    def profit(self, amount):
        self.budget += amount

    def animals_status(self):
        result = f'You have {len(self.animals)} animals\n'

        result += self.__get_object_status_by_type('Lion', self.animals)
        result += self.__get_object_status_by_type('Tiger', self.animals)
        result += self.__get_object_status_by_type('Cheetah', self.animals)

        return result.strip()

    def workers_status(self):
        result = f'You have {len(self.workers)} workers\n'

        result += self.__get_object_status_by_type('Keeper', self.workers)
        result += self.__get_object_status_by_type('Caretaker', self.workers)
        result += self.__get_object_status_by_type('Vet', self.workers)

        return result.strip()

    def __get_object_status_by_type(self, object_type, object_list):
        objects = [str(x) for x in object_list if x.__class__.__name__ == object_type]

        result = f'----- {len(objects)} {object_type}s:\n'

        for obj in objects:
            result += obj
            result += '\n'

        return result

