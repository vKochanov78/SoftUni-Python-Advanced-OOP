from tkinter import Tk, Canvas


def create_root():
    root = Tk()

    root.title = "GUI Shop"
    root.resizable("False", "False")
    root.geometry("700x600")

    return root


def frame_creator():
    frame = Canvas(root, width=700, height=700)
    frame.grid(row=0, column=0)

    return frame


root = create_root()
frame = frame_creator()