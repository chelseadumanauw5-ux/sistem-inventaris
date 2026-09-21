# Program Presensi Mahasiswa dengan OOP Python
# Chelsea Morenofa Dumanauw - 250211060077

class Mahasiswa:
    def __init__(self, nama, nim):
        self.nama = nama
        self.nim = nim

class Presensi:
    def __init__(self):
        self.__daftar_hadir = []  # private list

    def tambah_mahasiswa(self, mahasiswa):
        if isinstance(mahasiswa, Mahasiswa):
            self.__daftar_hadir.append(mahasiswa)
            print(f"[{mahasiswa.nim}] {mahasiswa.nama} berhasil ditambahkan ke presensi.")
        else:
            print("Error: Input harus berupa objek Mahasiswa!")

    def tampilkan_presensi(self):
        print("\n📋 Daftar Mahasiswa Hadir:")
        if not self.__daftar_hadir:
            print("- Belum ada mahasiswa yang hadir.")
        for mhs in self.__daftar_hadir:
            print(f"- {mhs.nama} ({mhs.nim})")

    def __hitung_total_hadir(self):  # private method
        return len(self.__daftar_hadir)

    def total_hadir(self):
        print(f"\n👥 Total Mahasiswa Hadir: {self.__hitung_total_hadir()}")


# --- Sesi Pengujian (Agar program memunculkan output) ---
if __name__ == "__main__":
    # 1. Membuat objek sistem presensi
    sistem_presensi = Presensi()

    # 2. Membuat 5 objek Mahasiswa
    mhs1 = Mahasiswa("Chelsea Morenofa Dumanauw", "250211060077")
    mhs2 = Mahasiswa("Jeon Jungkook", "250211060080")
    mhs3 = Mahasiswa("Kim Taehyung", "250211060081")
    mhs4 = Mahasiswa("Park Jimin", "250211060082")
    mhs5 = Mahasiswa("Songkang", "250211060083")
    
    print("--- Proses Presensi ---")
    # 3. Menambahkan ke-5 mahasiswa ke daftar presensi
    sistem_presensi.tambah_mahasiswa(mhs1)
    sistem_presensi.tambah_mahasiswa(mhs2)
    sistem_presensi.tambah_mahasiswa(mhs3)
    sistem_presensi.tambah_mahasiswa(mhs4)
    sistem_presensi.tambah_mahasiswa(mhs5)
    
    # 4. Menguji input error (Memasukkan tipe data String, bukan objek Mahasiswa)
    print("\n--- Uji Validasi Input ---")
    sistem_presensi.tambah_mahasiswa("Kim Taehyung")

    # 5. Menampilkan hasil
    sistem_presensi.tampilkan_presensi()
    sistem_presensi.total_hadir()