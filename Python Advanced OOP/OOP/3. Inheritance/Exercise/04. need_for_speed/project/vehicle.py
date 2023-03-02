class Vehicle:
    DEFAULT_FUEL_CONSUMPTION: [float, int] = 1.25

    def __init__(self, fuel: float, horse_power: int):
        self.fuel = fuel
        self.horse_power = horse_power
        self.fuel_consumption = self.DEFAULT_FUEL_CONSUMPTION

    def drive(self, kilometers) -> None:
        predicted_fuel = self.fuel_consumption * kilometers

        if predicted_fuel <= self.fuel:
            self.fuel -= predicted_fuel