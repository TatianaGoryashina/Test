from smartphone import Smartphone

catalog = []
catalog.append(Smartphone("Apple", "iPhone 14", "+79876543210"))
catalog.append(Smartphone("Samsung", "Galaxy S22", "+79543210987"))
catalog.append(Smartphone("Xiaomi", "Mi 11", "+79123456789"))
catalog.append(Smartphone("Google", "Pixel 7", "+79998887766"))
catalog.append(Smartphone("OnePlus", "9 Pro", "+79012345678"))

for smartphone in catalog:
    print(smartphone)
