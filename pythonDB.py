import sqlite3
from tkinter import Tk, Label, Entry, Button

# Membuat koneksi dan cursor SQLite
conn = sqlite3.connect('nilai_siswa.db')
cursor = conn.cursor()

# Membuat tabel nilai_siswa jika belum ada
cursor.execute('''
    CREATE TABLE IF NOT EXISTS nilai_siswa (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nama_siswa TEXT,
        biologi INTEGER,
        fisika INTEGER,
        inggris INTEGER,
        prediksi_fakultas TEXT
    )
''')
conn.commit()

# Fungsi untuk menentukan prediksi fakultas
def prediksi_fakultas(biologi, fisika, inggris):
    if biologi > fisika and biologi > inggris:
        return 'Kedokteran'
    elif fisika > biologi and fisika > inggris:
        return 'Teknik'
    elif inggris > biologi and inggris > fisika:
        return 'Bahasa'
    else:
        return 'Tidak dapat memprediksi'

# Fungsi untuk menangani tombol submit
def submit_nilai():
    nama_siswa = entry_nama.get()
    nilai_biologi = int(entry_biologi.get())
    nilai_fisika = int(entry_fisika.get())
    nilai_inggris = int(entry_inggris.get())

    prediksi = prediksi_fakultas(nilai_biologi, nilai_fisika, nilai_inggris)

    # Memasukkan data ke database
    cursor.execute('''
        INSERT INTO nilai_siswa (nama_siswa, biologi, fisika, inggris, prediksi_fakultas)
        VALUES (?, ?, ?, ?, ?)
    ''', (nama_siswa, nilai_biologi, nilai_fisika, nilai_inggris, prediksi))
    conn.commit()

    # Menampilkan hasil prediksi
    label_hasil.config(text=f'Hasil prediksi fakultas: {prediksi}')

# Membuat GUI dengan Tkinter
root = Tk()
root.title('Aplikasi Prediksi Fakultas')

label_nama = Label(root, text='Nama Siswa:')
label_nama.grid(row=0, column=0, padx=10, pady=10)
entry_nama = Entry(root)
entry_nama.grid(row=0, column=1, padx=10, pady=10)

label_biologi = Label(root, text='Nilai Biologi:')
label_biologi.grid(row=1, column=0, padx=10, pady=10)
entry_biologi = Entry(root)
entry_biologi.grid(row=1, column=1, padx=10, pady=10)

label_fisika = Label(root, text='Nilai Fisika:')
label_fisika.grid(row=2, column=0, padx=10, pady=10)
entry_fisika = Entry(root)
entry_fisika.grid(row=2, column=1, padx=10, pady=10)

label_inggris = Label(root, text='Nilai Inggris:')
label_inggris.grid(row=3, column=0, padx=10, pady=10)
entry_inggris = Entry(root)
entry_inggris.grid(row=3, column=1, padx=10, pady=10)

button_submit = Button(root, text='Submit Nilai', command=submit_nilai)
button_submit.grid(row=4, column=0, columnspan=2, pady=10)

label_hasil = Label(root, text='')
label_hasil.grid(row=5, column=0, columnspan=2, pady=10)

root.mainloop()

# Menutup koneksi SQLite setelah GUI ditutup
conn.clos()
