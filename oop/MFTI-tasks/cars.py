import csv
import os


class BaseCar(object):
    def __init__(self, car_type, brand, photo_file_name, carrying):
        self.car_type = car_type
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = carrying
        
    def __str__(self):
        return self.car_type
        
    def __repr__(self):
            return self.car_type
    
    
    def get_photo_file_ext(self):
        return os.path.splitext(self.photo_file_name)[1]
        
    
    
class Car(BaseCar):
    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
        super().__init__(brand,photo_file_name,carrying)
        self.passenger_seats_count = passenger_seats_count
    
    
class Truck(BaseCar):
    def __init__(self,car_type, brand, photo_file_name, carrying, body_whl=0):
        super().__init__(car_type,brand,photo_file_name,carrying)
        self.body_whl = body_whl
        self.body_width = int(self.body_whl.split('x')[0])
        self.body_height = int(self.body_whl.split('x')[1])
        self.body_lenght = int(self.body_whl.split('x')[2])
                
    def get_body_volume(self):
        sum = 1
        data = self.body_whl.split('x')
        
        for i in range(len(data)):
            data[i] = int(data[i])
            sum = sum * int(data[i])
            
        return sum
        
            
class SpecMachone(BaseCar):
    def __init__(self, brand, photo_file_name, carrying, extra):
        super().__init__(brand,photo_file_name,carrying)
        self.extra = extra
        
        
        
#подается файл-надо прочитать построчно и создать список нужных объектов. Функция должна возвращать список объектов        
def get_car_list(csv_filename):
    car_list = []
    return car_list
    
    
    
    
    
    
r = Truck('truck','toyota','wer.jpg',20,'8x4x2')

print(r.car_type,r.brand,r.carrying)

print(r.get_photo_file_ext())

print(r.get_body_volume())

print(r.body_lenght)

print(r)
