import imgui
import glfw
from imgui.integrations.glfw import GlfwRenderer
import OpenGL.GL as gl

class GUI:
    def __init__(self):
        self.window = None
        self.renderer = None
        
        self.imgui_ctx = False

        # GLFW SETUP (WINDOW) (OPEN GL AAAAH WINDOW)
        if not glfw.init():
            print("GLFW???")

        glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 3)
        glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 3)
        glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)
        glfw.window_hint(glfw.OPENGL_FORWARD_COMPAT, glfw.TRUE)
        
        self.window = glfw.create_window(800, 600, "DhanZipCracker", None, None)
        if not self.window:
            glfw.terminate()
            print("GLFW???")

        glfw.make_context_current(self.window)
        glfw.swap_interval(1)

        # GUI SETUP
        try:
            imgui.create_context()
            self.imgui_ctx = True
            self.renderer = GlfwRenderer(self.window)
        except Exception as e:
            print(f"Error (Imgui Init): {e}")
            self._cleanup_glfw()
        
    def run(self):

        while not glfw.window_should_close(self.window):
            glfw.poll_events()
            self.renderer.process_inputs()

            imgui.new_frame()
            imgui.begin("DHAN ZIP CRACKER")
            imgui.text("TEXT HERE")
            imgui.end()

            gl.glClearColor(0.2, 0.2, 0.2, 1.0)
            gl.glClear(gl.GL_COLOR_BUFFER_BIT)

            imgui.render()
            self.renderer.render(imgui.get_draw_data())
            glfw.swap_buffers(self.window)

        self._cleanup()

    def _cleanup_glfw(self):
        if self.window:
            glfw.destroy_window(self.window)
            self.window = None
        glfw.terminate()

    def _cleanup(self):
        if self.renderer:
            self.renderer.shutdown()
            self.renderer = None

        if self.imgui_ctx:
            try:
                imgui.destroy_context()
                self.imgui_ctx = False
            except RuntimeError:
                pass
        
        self._cleanup_glfw()
