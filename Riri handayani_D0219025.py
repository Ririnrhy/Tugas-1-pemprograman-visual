class karyawan:
    '''Dasar kelas untuk semua karyawan'''
    jumlah_karyawan = 0
    
    def _inist_(self, nama, gaji):
         self.nama = nama
         self.gaji = gaji
         karyawan.jumlah_karyawan += 1
         def tampilkan_jumlah(self):
            print("Total karyawan :",karyawan.jumlah_karyawan)
            def tampilkan_profil(self):
                print("nama :", self.nama)
                print("gaji :", self.gaji)
                karyawan1 = karyawan("ririn",2000000)
                karyawan2 = karyawan("aris",3000000)
                karyawan1.tampilkan_profil()
                karyawan2.tampilkan_profil()
                print("total karyawan :", karyawan.jumlah_karyawan)
