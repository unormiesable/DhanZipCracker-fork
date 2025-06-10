import zipfile
import os
from colorama import Fore, Style, init

# Inisialisasi colorama
init(autoreset=True)

def brute_force_zip(zip_path, wordlist_path):
    if not os.path.exists(zip_path):
        print(f"{Fore.RED}[!] ZIP file '{zip_path}' tidak ditemukan.")
        return

    if not os.path.exists(wordlist_path):
        print(f"{Fore.RED}[!] Wordlist file '{wordlist_path}' tidak ditemukan.")
        return

    try:
        with zipfile.ZipFile(zip_path, 'r') as zip_file:
            with open(wordlist_path, 'r', encoding='utf-8', errors='ignore') as wordlist:
                print(f"\n{Fore.YELLOW}[*] Memulai brute force...\n")
                for line in wordlist:
                    password = line.strip()
                    try:
                        zip_file.extractall(pwd=bytes(password, 'utf-8'))
                        print(f"\n{Fore.GREEN}[✓] Password ditemukan: {Style.BRIGHT}{password}")
                        return
                    except:
                        print(f"{Fore.RED}[-] Salah: {password}")
        print(f"\n{Fore.RED}[×] Password tidak ditemukan dalam wordlist.")
    except zipfile.BadZipFile:
        print(f"{Fore.RED}[!] File ZIP rusak atau tidak valid.")

def main():
    ascii_art = f"""{Fore.CYAN}{Style.BRIGHT}
 _____  _   _    _    _   _ 
|  __ \| | | |  / \  | \ | |
| |  | | |_| | / _ \ |  \| |
| |__| |  _  |/ ___ \| |\  |
|_____/|_| |_/_/   \_\_| \_|
        D  H  A  N
"""
    print(ascii_art)
    print(f"{Fore.MAGENTA}=== ZIP Password Brute Forcer by Dhan ==={Style.RESET_ALL}\n")

    zip_path = input(f"{Fore.CYAN}[?] Masukkan path file .ZIP/.7z target: ").strip()
    wordlist_path = input(f"{Fore.CYAN}[?] Masukkan path file wordlist (Bisa Menggunakan Wordlist Milik Sendiri: ").strip()

    brute_force_zip(zip_path, wordlist_path)

if __name__ == "__main__":
    main()
