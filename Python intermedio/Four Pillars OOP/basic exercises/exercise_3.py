# Investigue qué usos se le pueden dar a la herencia multiple y cree un ejemplo.


class PersianCat:
    def __init__(self):
        self.coat = "long"
        self.face = "flat"

    def groom(self):
        return "I need frequent brushing because of my long coat"



class SiameseCat:
    def __init__(self):
        self.eyes = "blue"
        self.color_pattern = "point"

    def socialize(self):
        return "I love people pet me"



class HimalayanCat(PersianCat, SiameseCat):
    def __init__(self):
        PersianCat.__init__(self)
        SiameseCat.__init__(self)


himalayan_cat = HimalayanCat()

print(f"\nHello, I'm an Himalayan cat with {himalayan_cat.coat} coat, {himalayan_cat.face} face, {himalayan_cat.eyes} eyes, and a {himalayan_cat.color_pattern} color pattern.")
print(f"Also, {himalayan_cat.groom()}, and {himalayan_cat.socialize()}")