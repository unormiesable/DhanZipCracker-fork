import flet as ft
import sys
import re

class GUI:
    def __init__(self, app):
        self.app = app
        self.button_width = 250
        
        self.zip_file_path = None
        self.txt_file_path = None
        self.log_text_control = ft.Column(
            controls=[],
            scroll=ft.ScrollMode.HIDDEN,
            expand=True,
            spacing=0
        )
        
        self.log_column_control = ft.Column(
            [self.log_text_control],
            scroll=ft.ScrollMode.HIDDEN,
            expand=True
        )
        self.start_button_ref = None
        self._cracking_in_progress = False
    
    
    def run(self, page: ft.Page):
        page.title = "DhanZipCracker"
        
        page.window.width = 800
        page.window.height = 600
        page.window.resizable = False
        page.window.maximizable = False
        page.window.opacity = 0.925
        page.window.borderless = True
        page.window.frameless = True
        
        page.window.shadow = True
        page.window.center()
        
        page.window_draggable = True 
        
        page.vertical_alignment = ft.CrossAxisAlignment.START
        page.horizontal_alignment = ft.CrossAxisAlignment.START
        
        page.theme = ft.Theme(
            scrollbar_theme=ft.ScrollbarTheme(
                
                track_visibility=False,
                track_border_color=ft.Colors.TRANSPARENT,
                thumb_visibility=True,

                thickness=0,
                radius=0,
                main_axis_margin=5,
                cross_axis_margin=10,
            )
        )

        
        # KEYBOARD INPUT (ESC TO QUIT)
        def key_input(e: ft.KeyboardEvent):
            if e.key == "Escape":
                page.window.destroy()
            page.update()

        page.on_keyboard_event = key_input
        
        
        # SOURCE FILE PICKER THINGY (ZIP/7z)
        def on_zip_file_result(e: ft.FilePickerResultEvent):
            if e.files:
                self.zip_file_path = e.files[0].path
                selected_zip_text.content.controls[0].value = f"Zip/7z terpilih : {e.files[0].name}"
                self.log_message(f"ZIP/7z Terpilih : {e.files[0].path}")
            else:
                selected_zip_text.content.controls[0].value = "Tidak ada ZIP/7z terpilih"
                self.log_message("Tidak ada ZIP/7z terpilih")
            page.update()

        zip_file_picker = ft.FilePicker(on_result=on_zip_file_result)
        page.overlay.append(zip_file_picker)


        # SOURCE WORDLIST PICKER THINGY (TXT)
        def on_txt_file_result(e: ft.FilePickerResultEvent):
            if e.files:
                self.txt_file_path = e.files[0].path
                selected_wordlist_text.content.controls[0].value = f"Wordlist Terpilih : {e.files[0].name}"
                self.log_message(f"Wordlist Terpilih : {e.files[0].path}")
            else:
                selected_wordlist_text.content.controls[0].value = "Tidak ada wordlist terpilih"
                self.log_message("Tidak ada wordlist terpilih")
            page.update()

        txt_file_picker = ft.FilePicker(on_result=on_txt_file_result)
        page.overlay.append(txt_file_picker)


        # LOG (AUTO SCROLL)
        def log_message(message: str):
            parts = re.split(r'(\x1b\[\d+m)', message)
            
            current_message_parts = []
            
            current_color = ft.Colors.WHITE
            current_weight = ft.FontWeight.NORMAL

            color_map = {
                '\x1b[31m': ft.Colors.RED,
                '\x1b[33m': ft.Colors.YELLOW,
                '\x1b[32m': ft.Colors.GREEN,
                '\x1b[39m': ft.Colors.WHITE,
                '\x1b[1m': ft.FontWeight.BOLD,
                '\x1b[22m': ft.FontWeight.NORMAL,
                '\x1b[0m': ft.Colors.WHITE,
            }
            
            for part in parts:
                if part in color_map:
                    if part == '\x1b[1m':
                        current_weight = ft.FontWeight.BOLD
                    elif part == '\x1b[22m':
                        current_weight = ft.FontWeight.NORMAL
                    elif part == '\x1b[0m':
                        current_color = ft.Colors.WHITE
                        current_weight = ft.FontWeight.NORMAL
                    else:
                        current_color = color_map[part]
                else:
                    if part:
                        current_message_parts.append(
                            ft.Text(part, color=current_color, weight=current_weight)
                        )
            
            self.log_text_control.controls.append(ft.Row(current_message_parts, spacing=0))
            
            page.update()
            self.log_column_control.scroll_to(offset=-1, duration=100)

        self.log_message = log_message

        # CLEAR LOG
        def clear_logs(e):
            self.log_text_control.controls.clear()
            page.update()

        def toggle_cracking_state(e):
            if not self._cracking_in_progress:
                self.app.start_cracking()
            else:
                self.app.stop_cracking()
            page.update()

        def update_start_button(is_cracking):
            self._cracking_in_progress = is_cracking
            if self.start_button_ref:
                if is_cracking:
                    self.start_button_ref.content.controls[0].icon = ft.Icons.STOP
                    self.start_button_ref.content.controls[1].value = "Hentikan"
                else:
                    self.start_button_ref.content.controls[0].icon = ft.Icons.PLAY_ARROW
                    self.start_button_ref.content.controls[1].value = "Mulai Crack"
                page.update()
        self.update_start_button = update_start_button

        # UI SETUP
        selected_zip_text = ft.ElevatedButton(
            content=ft.Row(
                [ft.Text("Tidak ada Zip/7z terpilih")],
                alignment=ft.MainAxisAlignment.START,
            ),
            style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(radius=5),
            ),
            width=self.button_width,
            disabled=True
        )

        selected_wordlist_text = ft.ElevatedButton(
            content=ft.Row(
                [ft.Text("Tidak ada wordlist terpilih")],
                alignment=ft.MainAxisAlignment.START,
            ),
            style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(radius=5),
            ),
            width=self.button_width,
            disabled=True
        )
        
        self.start_button_ref = ft.FilledButton(
            content=ft.Row(
                [
                    ft.Icon(ft.Icons.PLAY_ARROW),
                    ft.Text("Mulai Crack"),
                ],
                alignment=ft.MainAxisAlignment.START,
                spacing=10,
            ),
            on_click=toggle_cracking_state,
            style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(radius=5),
            ),
            width=self.button_width
        )


        page.add(
            ft.WindowDragArea(
                content=ft.Container(
                    content=ft.Row(
                        [
                            ft.Image(
                                src="./assets/Title.svg",
                                height=65,
                                fit=ft.ImageFit.CONTAIN,
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        vertical_alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                    bgcolor=ft.Colors.BLUE_GREY_900,
                    height=65,
                    padding=ft.padding.only(left=0, right=0),
                    alignment=ft.alignment.center, 
                ),
                expand= False
            ),
            
            ft.Row(
                [
                    # LEFT SIDE (CONTROL PANEL)
                    ft.Column(
                        [
                            selected_zip_text,
                            selected_wordlist_text,
                            
                            
                            ft.ElevatedButton(
                                content=ft.Row(
                                    [
                                        ft.Icon(ft.Icons.UPLOAD_FILE),
                                        ft.Text("Pilih File Zip/7z"),
                                    ],
                                    alignment=ft.MainAxisAlignment.START,
                                    spacing=10,
                                ),
                                on_click=lambda _: zip_file_picker.pick_files(
                                    allow_multiple=False,
                                    allowed_extensions=["zip", "7z"]
                                ),
                                style=ft.ButtonStyle(
                                    shape=ft.RoundedRectangleBorder(radius=5),
                                ),
                                width=self.button_width
                            ),
                            
                            
                            ft.ElevatedButton(
                                content=ft.Row(
                                    [
                                        ft.Icon(ft.Icons.UPLOAD_FILE),
                                        ft.Text("Pilih File Txt (Wordlist)"),
                                    ],
                                    alignment=ft.MainAxisAlignment.START,
                                    spacing=10,
                                ),
                                on_click=lambda _: txt_file_picker.pick_files(
                                    allow_multiple=False,
                                    allowed_extensions=["txt"]
                                ),
                                style=ft.ButtonStyle(
                                    shape=ft.RoundedRectangleBorder(radius=5),
                                ),
                                width=self.button_width
                            ),
                            
                            
                            self.start_button_ref,


                            ft.OutlinedButton(
                                content=ft.Row(
                                    [
                                        ft.Icon(ft.Icons.CLEAR),
                                        ft.Text("Clear Logs"),
                                    ],
                                    alignment=ft.MainAxisAlignment.START,
                                    spacing=10,
                                ),
                                on_click=clear_logs,
                                style=ft.ButtonStyle(
                                    shape=ft.RoundedRectangleBorder(radius=5),
                                ),
                                width=self.button_width
                            ),
                            
                            
                            ft.Container(
                                content=ft.Text(
                                    "Press Esc To Exit",
                                    text_align=ft.TextAlign.CENTER,
                                    color=ft.Colors.GREY_500
                                ),
                                padding=ft.padding.only(top=225),
                            ),
                            
                            
                        ],
                        alignment=ft.MainAxisAlignment.START,
                        horizontal_alignment=ft.CrossAxisAlignment.START,
                        expand=1
                    ),
                    
                    
                    ft.VerticalDivider(),
                    
                    
                    # RIGHT SIDE (LOGS)
                    ft.Column(
                        [
                            ft.Text("TERMINAL LOGS:", weight=ft.FontWeight.BOLD),
                            ft.Container(
                                content=self.log_column_control,
                                padding=10,
                                expand=True,
                            )
                        ],
                        alignment=ft.MainAxisAlignment.START,
                        horizontal_alignment=ft.CrossAxisAlignment.START,
                        expand=2
                    )
                ],
                expand=True
            )
        )