import ctypes
import win32gui
import win32con
import random
import time
import math

# ======================
# SYSTEM (3.14 SAFE)
# ======================

user32 = ctypes.windll.user32
SW = user32.GetSystemMetrics(0)
SH = user32.GetSystemMetrics(1)

hdc = win32gui.GetDC(0)

# ======================
# SETTINGS
# ======================

EFFECT = 8

bx, by = 200, 200
dx, dy = 18, 14
frame = 0

VK_ESCAPE = 0x1B

# ======================
# ORIGINAL EFFECTS (1–8)
# ======================

def glitch_blocks():
    x = random.randint(0, SW)
    y = random.randint(0, SH)
    w = random.randint(50, 400)
    h = random.randint(50, 400)
    win32gui.PatBlt(hdc, x, y, w, h, win32con.PATINVERT)


def shake():
    win32gui.BitBlt(hdc, random.randint(-10,10), random.randint(-10,10),
                    SW, SH, hdc, 0, 0, win32con.SRCCOPY)


def tunnel():
    s = 10
    win32gui.StretchBlt(hdc, s, s, SW-s*2, SH-s*2,
                         hdc, 0, 0, SW, SH, win32con.SRCCOPY)


def lines():
    for _ in range(20):
        win32gui.MoveToEx(hdc, random.randint(0,SW), random.randint(0,SH))
        win32gui.LineTo(hdc, random.randint(0,SW), random.randint(0,SH))


def text():
    words = ["ERROR","GLITCH","VOID","SYSTEM"]
    win32gui.TextOut(hdc, random.randint(0,SW), random.randint(0,SH),
                     random.choice(words))


def bounce():
    global bx,by,dx,dy
    size = 140
    bx += dx
    by += dy
    if bx<=0 or bx>=SW-size: dx*=-1
    if by<=0 or by>=SH-size: dy*=-1
    win32gui.PatBlt(hdc,bx,by,size,size,win32con.PATINVERT)


def wave():
    global frame
    offset = int(math.sin(frame*0.15)*80)
    win32gui.BitBlt(hdc,0,offset,SW,SH,hdc,0,0,win32con.SRCCOPY)
    win32gui.BitBlt(hdc,0,-offset,SW,SH,hdc,0,0,win32con.SRCCOPY)
    frame += 1


def bw_corruption():
    for _ in range(40):
        win32gui.PatBlt(hdc,
                        random.randint(0,SW),
                        random.randint(0,SH),
                        random.randint(80,600),
                        random.randint(20,300),
                        random.choice([win32con.BLACKNESS,
                                       win32con.WHITENESS,
                                       win32con.DSTINVERT]))

# ======================
# NEW EFFECTS (9–17)
# ======================

def flash():
    time.sleep(0.08)
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    color = r | (g << 8) | (b << 16)

    brush = win32gui.CreateSolidBrush(color)
    win32gui.SelectObject(hdc, brush)

    win32gui.PatBlt(hdc, 0, 0, SW, SH, win32con.PATCOPY)

    win32gui.DeleteObject(brush)

def pixel_blocks():
    for _ in range(60):
        win32gui.PatBlt(hdc,
                        random.randint(0,SW),
                        random.randint(0,SH),
                        random.randint(20,200),
                        random.randint(20,200),
                        win32con.DSTINVERT)

def pull():
    win32gui.BitBlt(hdc,random.randint(-30,30),0,SW,SH,
                    hdc,0,0,win32con.SRCCOPY)

def vertical_tears():
    for x in range(0,SW,50):
        win32gui.BitBlt(hdc,x,0,20,SH,
                        hdc,x,random.randint(-20,20),win32con.SRCCOPY)

def noise_shake():
    win32gui.BitBlt(hdc,random.randint(-20,20),random.randint(-20,20),
                    SW,SH,hdc,0,0,win32con.SRCCOPY)

def checker_invert():
    size=80
    for y in range(0,SH,size):
        for x in range(0,SW,size):
            if (x+y)//size % 2 == 0:
                win32gui.PatBlt(hdc,x,y,size,size,win32con.DSTINVERT)

def scan_sweep():
    y = random.randint(0, SH)
    win32gui.PatBlt(hdc, 0, y, SW, 6, win32con.DSTINVERT)

def trail():
    for _ in range(10):
        win32gui.PatBlt(hdc,
                        random.randint(0,SW),
                        random.randint(0,SH),
                        100,100,
                        win32con.PATINVERT)

def pulse():
    if random.random()>0.5:
        win32gui.PatBlt(hdc,0,0,SW,SH,win32con.DSTINVERT)

# ======================
# MAIN LOOP
# ======================

try:
    while True:

        if user32.GetAsyncKeyState(VK_ESCAPE) & 0x8000:
            break

        if EFFECT == 1: glitch_blocks()
        elif EFFECT == 2: shake()
        elif EFFECT == 3: tunnel()
        elif EFFECT == 4: lines()
        elif EFFECT == 5: text()
        elif EFFECT == 6: bounce()
        elif EFFECT == 7: wave()
        elif EFFECT == 8: bw_corruption()

        elif EFFECT == 9: flash()
        elif EFFECT == 10: pixel_blocks()
        elif EFFECT == 11: pull()
        elif EFFECT == 12: vertical_tears()
        elif EFFECT == 13: noise_shake()
        elif EFFECT == 14: checker_invert()
        elif EFFECT == 15: scan_sweep()
        elif EFFECT == 16: trail()
        elif EFFECT == 17: pulse()

        time.sleep(0.01)

finally:
    win32gui.ReleaseDC(0, hdc)