import zipfile
import py7zr
import os
from colorama import Fore

from gui import GUI
import flet as ft

class DhanZipCracker:
    def __init__(self):
        self.gui = GUI(self)
        
        self.zip_file_path = None
        self.txt_file_path = None

    def start_cracking(self):
        self.zip_file_path = self.gui.zip_file_path
        self.txt_file_path = self.gui.txt_file_path

        if not self.zip_file_path:
            self.gui.log_message(f"{Fore.RED}[!] Pilih file ZIP/7z terlebih dahulu.")
            return
        if not self.txt_file_path:
            self.gui.log_message(f"{Fore.RED}[!] Pilih file wordlist terlebih dahulu.")
            return

        self.gui.log_message(f"{Fore.YELLOW}[*] Memulai crack...")

        file_extension = os.path.splitext(self.zip_file_path)[1].lower()

        if file_extension == ".zip":
            success = self.brute_force_zip(self.zip_file_path, self.txt_file_path)
            if not success:
                self.gui.log_message(f"{Fore.RED}[×] Password ZIP tidak ditemukan dalam wordlist.")
        elif file_extension == ".7z":
            success = self.brute_force_7z(self.zip_file_path, self.txt_file_path)
            if not success:
                self.gui.log_message(f"{Fore.RED}[×] Password 7z tidak ditemukan dalam wordlist.")
        else:
            self.gui.log_message(f"{Fore.RED}[!] Ekstensi file tidak didukung: {file_extension}")


    def brute_force_zip(self, zip_path, wordlist_path):
        try:
            with zipfile.ZipFile(zip_path, 'r') as zip_file:
                with open(wordlist_path, 'r', encoding='utf-8', errors='ignore') as wordlist:
                    self.gui.log_message(f"{Fore.YELLOW}[*] Memulai brute force ZIP...")
                    for line in wordlist:
                        password = line.strip()
                        try:
                            zip_file.extractall(pwd=bytes(password, 'utf-8'))
                            self.gui.log_message(f"{Fore.GREEN}[✓] Password ZIP ditemukan: {password}")
                            return True
                        except:
                            self.gui.log_message(f"{Fore.RED}[-] ZIP Salah: {password}")
            return False
        except zipfile.BadZipFile:
            self.gui.log_message(f"{Fore.RED}[!] File ZIP rusak atau tidak valid.")
            return False
        except FileNotFoundError:
            self.gui.log_message(f"{Fore.RED}[!] File ZIP atau wordlist tidak ditemukan.")
            return False

    def brute_force_7z(self, sevenz_path, wordlist_path):
        try:
            with open(wordlist_path, 'r', encoding='utf-8', errors='ignore') as wordlist:
                self.gui.log_message(f"{Fore.YELLOW}[*] Memulai brute force 7z...")
                for line in wordlist:
                    password = line.strip()
                    try:
                        with py7zr.SevenZipFile(sevenz_path, mode='r', password=password) as archive:
                            archive.extractall()
                            self.gui.log_message(f"{Fore.GREEN}[✓] Password 7z ditemukan: {password}")
                            return True
                    except:
                        self.gui.log_message(f"{Fore.RED}[-] 7z Salah: {password}")
            return False
        except FileNotFoundError:
            self.gui.log_message(f"{Fore.RED}[!] File 7z tidak ditemukan atau rusak.")
            return False


if __name__ == "__main__":
    app = DhanZipCracker()
    ft.app(target=app.gui.run)