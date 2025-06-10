import zipfile
import py7zr
import os
from colorama import Fore, Style, init

from gui import GUI

class Main:
    def __init__(self):
        init(autoreset=True)
        self.gui = GUI()

    def brute_force_zip(self, zip_path, wordlist_path):
        try:
            with zipfile.ZipFile(zip_path, 'r') as zip_file:
                with open(wordlist_path, 'r', encoding='utf-8', errors='ignore') as wordlist:
                    print(f"\n{Fore.YELLOW}[*] Memulai brute force ZIP...\n")
                    for line in wordlist:
                        password = line.strip()
                        try:
                            zip_file.extractall(pwd=bytes(password, 'utf-8'))
                            print(f"\n{Fore.GREEN}[✓] Password ZIP ditemukan: {Style.BRIGHT}{password}")
                            return True
                        except:
                            print(f"{Fore.RED}[-] ZIP Salah: {password}")
            print(f"\n{Fore.RED}[×] Password ZIP tidak ditemukan dalam wordlist.")
            return False
        except zipfile.BadZipFile:
            print(f"{Fore.RED}[!] File ZIP rusak atau tidak valid.")
            return False
        except FileNotFoundError:
            print(f"{Fore.RED}[!] File ZIP atau wordlist tidak ditemukan.")
            return False

    def brute_force_7z(self, sevenz_path, wordlist_path):
        try:
            with open(wordlist_path, 'r', encoding='utf-8', errors='ignore') as wordlist:
                print(f"\n{Fore.YELLOW}[*] Memulai brute force 7z...\n")
                for line in wordlist:
                    password = line.strip()
                    try:
                        with py7zr.SevenZipFile(sevenz_path, mode='r', password=password) as archive:
                            archive.extractall()
                            print(f"\n{Fore.GREEN}[✓] Password 7z ditemukan: {Style.BRIGHT}{password}")
                            return True
                    except:
                        print(f"{Fore.RED}[-] 7z Salah: {password}")
            print(f"\n{Fore.RED}[×] Password 7z tidak ditemukan dalam wordlist.")
            return False
        except FileNotFoundError:
            print(f"{Fore.RED}[!] File 7z tidak ditemukan atau rusak.")
            return False

    def run_gui(self):
        self.gui.run()

if __name__ == "__main__":
    main_app = Main()
    main_app.run_gui()