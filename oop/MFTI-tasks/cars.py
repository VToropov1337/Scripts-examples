import csv
import os


class BaseCar(object):
    def __init__(self, car_type, brand, photo_file_name, carrying):
        self.car_type = car_type
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = float(carrying)
        
    def __str__(self):
        return self.car_type
        
    def __repr__(self):
            return self.car_type
    
    
    def get_photo_file_ext(self):
        return os.path.splitext(self.photo_file_name)[1]
            
    
class Car(BaseCar):
    def __init__(self, car_type,brand, photo_file_name, carrying, passenger_seats_count):
        super().__init__(car_type,brand,photo_file_name,carrying)
        self.passenger_seats_count = int(passenger_seats_count)
    
    
class Truck(BaseCar):
    def __init__(self,car_type, brand, photo_file_name, carrying, body_whl=None):
        super().__init__(car_type,brand,photo_file_name,carrying)
        self.body_whl = body_whl or 0
        if len(body_whl) != 0:
            self.body_width = float(body_whl.split('x')[0])
            self.body_height = float(body_whl.split('x')[1])
            self.body_lenght = float(body_whl.split('x')[2])
        else:
            self.body_width = 0
            self.body_height = 0
            self.body_lenght = 0

                
    def get_body_volume(self):
        if self.body_whl != 0:
            sum = 1
            data = self.body_whl.split('x')

            for i in range(len(data)):
                data[i] = float(data[i])
                sum = sum * float(data[i])
            return sum
        else:
            return 0
        
            
class SpecMachine(BaseCar):
    def __init__(self, car_type,brand, photo_file_name, carrying, extra):
        super().__init__(car_type,brand,photo_file_name,carrying)
        self.extra = extra


def get_car_list(csv_filename):
    car_list = []
    with open(csv_filename,'r',newline="") as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            if len(row) == 0:
                continue
            else:
                row = row[0].split(';')
                if row[0] == 'car':
                    car_list.append(Car(row[0],row[1],row[3],row[5],row[2]))
                if row[0] == 'truck':
                    car_list.append(Truck(row[0],row[1],row[3],row[5],row[4]))
                if row[0] == 'spec_machine':
                    car_list.append(SpecMachine(row[0],row[1],row[3],row[5],row[6]))

    return car_list



if __name__ == '__main__':

    car_list = get_car_list('cars.csv')
    for i in car_list:
        print(i.__dict__)
