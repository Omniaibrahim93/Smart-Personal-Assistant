import webbrowser
import pyautogui
import platform
import subprocess
import os

if platform.system() == "Windows":
    import screen_brightness_control as sbc
    from ctypes import cast, POINTER
    from comtypes import CLSCTX_ALL
    from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

def google_search(query):
    url = f"https://www.google.com/search?q={query}"
    webbrowser.open(url)
    return f"Searching Google for: {query}"

def youtube_search(query):
    url = f"https://www.youtube.com/results?search_query={query}"
    webbrowser.open(url)
    return f"Searching YouTube for: {query}"

def take_screenshot():
    filename = "screenshot.png"
    pyautogui.screenshot(filename)
    return f"Screenshot saved as {filename}"

def lower_brightness():
    if platform.system() != "Windows":
        return "Brightness control is only supported on Windows."
    current = sbc.get_brightness(display=0)[0]
    new_brightness = max(current - 20, 10)
    sbc.set_brightness(new_brightness, display=0)
    return f"Brightness lowered to {new_brightness}%"

def raise_brightness():
    if platform.system() != "Windows":
        return "Brightness control is only supported on Windows."
    current = sbc.get_brightness(display=0)[0]
    new_brightness = min(current + 20, 100)
    sbc.set_brightness(new_brightness, display=0)
    return f"Brightness raised to {new_brightness}%"

def lower_volume():
    if platform.system() != "Windows":
        return "Volume control is only supported on Windows."
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    current = volume.GetMasterVolumeLevelScalar()
    new_volume = max(current - 0.2, 0.1)
    volume.SetMasterVolumeLevelScalar(new_volume, None)
    return f"Volume lowered to {int(new_volume * 100)}%"

def raise_volume():
    if platform.system() != "Windows":
        return "Volume control is only supported on Windows."
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    current = volume.GetMasterVolumeLevelScalar()
    new_volume = min(current + 0.2, 1.0)
    volume.SetMasterVolumeLevelScalar(new_volume, None)
    return f"Volume raised to {int(new_volume * 100)}%"

def start_word_project():
    try:
        if platform.system() == "Windows":
            subprocess.Popen(["start", "winword"], shell=True)
        elif platform.system() == "Darwin":
            subprocess.Popen(["open", "-a", "Microsoft Word"])
        else:
            return "Word launch not supported on this OS."
        return "Microsoft Word opened."
    except FileNotFoundError:
        return "Microsoft Word not found."

def download_music():
    return "Music download feature is not implemented yet."
