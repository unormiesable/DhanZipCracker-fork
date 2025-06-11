# 🔐 ZIP Password Brute Forcer - DHAN Tools

DHAN Tools adalah script Python minimalis untuk melakukan brute force terhadap file ZIP yang dilindungi password menggunakan wordlist. Cocok untuk simulasi CTF, pembelajaran keamanan, dan forensik.

** Ini merupakan fork dari repository asli : https://github.com/Ardhandms/DhanZipCracker.git

## FITUR

- GUI Sederhana
- Hanya masih bisa cracking ZIP & 7z saja


## CARA MENJALANKAN

<pre>
Clone repository :
<code>git clone https://github.com/unormiesable/DhanZipCracker-fork.git</code>
<code>cd DhanZipCracker-fork</code>


Buat Virtual Environment :
<code>python -m venv virtual</code>


Gunakan Virtual Environment :
- Windows :
    - CMD           : <code>.\virtual\Scripts\activate.bat</code>
    - PowerShell    : <code>.\virtual\Scripts\Activate.ps1</code>
    - Git Bash      : <code>source virtual/Scripts/activate</code>

- Linux : <code>source virtual/bin/activate</code>


Install Modules :
<code>pip install -r requirements.txt</code>


Run Program :
<code>python main.py</code>
</pre>


Masukkan path file saat diminta:
Path file ZIP target : target.zip (SESUAIKAN DENGAN TARGET ZIP YANG ADA PADA FOLDER)
Path file wordlist : wordlist.txt (Atau bisa menggunakan worlists yang lain)


## DISCLAIMER

Tools ini hanya untuk pembelajaran, analisis forensik, dan simulasi keamanan.
Jangan digunakan untuk tujuan ilegal. Segala penyalahgunaan di luar tanggung jawab pembuat.
