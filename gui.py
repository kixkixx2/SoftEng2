

from pathlib import Path

from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\softeng\build\gui.py")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("950x600")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 600,
    width = 950,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    0.0,
    0.0,
    950.0,
    466.0,
    fill="#01BAF2",
    outline="")

canvas.create_rectangle(
    509.0,
    3.0,
    985.0,
    606.0,
    fill="#0D578C",
    outline="")

canvas.create_text(
    732.0,
    248.0,
    anchor="nw",
    text="Login",
    fill="#FFFFFF",
    font=("RobotoRoman Black", 20 * -1)
)

canvas.create_text(
    35.0,
    212.0,
    anchor="nw",
    text="COOPERATIVE",
    fill="#033B8E",
    font=("RobotoFlex ExtraBold", 64 * -1)
)

canvas.create_text(
    35.0,
    11.0,
    anchor="nw",
    text="SAN AGUSTIN",
    fill="#033B8E",
    font=("RobotoFlex ExtraBold", 64 * -1)
)

canvas.create_text(
    533.0,
    279.0,
    anchor="nw",
    text="Username",
    fill="#FFFFFF",
    font=("RobotoRoman SemiBold", 20 * -1)
)

canvas.create_text(
    533.0,
    355.0,
    anchor="nw",
    text="Password",
    fill="#FFFFFF",
    font=("RobotoRoman SemiBold", 20 * -1)
)

canvas.create_text(
    566.0,
    508.0,
    anchor="nw",
    text="By continuing you indicate that you agree to our Terms of Service, Refund & Cancellation and Privacy Policy.\n",
    fill="#FFFFFF",
    font=("RobotoRoman SemiBold", 14 * -1)
)

canvas.create_text(
    655.0,
    554.0,
    anchor="nw",
    text="Don't have an account? Signup",
    fill="#FFFFFF",
    font=("RobotoRoman SemiBold", 14 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    729.0,
    322.0,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=536.0,
    y=302.0,
    width=386.0,
    height=38.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    729.0,
    401.0,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=536.0,
    y=381.0,
    width=386.0,
    height=38.0
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=629.0,
    y=467.0,
    width=224.0,
    height=26.0
)

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    769.0,
    127.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    255.0,
    422.0,
    image=image_image_2
)

canvas.create_rectangle(
    562.0,
    431.0,
    575.0,
    444.0,
    fill="#D9D9D9",
    outline="")

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
button_2.place(
    x=813.0,
    y=428.0,
    width=120.0,
    height=20.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_3 clicked"),
    relief="flat"
)
button_3.place(
    x=816.0,
    y=430.0,
    width=114.0,
    height=16.0
)

canvas.create_text(
    35.0,
    66.0,
    anchor="nw",
    text="DAIRY",
    fill="#FFFFFF",
    font=("PoetsenOne Regular", 128 * -1)
)
window.resizable(False, False)
window.mainloop()
