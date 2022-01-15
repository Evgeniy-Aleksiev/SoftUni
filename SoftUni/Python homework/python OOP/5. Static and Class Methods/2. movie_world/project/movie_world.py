class MovieWorld:
    def __init__(self, name):
        self.name = name
        self.customers = []
        self.dvds = []

    @staticmethod
    def dvd_capacity():
        return 15

    @staticmethod
    def customer_capacity():
        return 10

    def add_customer(self, customer):
        if MovieWorld.customer_capacity() == len(self.customers):
            return
        self.customers.append(customer)

    def add_dvd(self, dvd):
        if MovieWorld.dvd_capacity() == len(self.dvds):
            return
        self.dvds.append(dvd)

    def rent_dvd(self, customer_id, dvd_id):
        customer = self.__get_obj_by_id(self.customers, customer_id)
        dvd = self.__get_obj_by_id(self.dvds, dvd_id)

        if dvd in customer.rented_dvds:
            return f'{customer.name} has already rented {dvd.name}'
        if dvd.is_rented:
            return "DVD is already rented"
        if customer.age < dvd.age_restriction:
            return f'{customer.name} should be at least {dvd.age_restriction} to rent this movie'

        customer.rented_dvds.append(dvd)
        dvd.is_rented = True
        return f'{customer.name} has successfully rented {dvd.name}'

    def return_dvd(self, customer_id, dvd_id):
        customer = self.__get_obj_by_id(self.customers, customer_id)
        dvd = self.__get_obj_by_id(self.dvds, dvd_id)

        if dvd in customer.rented_dvds:
            customer.rented_dvds.remove(dvd)
            dvd.is_rented = False
            return f'{customer.name} has successfully returned {dvd.name}'

        return f'{customer.name} does not have that DVD'

    def __repr__(self):
        customers = '\n'.join([str(x) for x in self.customers])
        dvds = '\n'.join([str(x) for x in self.dvds])
        return customers + '\n' + dvds

    @staticmethod
    def __get_obj_by_id(objects, id):
        for object in objects:
            if object.id == id:
                return object
