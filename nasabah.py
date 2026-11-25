# nasabah.py
# SUPERCLASS: Nasabah
# Menyimpan data umum nasabah asuransi. Semua atribut bersifat private
# (diawali dua underscore) dan diakses lewat getter / setter.


class Nasabah:
    # Constructor berparameter: dipanggil saat objek Nasabah dibuat
    def __init__(self, id_nasabah, nama, umur, status_aktif=True):
        self.__id_nasabah = id_nasabah      # atribut private 1
        self.__nama = nama                  # atribut private 2
        self.__umur = umur                  # atribut private 3
        self.__status_aktif = status_aktif  # atribut private 4

    # ---------- GETTER (menjaga enkapsulasi) ----------
    def get_id(self):
        return self.__id_nasabah

    def get_nama(self):
        return self.__nama

    def get_umur(self):
        return self.__umur

    def is_aktif(self):
        return self.__status_aktif

    # ---------- SETTER dengan validasi ----------
    def set_nama(self, nama_baru):
        if nama_baru.strip() == "":
            raise ValueError("Nama tidak boleh kosong.")
        self.__nama = nama_baru.strip()

    def set_umur(self, umur_baru):
        if umur_baru <= 0 or umur_baru > 100:
            raise ValueError("Umur harus antara 1 - 100.")
        self.__umur = umur_baru

    # ---------- METHOD TAMBAHAN ----------
    def aktifkan(self):
        # Mengubah status nasabah menjadi aktif
        self.__status_aktif = True

    def nonaktifkan(self):
        # Mengubah status nasabah menjadi nonaktif
        self.__status_aktif = False

    def get_jenis(self):
        # Dioverride oleh subclass
        return "Umum"

    def hitung_premi(self):
        # Premi dasar per bulan: Rp100.000 + Rp25.000 untuk setiap 10 tahun umur
        return 100000 + (self.__umur // 10) * 25000

    def cek_kelayakan(self):
        # Nasabah layak jika aktif dan umur 17 - 65 tahun
        return self.__status_aktif and 17 <= self.__umur <= 65

    def tampilkan_info(self):
        status = "Aktif" if self.__status_aktif else "Nonaktif"
        print(f"ID       : {self.__id_nasabah}")
        print(f"Nama     : {self.__nama}")
        print(f"Umur     : {self.__umur} tahun")
        print(f"Jenis    : {self.get_jenis()}")
        print(f"Status   : {status}")
