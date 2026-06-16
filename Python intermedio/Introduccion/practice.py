

# class Car:
#     wheel_number = 6

#     def my_first_method(self):
#         print("Hello OOP World")

# my_car = Car()

# my_car.my_first_method()


class PhotographyCamera:
    photograpies = []

    def __init__(self, storage_size_in_mb):
        #each photo takes around 10mb
        self.max_photographies = storage_size_in_mb/10

    
    def take_photo(self, photography):
        if len(self.photograpies) >= self.max_photographies:
            print("The storage is full")
            return
        
        self.photograpies.append(photography)

kodak_camera = PhotographyCamera(50)
kodak_camera.take_photo("My car")
kodak_camera.take_photo("My house")
kodak_camera.take_photo("My dog")
kodak_camera.take_photo("The cat")
kodak_camera.take_photo("The garden")
kodak_camera.take_photo("My family")

print(kodak_camera.photograpies)