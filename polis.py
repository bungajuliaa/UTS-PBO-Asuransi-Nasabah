# polis.py
# CLASS RELASI (Association): Polis dimiliki oleh SATU Nasabah.
# Atribut __nasabah menyimpan objek Nasabah (atau subclass-nya).

from datetime import date, timedelta


class Polis:
    def __init__(self, nomor_polis, nasabah, durasi_tahun, tanggal_mulai=None):
        self.__nomor_polis = nomor_polis
        self.__nasabah = nasabah                                # relasi ke 1 Nasabah
        self.__durasi_tahun = durasi_tahun
        self.__tanggal_mulai = tanggal_mulai or date.today()
        self.__dibatalkan = False

    # ---------- GETTER ----------
    def get_nomor_polis(self):
        return self.__nomor_polis

    def get_nasabah(self):
        return self.__nasabah

    def get_durasi_tahun(self):
        return self.__durasi_tahun

    def get_tanggal_mulai(self):
        return self.__tanggal_mulai

    # ---------- METHOD TAMBAHAN ----------
    def get_tanggal_berakhir(self):
        return self.__tanggal_mulai + timedelta(days=365 * self.__durasi_tahun)

    def hitung_total_premi(self):
        # Total premi = premi bulanan nasabah x 12 bulan x durasi
        return self.__nasabah.hitung_premi() * 12 * self.__durasi_tahun

    def cek_status(self):
        # Status ditentukan dari pembatalan dan tanggal berakhir
        if self.__dibatalkan:
            return "Dibatalkan"
        if date.today() > self.get_tanggal_berakhir():
            return "Kedaluwarsa"
        return "Aktif"

    def perpanjang(self, tambahan_tahun):
        if tambahan_tahun <= 0:
            raise ValueError("Tambahan durasi harus lebih dari 0.")
        self.__durasi_tahun += tambahan_tahun

    def batalkan(self):
        self.__dibatalkan = True

    def tampilkan_info(self):
        print(f"No. Polis : {self.__nomor_polis}")
        print(f"Pemilik   : {self.__nasabah.get_nama()} ({self.__nasabah.get_jenis()})")
        print(f"Mulai     : {self.__tanggal_mulai}")
        print(f"Berakhir  : {self.get_tanggal_berakhir()} ({self.__durasi_tahun} tahun)")
        print(f"Premi/bln : Rp{self.__nasabah.hitung_premi():,}")
        print(f"Total     : Rp{self.hitung_total_premi():,}")
        print(f"Status    : {self.cek_status()}")
