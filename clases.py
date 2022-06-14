class Dinosaur:
    def __init__(self, name, type, number, period, named_by):
        self.name = name
        self.type = type
        self.number = number
        self.period = period
        self.named_by = named_by

    def __str__(self):
        return f'{self.name}, {self.type}, {self.number}, {self.period}, {self.named_by}'

class Alert:
    def __init__(self, time, zone_code, dino_number, alert_level, dino_name, dino_type):
        self.time = time
        self.zone_code = zone_code
        self.dino_number = dino_number
        self.alert_level = alert_level
        self.dino_name = dino_name
        self.dino_type = dino_type

    def __str__(self):
        return f'{self.time}, {self.zone_code}, {self.dino_number}, {self.alert_level}, {self.dino_name}, {self.dino_type}'


        