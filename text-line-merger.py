# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import filedialog

def gabungkan_baris(nama_file_input, nama_file_output):
    """
    Membaca file teks, menggabungkan semua baris menjadi satu baris
    yang dipisahkan oleh spasi, dan menuliskannya ke file output.

    Args:
        nama_file_input (str): Path ke file input (.txt).
        nama_file_output (str): Path untuk menyimpan file output.
    """
    try:
        # Membuka dan membaca file input
        with open(nama_file_input, 'r', encoding='utf-8') as file_input:
            # Membaca semua baris ke dalam sebuah list
            baris = file_input.readlines()

            # Menghapus spasi kosong di awal/akhir setiap baris (termasuk newline character)
            # dan menyaring baris yang kosong.
            baris_bersih = [b.strip() for b in baris if b.strip()]

            # Menggabungkan semua elemen dalam list menjadi satu string tunggal
            # dengan pemisah spasi.
            satu_baris = ' '.join(baris_bersih)

        # Membuka dan menulis hasil ke file output
        with open(nama_file_output, 'w', encoding='utf-8') as file_output:
            file_output.write(satu_baris)

        print(f"✅ Berhasil! File '{nama_file_input}' telah diproses dan disimpan sebagai '{nama_file_output}'.")

    except FileNotFoundError:
        print(f"❌ Gagal: File input '{nama_file_input}' tidak ditemukan.")
    except Exception as e:
        print(f"❌ Terjadi kesalahan: {e}")

# --- Cara Penggunaan ---
if __name__ == "__main__":
    # Membuat root window untuk Tkinter
    root = tk.Tk()
    root.withdraw() # Sembunyikan window utama karena kita hanya butuh dialognya

    # 1. Membuka dialog untuk memilih file input
    print("Silakan pilih file input (.txt) yang ingin diproses...")
    file_input = filedialog.askopenfilename(
        title="Pilih file input",
        filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
    )

    # 2. Jika pengguna memilih file, lanjutkan untuk memilih lokasi output
    if file_input:
        print(f"File input dipilih: {file_input}")
        print("Sekarang, pilih lokasi untuk menyimpan file hasil...")
        
        # Membuka dialog untuk menyimpan file output
        file_output = filedialog.asksaveasfilename(
            title="Simpan file sebagai...",
            defaultextension=".txt",
            filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
        )

        # 3. Jika pengguna menentukan lokasi penyimpanan, jalankan fungsi utama
        if file_output:
            print(f"File output akan disimpan di: {file_output}")
            gabungkan_baris(file_input, file_output)
        else:
            print("❌ Proses dibatalkan: Tidak ada lokasi penyimpanan yang dipilih.")
    else:
        print("❌ Proses dibatalkan: Tidak ada file input yang dipilih.")
