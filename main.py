# main.py
# MAIN FILE: menu CLI Aplikasi Asuransi Nasabah

from nasabah import Nasabah
from nasabah_kesehatan import NasabahKesehatan
from nasabah_jiwa import NasabahJiwa
from polis import Polis

# Penyimpanan data sementara (in-memory)
daftar_nasabah = []
daftar_polis = []


# ---------- FUNGSI BANTU ----------
def input_angka(pesan):
    # Meminta input angka, diulang sampai valid
    while True:
        try:
            return int(input(pesan))
        except ValueError:
            print("Input harus berupa angka!")


def cari_nasabah_by_id(id_nasabah):
    # strip() membuang spasi di awal/akhir supaya input lebih toleran
    id_nasabah = id_nasabah.strip().lower()
    for n in daftar_nasabah:
        if n.get_id().lower() == id_nasabah:
            return n
    return None


def cari_polis_by_nomor(nomor):
    nomor = nomor.strip().lower()
    for p in daftar_polis:
        if p.get_nomor_polis().lower() == nomor:
            return p
    return None


# ---------- 1. TAMBAH DATA ----------
def tambah_nasabah():
    print("--- Tambah Nasabah ---")
    print("1. Asuransi Kesehatan")
    print("2. Asuransi Jiwa")
    jenis = input("Pilih jenis: ")
    id_baru = f"N{len(daftar_nasabah) + 1:03d}"  # ID otomatis: N001, N002, ...
    nama = input("Nama   : ")
    umur = input_angka("Umur   : ")

    if jenis == "1":
        kelas = input_angka("Kelas rawat (1/2/3): ")
        riwayat = input("Riwayat penyakit (ketik 'tidak ada' jika tidak ada): ")
        tanggungan = input_angka("Jumlah tanggungan: ")
        nasabah = NasabahKesehatan(id_baru, nama, umur, kelas, riwayat, tanggungan)
    elif jenis == "2":
        up = input_angka("Uang pertanggungan (Rp): ")
        # Ulangi sampai user mengetik y atau n
        jawab = ""
        while jawab not in ("y", "n"):
            jawab = input("Pekerjaan berisiko? (y/n): ").strip().lower()
            if jawab not in ("y", "n"):
                print("Ketik y atau n saja!")
        berisiko = (jawab == "y")
        waris = input_angka("Jumlah ahli waris: ")
        nasabah = NasabahJiwa(id_baru, nama, umur, up, berisiko, waris)
    else:
        print("Pilihan tidak valid.")
        return

    daftar_nasabah.append(nasabah)
    print(f"Nasabah berhasil ditambahkan dengan ID {id_baru}.")


def tambah_polis():
    print("--- Tambah Polis ---")
    nasabah = cari_nasabah_by_id(input("ID Nasabah pemilik polis: "))
    if nasabah is None:
        print("Nasabah tidak ditemukan.")
        return
    # Validasi kelayakan memakai method cek_kelayakan (polimorfisme)
    if not nasabah.cek_kelayakan():
        print("Nasabah tidak layak mendapatkan polis (nonaktif / tidak memenuhi syarat).")
        return
    durasi = input_angka("Durasi polis (tahun): ")
    nomor = f"P{len(daftar_polis) + 1:03d}"
    daftar_polis.append(Polis(nomor, nasabah, durasi))
    print(f"Polis {nomor} berhasil dibuat untuk {nasabah.get_nama()}.")


# ---------- 2. TAMPILKAN DATA ----------
def tampilkan_data():
    print("=== DATA NASABAH ===")
    if not daftar_nasabah:
        print("(belum ada data)")
    for n in daftar_nasabah:
        n.tampilkan_info()
        print("-" * 30)
    print("=== DATA POLIS ===")
    if not daftar_polis:
        print("(belum ada data)")
    for p in daftar_polis:
        p.tampilkan_info()
        print("-" * 30)


# ---------- 3. CARI DATA ----------
def cari_data():
    print("--- Cari Data ---")
    kata = input("Masukkan ID atau nama nasabah: ").strip().lower()
    hasil = [n for n in daftar_nasabah
             if kata in n.get_id().lower() or kata in n.get_nama().lower()]
    if not hasil:
        print("Data tidak ditemukan.")
        return
    for n in hasil:
        n.tampilkan_info()
        # Tampilkan polis milik nasabah tersebut (relasi)
        polis_milik = [p.get_nomor_polis() for p in daftar_polis if p.get_nasabah() is n]
        print(f"Polis    : {', '.join(polis_milik) if polis_milik else '-'}")
        print("-" * 30)


# ---------- 4. UBAH DATA ----------
def ubah_data():
    print("--- Ubah Data ---")
    print("1. Ubah data nasabah")
    print("2. Perpanjang polis")
    pilih = input("Pilih: ")
    try:
        if pilih == "1":
            n = cari_nasabah_by_id(input("ID Nasabah: "))
            if n is None:
                print("Nasabah tidak ditemukan.")
                return
            print("1. Nama")
            print("2. Umur")
            print("3. Aktifkan/Nonaktifkan")
            print("4. Data khusus jenis asuransi")
            f = input("Ubah apa? ")
            if f == "1":
                n.set_nama(input("Nama baru: "))
            elif f == "2":
                n.set_umur(input_angka("Umur baru: "))
            elif f == "3":
                if n.is_aktif():
                    n.nonaktifkan()
                else:
                    n.aktifkan()
            elif f == "4":
                if isinstance(n, NasabahKesehatan):
                    n.set_kelas_rawat(input_angka("Kelas rawat baru (1/2/3): "))
                elif isinstance(n, NasabahJiwa):
                    n.set_uang_pertanggungan(input_angka("Uang pertanggungan baru: "))
            else:
                print("Pilihan tidak valid.")
                return
            print("Data nasabah berhasil diubah.")
        elif pilih == "2":
            p = cari_polis_by_nomor(input("Nomor Polis: "))
            if p is None:
                print("Polis tidak ditemukan.")
                return
            p.perpanjang(input_angka("Tambah durasi (tahun): "))
            print("Polis berhasil diperpanjang.")
        else:
            print("Pilihan tidak valid.")
    except ValueError as e:
        # Error validasi dari setter
        print(f"Gagal: {e}")


# ---------- 5. CEK STATUS ----------
def cek_status():
    print("--- Cek Status ---")
    p = cari_polis_by_nomor(input("Nomor Polis: "))
    if p is None:
        print("Polis tidak ditemukan.")
        return
    n = p.get_nasabah()
    print(f"Status polis   : {p.cek_status()}")
    print(f"Status nasabah : {'Aktif' if n.is_aktif() else 'Nonaktif'}")
    print(f"Kelayakan      : {'Layak' if n.cek_kelayakan() else 'Tidak layak'}")


# ---------- DATA CONTOH (tidak dipakai, aktifkan kalau perlu) ----------
def isi_data_contoh():
    daftar_nasabah.append(NasabahKesehatan("N001", "Budi Santoso", 30, 2, "tidak ada", 3))
    daftar_nasabah.append(NasabahJiwa("N002", "Siti Aminah", 40, 500000000, False, 2))
    daftar_polis.append(Polis("P001", daftar_nasabah[0], 2))


# ---------- MENU UTAMA ----------
def main():
    # isi_data_contoh()   # dinonaktifkan: daftar mulai kosong
    while True:
        print("===== ASURANSI NASABAH =====")
        print("1. Tambah Nasabah")
        print("2. Tambah Polis")
        print("3. Tampilkan Data")
        print("4. Cari Data")
        print("5. Ubah Data")
        print("6. Cek Status")
        print("0. Keluar")
        pilih = input("Pilih menu: ")

        if pilih == "1":
            tambah_nasabah()
        elif pilih == "2":
            tambah_polis()
        elif pilih == "3":
            tampilkan_data()
        elif pilih == "4":
            cari_data()
        elif pilih == "5":
            ubah_data()
        elif pilih == "6":
            cek_status()
        elif pilih == "0":
            print("Terima kasih!")
            break
        else:
            print("Menu tidak valid.")


if __name__ == "__main__":
    main()
