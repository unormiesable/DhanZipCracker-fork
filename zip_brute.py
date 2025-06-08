import zipfile
import os

def brute_force_zip(zip_path, wordlist_path):
    if not os.path.exists(zip_path):
        print(f"[!] ZIP file '{zip_path}' tidak ditemukan.")
        return

    if not os.path.exists(wordlist_path):
        print(f"[!] Wordlist file '{wordlist_path}' tidak ditemukan.")
        return

    try:
        with zipfile.ZipFile(zip_path, 'r') as zip_file:
            with open(wordlist_path, 'r', encoding='utf-8', errors='ignore') as wordlist:
                for line in wordlist:
                    password = line.strip()
                    try:
                        zip_file.extractall(pwd=bytes(password, 'utf-8'))
                        print(f"\n[✓] Password ditemukan: {password}")
                        return
                    except:
                        print(f"[-] Salah: {password}")
        print("\n[×] Password tidak ditemukan dalam wordlist.")
    except zipfile.BadZipFile:
        print("[!] File ZIP rusak atau tidak valid.")

def main():
    ascii_art = r"""
 _____  _   _    _    _   _ 
|  __ \| | | |  / \  | \ | |
| |  | | |_| | / _ \ |  \| |
| |__| |  _  |/ ___ \| |\  |
|_____/|_| |_/_/   \_\_| \_|
        D  H  A  N
"""
    print(ascii_art)
    print("=== ZIP Password Brute Forcer ===")

    zip_path = input("Masukkan path file ZIP target: ").strip()
    wordlist_path = input("Masukkan path file wordlist: ").strip()

    brute_force_zip(zip_path, wordlist_path)

if __name__ == "__main__":
    main()

