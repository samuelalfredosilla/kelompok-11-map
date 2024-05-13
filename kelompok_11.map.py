class Peta:
    def __init__(self):
        self.ListKota = {}
    
    def printPeta(self):
        for kota in self.ListKota:
            print(kota, ":",self.ListKota[kota])
            for neighbor, distance in self.ListKota[kota].items():
                print("   -->", neighbor, ":", distance)
        
    def tambahkanKota(self,kota):
        if kota not in self.ListKota:
            self.ListKota[kota] = {}
            return True
        return False
    
    def hapusKota(self,kotaDihapus):
        #cek apakah kota yang ingin dihapus ada di list
        if kotaDihapus in self.ListKota:
        #iterasi setiap kotalain untuk hapus kotadihapus
            for kotalain in self.ListKota:
                #cek apakah kota yang ingin dihapus ada jalannya ke kotalain
                if kotaDihapus in self.ListKota[kotalain]:
                    del self.ListKota[kotalain][kotaDihapus]
            del self.ListKota[kotaDihapus]
            return True
        return False
    
    def tambahkanJalan(self,kota1,kota2, jarak):
        if kota1 in self.ListKota and kota2 in self.ListKota:
            #masukkan kota 1 di list kota2
            self.ListKota[kota2] [kota1] = jarak
            #masukkan kota 2 di list kota1
            self.ListKota[kota1] [kota2] = jarak
            return True
        return False
    
    def hapusJalan(self,kota1,kota2):
        if kota1 in self.ListKota and kota2 in self.ListKota:
            #hapus kota 1 di list kota2
            self.ListKota[kota2].remove(kota1)
            #hapus kota 2 di list kota1
            self.ListKota[kota1].remove(kota2)
            return True
        return False
    
    def djikstra (self, source):
        
        #buat sebuah map yang melacak dari setiap kota ke source
        distance = {}
        for city in self.ListKota:
            distance[city] = float("inf")
        #tentukan jarak ke source = 0
        distance[source] = 0
        #buat sebuah sptSet
        
        unvisited_cities = []
        for city in self.ListKota:
            unvisited_cities.append(city)
        
        #buat perulangan selama unvisited cities masih ada isinya
        while unvisited_cities:
            #buat variable jarak minimum
            min_distance = float("inf")
            #buat variable kota terdekat
            closest_city = None
            
            #cari kota terdekat dengan jarak minimum
            for city in unvisited_cities:
                #jika jarak kota lebih kecil dari pada min distance
                if distance[city] < min_distance:
                #maka closest city dirubah ke kota tersebut
                    min_distance = distance[city]
                    closest_city = city
            
            #hapus vertex u dari unvisited        
            unvisited_cities.remove(closest_city)
            
            #perbarui nilai jarak dari semua vertex yang berdekatan
            for neighbor, jarak in self.ListKota[closest_city].items():
                #jika jarak kota terdekat + weight lebih kecil dari pada jarak di distance, maka ubah nilai distances
                jarakNeighbor = distance[closest_city] + jarak
                if jarakNeighbor < distance[neighbor]:
                    distance[neighbor] = jarakNeighbor
        return distance
        

petaJateng = Peta()
petaJateng.tambahkanKota("Surakarta")
petaJateng.tambahkanKota("Klaten")
petaJateng.tambahkanKota("Semarang")
petaJateng.tambahkanKota("Boyolali")
petaJateng.tambahkanKota("Magelang")
petaJateng.tambahkanKota("Temanggung")
petaJateng.tambahkanKota("Wonosobo")
petaJateng.tambahkanKota("Sukoharjo")
petaJateng.tambahkanKota("Karanganyar")
petaJateng.tambahkanKota("Purwodadi")
petaJateng.tambahkanKota("Wonogiri")
petaJateng.tambahkanKota("Sukoredjo")
petaJateng.tambahkanKota("Kebumen")
petaJateng.tambahkanKota("Purworejo")
petaJateng.tambahkanKota("Salatiga")
petaJateng.tambahkanJalan("Surakarta","Klaten", 34)
petaJateng.tambahkanJalan("Klaten","Semarang", 109)
petaJateng.tambahkanJalan("Semarang","Boyolali", 83)
petaJateng.tambahkanJalan("Boyolali","Magelang", 72)
petaJateng.tambahkanJalan("Magelang","Temanggung", 23)
petaJateng.tambahkanJalan("Temanggung","Wonosobo", 39)
petaJateng.tambahkanJalan("Wonosobo","Sukoharjo", 146)
petaJateng.tambahkanJalan("Sukoharjo","Karanganyar", 27)
petaJateng.tambahkanJalan("Karanganyar","Purwodadi", 73)
petaJateng.tambahkanJalan("Purwodadi","Wonogiri", 104)
petaJateng.tambahkanJalan("Wonogiri","Sukoredjo", 168)
petaJateng.tambahkanJalan("Sukoredjo","Kebumen", 130)
petaJateng.tambahkanJalan("Kebumen","Purworejo", 42)
petaJateng.tambahkanJalan("Purworejo","Salatiga", 87)
petaJateng.tambahkanJalan("Salatiga","Surakarta", 53)
petaJateng.tambahkanJalan("Klaten","Boyolali", 43)
petaJateng.tambahkanJalan("Semarang","Magelang", 77)
petaJateng.tambahkanJalan("Boyolali","Temanggung", 76)
petaJateng.tambahkanJalan("Magelang","Wonosobo", 62)
petaJateng.tambahkanJalan("Temanggung","Sukoharjo", 106)
petaJateng.tambahkanJalan("Wonosobo","Karanganyar", 154)
petaJateng.tambahkanJalan("Sukoharjo","Purwodadi", 80)
petaJateng.tambahkanJalan("Karanganyar","Wonogiri", 35)
petaJateng.tambahkanJalan("Purwodadi","Sukoredjo", 117)
petaJateng.tambahkanJalan("Wonogiri","Kebumen", 185)
petaJateng.tambahkanJalan("Sukoredjo","Purworejo", 92)
petaJateng.tambahkanJalan("Kebumen","Salatiga", 129)
petaJateng.tambahkanJalan("Purworejo","Surakarta", 120)
petaJateng.tambahkanJalan("Salatiga","Boyolali", 35)
petaJateng.tambahkanJalan("Klaten","Magelang", 73)
petaJateng.tambahkanJalan("Boyolali","Surakarta", 28)

print('------------------------------')
petaJateng.djikstra("Surakarta")
JarakSemuaKotaDariSurakarta = petaJateng.djikstra("Surakarta")
print("jarak dari Surakarta adalah :")
for city, distance in JarakSemuaKotaDariSurakarta.items():
    print(city, "adalah", distance, "KM")
