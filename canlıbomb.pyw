import glfw
import imgui
from imgui.integrations.glfw import GlfwRenderer
from OpenGL import GL
import time


WINDOW_W = 700
WINDOW_H = 440


def apply_dark_red_theme():
    style = imgui.get_style()
    colors = style.colors

    colors[imgui.COLOR_WINDOW_BACKGROUND] = (0.07, 0.07, 0.07, 1.0)
    colors[imgui.COLOR_HEADER] = (0.6, 0.1, 0.1, 1.0)
    colors[imgui.COLOR_HEADER_HOVERED] = (0.85, 0.15, 0.15, 1.0)
    colors[imgui.COLOR_HEADER_ACTIVE] = (1.0, 0.2, 0.2, 1.0)

    colors[imgui.COLOR_BUTTON] = (0.6, 0.1, 0.1, 1.0)
    colors[imgui.COLOR_BUTTON_HOVERED] = (0.85, 0.15, 0.15, 1.0)
    colors[imgui.COLOR_BUTTON_ACTIVE] = (1.0, 0.2, 0.2, 1.0)

    colors[imgui.COLOR_CHECK_MARK] = (1.0, 0.2, 0.2, 1.0)
    colors[imgui.COLOR_SLIDER_GRAB] = (1.0, 0.2, 0.2, 1.0)
    colors[imgui.COLOR_SLIDER_GRAB_ACTIVE] = (1.0, 0.4, 0.4, 1.0)


def main():
    if not glfw.init():
        return

    glfw.window_hint(glfw.RESIZABLE, False)
    glfw.window_hint(glfw.FLOATING, True)

    window = glfw.create_window(
        WINDOW_W,
        WINDOW_H,
        "AFGAN MODMENU",
        None,
        None
    )
    glfw.make_context_current(window)

    imgui.create_context()
    impl = GlfwRenderer(window)
    apply_dark_red_theme()

    methods = [
        "Method 1 – Loader",
        "Method 2 – External",
        "Method 3 – Manual",
        "Method 4 – Kernel",
        "Method 5 – Experimental",
    ]

    selected_method = 0
    auto_attach = False
    stealth_mode = False
    logs = []

    ascii_art = """
        A F G A N   M O D M E N U
        legit? maybe. working? NO.
    """

    while not glfw.window_should_close(window):
        glfw.poll_events()
        impl.process_inputs()
        imgui.new_frame()

        imgui.set_next_window_size(WINDOW_W, WINDOW_H)
        imgui.set_next_window_position(0, 0)

        imgui.begin(
            "AFGAN MODMENU",
            flags=imgui.WINDOW_NO_MOVE
            | imgui.WINDOW_NO_RESIZE
            | imgui.WINDOW_NO_COLLAPSE,
        )

        imgui.text("🔥 Ultimate Afghan Technology 🔥")
        imgui.separator()

        # LEFT PANEL
        imgui.begin_child("left", 220, 0, True)
        imgui.text("Injection Method")
        imgui.separator()

        _, selected_method = imgui.combo(
            "##methods",
            selected_method,
            methods
        )

        imgui.spacing()
        _, auto_attach = imgui.checkbox("Auto Attach", auto_attach)
        _, stealth_mode = imgui.checkbox("Ultra Stealth 😎", stealth_mode)

        imgui.end_child()
        imgui.same_line()

        # RIGHT PANEL
        imgui.begin_child("right", 0, 0, True)
        imgui.text("Status")
        imgui.separator()

        imgui.text(f"Selected: {methods[selected_method]}")
        imgui.text(f"Auto Attach: {'ON' if auto_attach else 'OFF'}")
        imgui.text(f"Stealth: {'ON' if stealth_mode else 'OFF'}")

        imgui.spacing()
        if imgui.button("Inject (Inshallah)", width=160):
            logs.append(f"[{time.strftime('%H:%M:%S')}] Inject failed successfully ✔")

        imgui.same_line()
        if imgui.button("Unload", width=120):
            logs.append(f"[{time.strftime('%H:%M:%S')}] Nothing unloaded")

        imgui.spacing()
        imgui.separator()
        imgui.text("Log")

        imgui.begin_child("log", 0, 90, True)
        for log in logs[-6:]:
            imgui.text(log)
        imgui.end_child()

        imgui.spacing()
        imgui.separator()
        imgui.text("ASCII AREA")

        # ASCII AREA (GENİŞ)
        imgui.begin_child("ascii", 0, 140, True)
        imgui.text_unformatted(ascii_art)
        imgui.end_child()

        imgui.end_child()
        imgui.end()

        imgui.render()
        GL.glClearColor(0.05, 0.05, 0.05, 1)
        GL.glClear(GL.GL_COLOR_BUFFER_BIT)
        impl.render(imgui.get_draw_data())
        glfw.swap_buffers(window)

    impl.shutdown()
    glfw.terminate()


if __name__ == "__main__":
    main()
