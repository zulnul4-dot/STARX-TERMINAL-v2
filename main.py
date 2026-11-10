
import os
import sys
import time
import random
import shutil
import platform
import subprocess
import shlex
from datetime import datetime

# ==========================================
# STARX TERMINAL V5.2 FULL
# ==========================================

VERSION = "5.2 MATRIX ST EDITION"

R = "\033[91m"
Y = "\033[93m"
G = "\033[92m"
C = "\033[96m"
W = "\033[97m"
D = "\033[90m"
M = "\033[95m"
B = "\033[1m"
X = "\033[0m"

THEME = C
HISTORY = []
BASH = shutil.which("bash") or "/system/bin/sh"

# ==========================================
# STARX LOGO
# ==========================================

FONT = {
    "S": ["1111","1000","1111","0001","1111"],
    "T": ["1111","0110","0110","0110","0110"],
    "A": ["0110","1001","1111","1001","1001"],
    "R": ["1110","1001","1110","1010","1001"],
    "X": ["1001","0110","0110","0110","1001"]
}

def make_logo():
    rows = [[] for _ in range(5)]

    for letter in "STARX":
        for y in range(5):
            for bit in FONT[letter][y]:
                color = R if letter in "STAR" else Y
                rows[y].append((bit == "1", color))
            rows[y].append((False, X))

    return rows

def show_logo():
    os.system("clear")
    logo = make_logo()

    for step in range(1, len(logo[0]) + 1):
        sys.stdout.write("\033[H")

        for row in logo:
            for visible, color in row[:step]:
                char = "█" if visible else " "
                sys.stdout.write(color + B + char + X)
            sys.stdout.write("\033[K\n")

        sys.stdout.flush()
        time.sleep(0.025)

    print()
    print(Y + B + "    STARX TERMINAL V5.2" + X)
    print(D + "    ANDROID | TERMUX" + X)
    print()

# ==========================================
# STATUS
# ==========================================

def status():
    print(C + B + "\n[ SYSTEM STATUS ]" + X)
    print(G + " ● STARX ONLINE" + X)
    print(" Version :", VERSION)
    print(" Platform:", platform.system())
    print(" Python  :", platform.python_version())
    print(" Folder  :", os.getcwd())
    print(" Time    :", datetime.now().strftime("%H:%M:%S"))

    try:
        disk = shutil.disk_usage(os.path.expanduser("~"))
        print(" Storage :", round(disk.free / 1024**3, 2), "GB free")
    except Exception:
        pass

    print()

def sysinfo():
    print(C + B + "\n[ DEVICE INFORMATION ]" + X)
    print("System      :", platform.system())
    print("Release     :", platform.release())
    print("Machine     :", platform.machine())
    print("Architecture:", platform.architecture()[0])
    print("Python      :", platform.python_version())
    print("Directory   :", os.getcwd())
    print()

def storage():
    print(C + B + "\n[ STORAGE ]" + X)
    try:
        disk = shutil.disk_usage(os.path.expanduser("~"))
        print("Total:", round(disk.total / 1024**3, 2), "GB")
        print("Used :", round(disk.used / 1024**3, 2), "GB")
        print("Free :", round(disk.free / 1024**3, 2), "GB")
    except Exception as e:
        print(e)
    print()

def memory():
    print(C + B + "\n[ MEMORY ]" + X)
    try:
        with open("/proc/meminfo") as f:
            for line in f:
                if line.startswith(("MemTotal:", "MemAvailable:")):
                    print(line.strip())
    except Exception:
        print("Memory unavailable.")
    print()

def cpu():
    print(C + B + "\n[ CPU ]" + X)
    try:
        with open("/proc/cpuinfo") as f:
            for line in f:
                if line.startswith(("Hardware", "model name", "Processor")):
                    print(line.strip())
                    break
    except Exception:
        print("CPU information unavailable.")
    print()

def uptime():
    print(C + B + "\n[ UPTIME ]" + X)
    try:
        with open("/proc/uptime") as f:
            seconds = int(float(f.read().split()[0]))
        print(seconds // 3600, "hours", (seconds % 3600) // 60, "minutes")
    except Exception:
        print("Uptime unavailable.")
    print()

def battery():
    print(C + B + "\n[ BATTERY ]" + X)
    if shutil.which("termux-battery-status"):
        subprocess.run(["termux-battery-status"])
    else:
        print(Y + "Requires Termux:API and termux-api package." + X)
    print()

# ==========================================
# MATRIX
# ==========================================

def matrix(st=False):
    width = min(shutil.get_terminal_size((40, 20)).columns, 70)

    starx_cat = [
        r" /\_/\ ",
        r"( o.o )",
        r" > ^ < ",
        r" S T A R X "
    ]

    if st:
        print(G + B + "\n[ MATRIX ST ]" + X)
    else:
        print(G + B + "\n[ MATRIX ]" + X)

    print(D + "Press CTRL+C to stop." + X)

    try:
        while True:
            if st:
                for _ in range(3):
                    line = "".join(
                        random.choice("01STARX")
                        for _ in range(width)
                    )
                    print(G + line + X)

                print()
                for line in starx_cat:
                    print(C + B + line.center(width) + X)
                print()

            else:
                line = "".join(
                    random.choice("01STARX")
                    for _ in range(width)
                )
                print(G + line + X)

            time.sleep(0.15)

    except KeyboardInterrupt:
        print(Y + "\nMatrix stopped." + X)

# ==========================================
# MENUS
# ==========================================

def help_menu():
    print(C + B + "\n[ STARX HELP ]" + X)
    print(Y + "SYSTEM" + X)
    print("status, sysinfo, cpu, memory, storage, battery, uptime")
    print(Y + "\nTERMINAL" + X)
    print("help, menu, tools, banner, clear, history")
    print("about, version, theme, restart, exit")
    print(Y + "\nMATRIX" + X)
    print("matrix")
    print("matrix st")
    print(Y + "\nSECRET" + X)
    print("secret, hackerman, ghost, rainbow")
    print("scan, easteregg, godmode")
    print(Y + "\nTERMUX" + X)
    print("ls, cd, pwd, mkdir, cp, mv, rm")
    print("pkg, apt, python, pip, git, curl, wget, nano")
    print(D + "\nOther installed commands are passed to Bash." + X)
    print()

def menu():
    print(C + B + "\n[ STARX MAIN MENU ]" + X)
    print("01. System")
    print("02. Files")
    print("03. Packages")
    print("04. Python")
    print("05. Network")
    print("06. Matrix")
    print("07. Secret commands")
    print("08. Themes")
    print()

def tools():
    print(C + B + "\n[ STARX TOOLS ]" + X)

    groups = {
        "FILES": "ls pwd cd mkdir rmdir touch cat cp mv find grep",
        "PACKAGES": "pkg apt dpkg",
        "PYTHON": "python pip",
        "GIT": "git clone status pull log",
        "NETWORK": "ping curl wget ssh",
        "SYSTEM": "date whoami uname df free uptime",
        "MATRIX": "matrix matrix st"
    }

    for name, commands in groups.items():
        print(Y + name + X + " : " + commands)
    print()

def about():
    print(M + B + "\nSTARX TERMINAL" + X)
    print("Version:", VERSION)
    print("Python-based Termux interface")
    print("Mode: Local terminal")
    print()

# ==========================================
# THEME
# ==========================================

def change_theme(parts):
    global THEME

    colors = {
        "red": R,
        "yellow": Y,
        "green": G,
        "cyan": C,
        "white": W,
        "purple": M
    }

    if len(parts) < 2:
        print("Themes: red, yellow, green, cyan, white, purple")
        return

    name = parts[1].lower()

    if name in colors:
        THEME = colors[name]
        print(THEME + "Theme changed: " + name.upper() + X)
    else:
        print(R + "Unknown theme." + X)

# ==========================================
# SECRET COMMANDS
# ==========================================

def secret_menu():
    print(M + B + "\n[ CLASSIFIED STARX ]" + X)
    print("matrix     - Matrix animation")
    print("matrix st  - Matrix STARX cat")
    print("hackerman  - Fictional terminal display")
    print("ghost      - Quiet display")
    print("rainbow    - Rainbow text")
    print("scan       - Local system check")
    print("easteregg  - STARX surprise")
    print("godmode    - Special theme")
    print()

def hackerman():
    print(G + B + "\n[ STARX SIMULATION ]" + X)

    for msg in [
        "Loading local terminal...",
        "Checking Python runtime...",
        "Checking storage...",
        "Loading STARX modules...",
        "Simulation complete."
    ]:
        print(G + "[OK] " + msg + X)
        time.sleep(0.4)

    print()

def ghost():
    print(D + B + "\n[ GHOST MODE ]" + X)
    print("STARX quiet display activated.")
    print()

def rainbow():
    colors = [R, Y, G, C, M]
    text = "STARX RAINBOW MODE"

    for i, char in enumerate(text):
        sys.stdout.write(colors[i % len(colors)] + B + char + X)
        sys.stdout.flush()
        time.sleep(0.06)

    print("\n")

def scan():
    print(C + B + "\n[ LOCAL SYSTEM SCAN ]" + X)

    for item in [
        "Python runtime",
        "Storage",
        "Operating system",
        "Terminal environment"
    ]:
        print(Y + "[CHECK] " + item + X)
        time.sleep(0.3)
        print(G + "[OK] " + item + X)

    print("\nLocal inspection complete.")
    status()

def easteregg():
    print(Y + B + "\n★ WELCOME TO STARX SECRET ZONE ★" + X)
    print(M + "STARX NEVER STOPS." + X)
    print()

def godmode():
    global THEME
    THEME = M
    print(M + B + "GODMODE THEME ENABLED." + X)
    print()

# ==========================================
# SHELL
# ==========================================

def run_shell(command):
    try:
        subprocess.run(
            command,
            shell=True,
            executable=BASH,
            cwd=os.getcwd()
        )
    except Exception as e:
        print(R + "Shell error: " + str(e) + X)

# ==========================================
# HISTORY
# ==========================================

def show_history():
    print(C + B + "\n[ COMMAND HISTORY ]" + X)

    if not HISTORY:
        print("No history.")
    else:
        for i, item in enumerate(HISTORY, 1):
            print(str(i).rjust(3), item)

    print()

# ==========================================
# EXECUTE
# ==========================================

def execute(command):
    global THEME

    try:
        parts = shlex.split(command)
    except ValueError as e:
        print(R + str(e) + X)
        return

    if not parts:
        return

    action = parts[0].lower()

    if action in ("exit", "quit"):
        raise SystemExit

    elif action == "help":
        help_menu()

    elif action == "menu":
        menu()

    elif action == "tools":
        tools()

    elif action == "status":
        status()

    elif action in ("sysinfo", "system"):
        sysinfo()

    elif action == "cpu":
        cpu()

    elif action == "memory":
        memory()

    elif action == "storage":
        storage()

    elif action == "battery":
        battery()

    elif action == "uptime":
        uptime()

    elif action in ("banner", "logo"):
        show_logo()

    elif action == "clear":
        os.system("clear")

    elif action == "history":
        show_history()

    elif action == "about":
        about()

    elif action == "version":
        print(Y + "STARX " + VERSION + X)

    elif action == "theme":
        change_theme(parts)

    elif action == "matrix":
        matrix(
            len(parts) > 1 and parts[1].lower() == "st"
        )

    elif action == "secret":
        secret_menu()

    elif action == "hackerman":
        hackerman()

    elif action == "ghost":
        ghost()

    elif action == "rainbow":
        rainbow()

    elif action == "scan":
        scan()

    elif action == "easteregg":
        easteregg()

    elif action == "godmode":
        godmode()

    elif action == "restart":
        print(Y + "Restarting STARX..." + X)
        os.execv(sys.executable, [sys.executable] + sys.argv)

    elif action == "cd":
        target = parts[1] if len(parts) > 1 else "~"

        try:
            os.chdir(os.path.expanduser(target))
        except OSError as e:
            print(R + str(e) + X)

    else:
        run_shell(command)

# ==========================================
# DASHBOARD
# ==========================================

def dashboard():
    print(C + B + "==============================" + X)
    print(Y + B + "       STARX CONTROL" + X)
    print(C + B + "==============================" + X)

    status()

    print(Y + "[ QUICK COMMANDS ]" + X)
    print("help | menu | tools | status")
    print("matrix | matrix st")
    print("secret | sysinfo | storage | history")
    print(G + "\nSTARX READY." + X)
    print()

# ==========================================
# MAIN
# ==========================================

def main():
    show_logo()
    dashboard()

    while True:
        try:
            command = input(
                THEME + B + "STARX >>> " + X
            ).strip()

            if not command:
                continue

            HISTORY.append(command)
            execute(command)

        except SystemExit:
            print(Y + "\nSTARX TERMINATED." + X)
            break

        except KeyboardInterrupt:
            print(Y + "\nUse exit to close STARX." + X)

        except EOFError:
            break

        except Exception as e:
            print(R + "ERROR: " + str(e) + X)

    print(X)

if __name__ == "__main__":
    main()

