# nasabah_jiwa.py
# SUBCLASS 2: NasabahJiwa (extends Nasabah)

from nasabah import Nasabah


class NasabahJiwa(Nasabah):
    def __init__(self, id_nasabah, nama, umur, uang_pertanggungan, pekerjaan_berisiko, jumlah_ahli_waris):
        # Memanggil constructor superclass
        super().__init__(id_nasabah, nama, umur)
        self.__uang_pertanggungan = uang_pertanggungan    # nilai santunan (Rp)
        self.__pekerjaan_berisiko = pekerjaan_berisiko    # True / False
        self.__jumlah_ahli_waris = jumlah_ahli_waris

    # ---------- GETTER ----------
    def get_uang_pertanggungan(self):
        return self.__uang_pertanggungan

    def is_pekerjaan_berisiko(self):
        return self.__pekerjaan_berisiko

    def get_jumlah_ahli_waris(self):
        return self.__jumlah_ahli_waris

    # ---------- SETTER ----------
    def set_uang_pertanggungan(self, nilai_baru):
        if nilai_baru <= 0:
            raise ValueError("Uang pertanggungan harus lebih dari 0.")
        self.__uang_pertanggungan = nilai_baru

    # ---------- OVERRIDE method superclass ----------
    def get_jenis(self):
        return "Asuransi Jiwa"

    def hitung_premi(self):
        # Premi dasar + 0,05% dari uang pertanggungan + tambahan jika pekerjaan berisiko
        tambahan_up = int(self.__uang_pertanggungan * 0.0005)
        tambahan_risiko = 200000 if self.__pekerjaan_berisiko else 0
        return super().hitung_premi() + tambahan_up + tambahan_risiko

    def cek_kelayakan(self):
        # Selain syarat umum, umur maksimal 60 tahun dan minimal 1 ahli waris
        return super().cek_kelayakan() and self.get_umur() <= 60 and self.__jumlah_ahli_waris >= 1

    def tampilkan_info(self):
        super().tampilkan_info()
        print(f"Uang Pertanggungan : Rp{self.__uang_pertanggungan:,}")
        print(f"Pekerjaan Berisiko : {'Ya' if self.__pekerjaan_berisiko else 'Tidak'}")
        print(f"Ahli Waris : {self.__jumlah_ahli_waris} orang")
