# nasabah_kesehatan.py
# SUBCLASS 1: NasabahKesehatan (extends Nasabah)

from nasabah import Nasabah


class NasabahKesehatan(Nasabah):
    def __init__(self, id_nasabah, nama, umur, kelas_rawat, riwayat_penyakit, jumlah_tanggungan):
        # Memanggil constructor superclass
        super().__init__(id_nasabah, nama, umur)
        self.__kelas_rawat = kelas_rawat              # 1, 2, atau 3
        self.__riwayat_penyakit = riwayat_penyakit    # "tidak ada" jika sehat
        self.__jumlah_tanggungan = jumlah_tanggungan  # jumlah anggota keluarga ditanggung

    # ---------- GETTER ----------
    def get_kelas_rawat(self):
        return self.__kelas_rawat

    def get_riwayat_penyakit(self):
        return self.__riwayat_penyakit

    def get_jumlah_tanggungan(self):
        return self.__jumlah_tanggungan

    # ---------- SETTER ----------
    def set_kelas_rawat(self, kelas_baru):
        if kelas_baru not in (1, 2, 3):
            raise ValueError("Kelas rawat harus 1, 2, atau 3.")
        self.__kelas_rawat = kelas_baru

    # ---------- OVERRIDE method superclass ----------
    def get_jenis(self):
        return "Asuransi Kesehatan"

    def hitung_premi(self):
        # Premi dasar dari superclass + tambahan khusus asuransi kesehatan
        tambahan_kelas = {1: 300000, 2: 200000, 3: 100000}[self.__kelas_rawat]
        tambahan_tanggungan = self.__jumlah_tanggungan * 75000
        tambahan_penyakit = 0 if self.__riwayat_penyakit.lower() == "tidak ada" else 150000
        return super().hitung_premi() + tambahan_kelas + tambahan_tanggungan + tambahan_penyakit

    def cek_kelayakan(self):
        # Selain syarat umum, tanggungan maksimal 5 orang
        return super().cek_kelayakan() and self.__jumlah_tanggungan <= 5

    def tampilkan_info(self):
        super().tampilkan_info()
        print(f"Kelas Rawat : {self.__kelas_rawat}")
        print(f"Riwayat Penyakit : {self.__riwayat_penyakit}")
        print(f"Tanggungan  : {self.__jumlah_tanggungan} orang")
