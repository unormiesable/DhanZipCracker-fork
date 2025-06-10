import zipfile
import py7zr
import os
from colorama import Fore, Style, init

import imgui
import glfw
from imgui.integrations.glfw import GlfwRenderer
import OpenGL.GL as gl

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
    
    
    # GLFW SETUP (WINDOW)
    if not glfw.init():
        print("GLFW???")
        return

    glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 3)
    glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 3)
    glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)
    glfw.window_hint(glfw.OPENGL_FORWARD_COMPAT, glfw.TRUE)
    
    window = glfw.create_window(800, 600, "DhanZipCracker", None, None)
    if not window:
        glfw.terminate()
        print("GLFW???")
        return

    glfw.make_context_current(window)
    glfw.swap_interval(1)
    
    # GUI SETUP
    imgui.create_context()
    impl = GlfwRenderer(window)
    
    while not glfw.window_should_close(window):
        glfw.poll_events()
        impl.process_inputs()

        imgui.new_frame()

        imgui.begin("DHAN ZIP CRACKER")
        imgui.text("TEXT HERE")
        imgui.end()

        gl.glClearColor(0.2, 0.2, 0.2, 1.0)
        gl.glClear(gl.GL_COLOR_BUFFER_BIT)

        imgui.render()
        impl.render(imgui.get_draw_data())
        glfw.swap_buffers(window)

    impl.shutdown()
    glfw.destroy_window(window)
    glfw.terminate()
    imgui.destroy_context()
    
    
#     ascii_art = fr"""{Fore.CYAN}{Style.BRIGHT}
#  _____  _   _    _    _   _
# |  __ \| | | |  / \  | \ | |
# | |  | | |_| | / _ \ |  \| |
# | |__| |  _  |/ ___ \| |\  |
# |_____/|_| |_/_/   \_\_| \_|
#         D  H  A  N
# """

#     print(ascii_art)
#     print(f"{Fore.MAGENTA}=== ZIP & 7z Password Brute Forcer by Dhan ==={Style.RESET_ALL}\n")

#     file_path = input(f"{Fore.CYAN}[?] Masukkan path file .ZIP/.7z target: ").strip()
#     wordlist_path = input(f"{Fore.CYAN}[?] Masukkan path file wordlist: ").strip()

#     if not os.path.exists(file_path):
#         print(f"{Fore.RED}[!] File target tidak ditemukan.")
#         return

#     if not os.path.exists(wordlist_path):
#         print(f"{Fore.RED}[!] File wordlist tidak ditemukan.")
#         return

#     if file_path.lower().endswith(".zip"):
#         brute_force_zip(file_path, wordlist_path)
#     elif file_path.lower().endswith(".7z"):
#         brute_force_7z(file_path, wordlist_path)
#     else:
#         print(f"{Fore.RED}[!] Format file tidak didukung. Hanya .zip dan .7z")

if __name__ == "__main__":
    main()
