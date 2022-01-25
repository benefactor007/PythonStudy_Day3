class Taxi:

    def __init__(self, drivername, onduty, cities):
        self.drivername = drivername
        self.onduty = onduty
        self.cities = cities

    def __str__(self):
        return '{} {} {}'.format(self.drivername, self.onduty, self.cities)


class Type(Taxi):

    def __init__(self, drivername, onduty, cities, model):
        super().__init__(drivername, onduty, cities)
        self.model = model

    def __str__(self):
        prefix = super().__str__()
        return '{} {}'.format(prefix, self.model)


mymodel = Type('Foobar', True, 'Washington', 'Volvo')
print(mymodel)
