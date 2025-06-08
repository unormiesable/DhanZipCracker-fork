🔐 ZIP Password Brute Forcer - DHAN Tools

DHAN Tools adalah script Python minimalis untuk melakukan brute force terhadap file ZIP yang dilindungi password menggunakan wordlist. Cocok untuk simulasi CTF, pembelajaran keamanan, dan forensik.

===============================

FITUR

- Interaktif via terminal
- Tampilan bersih dan sederhana
- Hanya masih bisa cracking ZIP saja

===============================

STRUKTUR FOLDER

├── zip_brute_force_dhan.py

├── target.zip

└── wordlist.txt

===============================

CARA MENJALANKAN

Clone repository:
git clone https://github.com/username/zip-brute-dhan.git

Jalankan script:
python zip_brute.py

Masukkan path file saat diminta:
Path file ZIP target : target.zip (SESUAIKAN DENGAN TARGET ZIP YANG ADA PADA FOLDER)
Path file wordlist : wordlist.txt (Atau bisa menggunakan worlists yang lain)

===============================

CONTOH ISI WORLIST DISINI

123456
admin
admin123
letmein
password

===============================

SEDIKI TIPS MEMBUAT ZIP BERPASSWORD

Di Linux/macOS:
echo "Flag{rahasia}" > secret.txt
zip -e target.zip secret.txt
(masukkan password: admin123)

===============================

DISCLAIMER

Tools ini hanya untuk pembelajaran, analisis forensik, dan simulasi keamanan.
Jangan digunakan untuk tujuan ilegal. Segala penyalahgunaan di luar tanggung jawab pembuat.
