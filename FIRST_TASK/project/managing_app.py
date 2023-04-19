from project.user import User
from project.vehicles.base_vehicle import BaseVehicle
from project.route import Route
from project.vehicles.cargo_van import CargoVan
from project.vehicles.passenger_car import PassengerCar


class ManagingApp():
    def __init__(self):
        self.users: list[User] = []
        self.vehicles : list[BaseVehicle] = []
        self.routes : list[Route] = []

    def register_user(self, first_name: str, last_name: str, driving_license_number: str):
        for person in self.users:
            if driving_license_number == person.driving_license_number:
                return f"{driving_license_number} has already been registered to our platform."
        person = User(first_name, last_name, driving_license_number)
        self.users.append(person)
        return f"{person.first_name} {person.last_name} was successfully registered under DLN-{person.driving_license_number}"

    def upload_vehicle(self, vehicle_type: str, brand: str, model: str, license_plate_number: str):
        if vehicle_type != "PassengerCar" and vehicle_type != "CargoVan":
            return f"Vehicle type {vehicle_type} is inaccessible."
        for vehicle in self.vehicles:
            if license_plate_number == vehicle.license_plate_number:
                return f"{license_plate_number} belongs to another vehicle."
        if vehicle_type == "PassengerCar":
            vehicle = PassengerCar(brand, model, license_plate_number)
        elif vehicle_type == "CargoVan":
            vehicle = CargoVan(brand, model, license_plate_number)
        self.vehicles.append(vehicle)
        return f"{brand} {model} was successfully uploaded with LPN-{license_plate_number}."

    def allow_route(self, start_point: str, end_point: str, length: float):
        route_counter = len(self.routes) + 1
        for route in self.routes:
            if route.start_point == start_point and route.end_point == end_point and route.length == length:
                return f"{start_point}/{end_point} - {length} km had already been added to our platform."
            elif route.start_point == start_point and route.end_point == end_point and route.length < length:
                return f"{start_point}/{end_point} shorter route had already been added to our platform."
        route = Route(start_point, end_point, length, route_id=route_counter)
        self.routes.append(route)
        return f"{route.start_point}/{route.end_point} - {route.length} km is unlocked and available to use."

    def make_trip(self, driving_license_number: str, license_plate_number: str, route_id: int,  is_accident_happened: bool):
        driving_vehicle = None
        driving_route = None
        driving_person = None
        for person in self.users:
            if person.is_blocked:
                return f"User {driving_license_number} is blocked in the platform! This trip is not allowed."
            driving_person = person
        for vehicle in self.vehicles:
            if vehicle.is_damaged:
                return f"Vehicle {license_plate_number} is damaged! This trip is not allowed."
            driving_vehicle = vehicle
        for route in self.routes:
            if route.is_locked:
                return f"Route {route_id} is locked! This trip is not allowed."
            driving_route = route
        driving_vehicle.drive(driving_route.length)

        if is_accident_happened:
            driving_vehicle.is_damaged = True
            driving_person.decrease_rating()
        else:
            driving_person.increase_rating()

        is_damaged = "Damaged" if driving_vehicle.is_damaged else "OK"
        return f"{driving_vehicle.brand} {driving_vehicle.model} License plate: {driving_vehicle.license_plate_number} Battery: {driving_vehicle.battery_level}% Status: {is_damaged}"

    def repair_vehicles(self, count: int):
        repair_collection = []
        for vehicle in self.vehicles:
            if vehicle.is_damaged:
                repair_collection.append(vehicle)

        for vehicles in repair_collection:
            vehicles.is_damaged = False
            vehicles.recharge()

        repair_collection.sort(key=lambda x: (x.brand, x.model))

    def users_report(self):
        pass
