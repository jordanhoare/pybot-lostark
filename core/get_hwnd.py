import pygetwindow as gw
import win32gui


def get_hwnd(Title):
    """
    Returns the HWND number for provided string

    Example:
        > window_title = "Lost Ark"
        > hwnd = get_hwnd(window_title)
        #### Lost Ark (3412402) window was located.
    """
    try:
        a = gw.getWindowsWithTitle(Title)
        a = str(a)
        b = a.split("=", 1)
        b = b[1].split(")", 1)
        hwnd = int(b[0])
        print(f"####################################")
        print(f">>> {Title} ({hwnd}) window was located.")
        return hwnd
    except Exception as Ex:
        print(f">>> From get_hwnd.py: ", Ex)
        print(f">>> No window matched with the title: '{Title}'")
        return 0


def list_window_names():
    """
    Returns a list of windows currently opened

    Example:
        > list_window_names()
        #### 0x20085c ""
        #### 0x3411b2 "LOST ARK (64-bit, DX11) v.2.0.2.1"
        #### 0x4a049c ""
    """

    def winEnumHandler(hwnd, ctx):
        if win32gui.IsWindowVisible(hwnd):
            print(hex(hwnd), '"' + win32gui.GetWindowText(hwnd) + '"')

    win32gui.EnumWindows(winEnumHandler, None)
