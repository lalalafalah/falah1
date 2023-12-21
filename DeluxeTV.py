import os
os.system("cls")

from d1.Television import Television
from SortedSet import SortedSet

class DeluxeTV(Television):
    def __init__(self):
        Television.__init__(self)
        self.favorites = []

    def addToFavorites(self):
        if self.powerOn and self.channel not in self.favorites:
            self.favorites.append(self.channel)

    def removeFromFavorites(self):
        if self.powerOn and self.channel in self.favorites:
            self.favorites.remove(self.channel)

    def jumpToFavorite(self):
        if self.powerOn and len(self.favorites)>0:
            closest = max(self.favorites)
            if closest <= self.channel:
                closest = min(self.favorites)
            else:
                for option in self.favorites:
                    if self.channel < option < closest:
                        closest = option
            self.setChannel(closest)
            return closest

#     def jumpToFavorite(self):
#         if self.powerOn and len(self.favorites)>0:
#             resultIndex = self.favorites.indexAfter(self.channel)
#             if resultIndex == len(self.favorites):
#                 result = self.favorites[0]
#             else:
#                 result = self.favorites[resultIndex]
#             self.setChannel(result)
#             return result
   
# # Membuat objek DeluxeTV
# deluxe_tv = DeluxeTV()

# # Menghidupkan TV
# deluxe_tv.togglePower()

# # Mengubah saluran
# deluxe_tv.setChannel(5)

# # Menambahkan beberapa saluran favorit
# deluxe_tv.addToFavorites()
# deluxe_tv.addToFavorites()
# deluxe_tv.addToFavorites()

# # Menghapus satu saluran favorit
# deluxe_tv.removeFromFavorites()

# # Melompat ke saluran favorit terdekat
# favorite_channel = deluxe_tv.jumpToFavorite()

# # Menampilkan status TV
# print(deluxe_tv)