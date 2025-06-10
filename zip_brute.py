import zipfile
import py7zr
import os
from colorama import Fore, Style, init

init(autoreset=True)

def brute_force_zip(zip_path, wordlist_path):
    try:
        with zipfile.ZipFile(zip_path, 'r') as zip_file:
            with open(wordlist_path, 'r', encoding='utf-8', errors='ignore') as wordlist:
                print(f"\n{Fore.YELLOW}[*] Memulai brute force ZIP...\n")
                for line in wordlist:
                    password = line.strip()
                    try:
                        zip_file.extractall(pwd=bytes(password, 'utf-8'))
                        print(f"\n{Fore.GREEN}[✓] Password ZIP ditemukan: {Style.BRIGHT}{password}")
                        return
                    except:
                        print(f"{Fore.RED}[-] ZIP Salah: {password}")
        print(f"\n{Fore.RED}[×] Password ZIP tidak ditemukan dalam wordlist.")
    except zipfile.BadZipFile:
        print(f"{Fore.RED}[!] File ZIP rusak atau tidak valid.")

def brute_force_7z(sevenz_path, wordlist_path):
    try:
        with open(wordlist_path, 'r', encoding='utf-8', errors='ignore') as wordlist:
            print(f"\n{Fore.YELLOW}[*] Memulai brute force 7z...\n")
            for line in wordlist:
                password = line.strip()
                try:
                    with py7zr.SevenZipFile(sevenz_path, mode='r', password=password) as archive:
                        archive.extractall()
                        print(f"\n{Fore.GREEN}[✓] Password 7z ditemukan: {Style.BRIGHT}{password}")
                        return
                except:
                    print(f"{Fore.RED}[-] 7z Salah: {password}")
        print(f"\n{Fore.RED}[×] Password 7z tidak ditemukan dalam wordlist.")
    except FileNotFoundError:
        print(f"{Fore.RED}[!] File 7z tidak ditemukan atau rusak.")

def main():
    ascii_art = fr"""{Fore.CYAN}{Style.BRIGHT}
 _____  _   _    _    _   _
|  __ \| | | |  / \  | \ | |
| |  | | |_| | / _ \ |  \| |
| |__| |  _  |/ ___ \| |\  |
|_____/|_| |_/_/   \_\_| \_|
        D  H  A  N
"""

    print(ascii_art)
    print(f"{Fore.MAGENTA}=== ZIP & 7z Password Brute Forcer by Dhan ==={Style.RESET_ALL}\n")

    file_path = input(f"{Fore.CYAN}[?] Masukkan path file .ZIP/.7z target: ").strip()
    wordlist_path = input(f"{Fore.CYAN}[?] Masukkan path file wordlist: ").strip()

    if not os.path.exists(file_path):
        print(f"{Fore.RED}[!] File target tidak ditemukan.")
        return

    if not os.path.exists(wordlist_path):
        print(f"{Fore.RED}[!] File wordlist tidak ditemukan.")
        return

    if file_path.lower().endswith(".zip"):
        brute_force_zip(file_path, wordlist_path)
    elif file_path.lower().endswith(".7z"):
        brute_force_7z(file_path, wordlist_path)
    else:
        print(f"{Fore.RED}[!] Format file tidak didukung. Hanya .zip dan .7z")

if __name__ == "__main__":
    main()
