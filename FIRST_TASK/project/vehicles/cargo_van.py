from project.vehicles.base_vehicle import BaseVehicle


class CargoVan(BaseVehicle):
    max_mileage = 180.00

    def __init__(self, brand: str, model: str, license_plate_number: str):
        super().__init__(brand, model, license_plate_number, max_mileage=self.max_mileage)

    def drive(self, mileage):
        percentage = round((mileage / self.max_mileage) * 100)
        reduction = percentage * 0.05
        self.battery_level -= reduction
