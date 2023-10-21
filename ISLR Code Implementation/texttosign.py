import tkinter as tk
from PIL import Image, ImageTk
import pyttsx3

# main window
root = tk.Toplevel()
root.title("Text To Sign Conversion")
root.geometry("450x344")

# dictionary mapping characters to corresponding hand gesture images
gesture_map = {
    'a': 'C:\\Users\\ADMIN\\OneDrive - SONA COLLEGE OF TECHNOLOGY\\Desktop\\App System\\Hand gestures\\a.jpg',
    'b': 'C:\\Users\\ADMIN\\OneDrive - SONA COLLEGE OF TECHNOLOGY\\Desktop\\App System\\Hand gestures\\b.jpg',
    'c': 'C:\\Users\\ADMIN\\OneDrive - SONA COLLEGE OF TECHNOLOGY\\Desktop\\App System\\Hand gestures\\c.jpg',
    'd': 'C:\\Users\\ADMIN\\OneDrive - SONA COLLEGE OF TECHNOLOGY\\Desktop\\App System\\Hand gestures\\d.jpg',
    'e': 'C:\\Users\\ADMIN\\OneDrive - SONA COLLEGE OF TECHNOLOGY\\Desktop\\App System\\Hand gestures\\e.jpg',
    'f': 'C:\\Users\\ADMIN\\OneDrive - SONA COLLEGE OF TECHNOLOGY\\Desktop\\App System\\Hand gestures\\f.jpg',
    'g': 'C:\\Users\\ADMIN\\OneDrive - SONA COLLEGE OF TECHNOLOGY\\Desktop\\App System\\Hand gestures\\g.jpg',
    'h': 'C:\\Users\\ADMIN\\OneDrive - SONA COLLEGE OF TECHNOLOGY\\Desktop\\App System\\Hand gestures\\h.jpg',
    'i': 'C:\\Users\\ADMIN\\OneDrive - SONA COLLEGE OF TECHNOLOGY\\Desktop\\App System\\Hand gestures\\i.jpg',
    'j': 'C:\\Users\\ADMIN\\OneDrive - SONA COLLEGE OF TECHNOLOGY\\Desktop\\App System\\Hand gestures\\j.jpg',
    'k': 'C:\\Users\\ADMIN\\OneDrive - SONA COLLEGE OF TECHNOLOGY\\Desktop\\App System\\Hand gestures\\k.jpg',
    'l': 'C:\\Users\\ADMIN\\OneDrive - SONA COLLEGE OF TECHNOLOGY\\Desktop\\App System\\Hand gestures\\l.jpg',
    'm': 'C:\\Users\\ADMIN\\OneDrive - SONA COLLEGE OF TECHNOLOGY\\Desktop\\App System\\Hand gestures\\m.jpg',
    'n': 'C:\\Users\\ADMIN\\OneDrive - SONA COLLEGE OF TECHNOLOGY\\Desktop\\App System\\Hand gestures\\n.jpg',
    'o': 'C:\\Users\\ADMIN\\OneDrive - SONA COLLEGE OF TECHNOLOGY\\Desktop\\App System\\Hand gestures\\o.jpg',
    'p': 'C:\\Users\\ADMIN\\OneDrive - SONA COLLEGE OF TECHNOLOGY\\Desktop\\App System\\Hand gestures\\p.jpg',
    'q': 'C:\\Users\\ADMIN\\OneDrive - SONA COLLEGE OF TECHNOLOGY\\Desktop\\App System\\Hand gestures\\q.jpg',
    'r': 'C:\\Users\\ADMIN\\OneDrive - SONA COLLEGE OF TECHNOLOGY\\Desktop\\App System\\Hand gestures\\r.jpg',
    's': 'C:\\Users\\ADMIN\\OneDrive - SONA COLLEGE OF TECHNOLOGY\\Desktop\\App System\\Hand gestures\\s.jpg',
    't': 'C:\\Users\\ADMIN\\OneDrive - SONA COLLEGE OF TECHNOLOGY\\Desktop\\App System\\Hand gestures\\t.jpg',
    'u': 'C:\\Users\\ADMIN\\OneDrive - SONA COLLEGE OF TECHNOLOGY\\Desktop\\App System\\Hand gestures\\u.jpg',
    'v': 'C:\\Users\\ADMIN\\OneDrive - SONA COLLEGE OF TECHNOLOGY\\Desktop\\App System\\Hand gestures\\v.jpg',
    'w': 'C:\\Users\\ADMIN\\OneDrive - SONA COLLEGE OF TECHNOLOGY\\Desktop\\App System\\Hand gestures\\w.jpg',
    'x': 'C:\\Users\\ADMIN\\OneDrive - SONA COLLEGE OF TECHNOLOGY\\Desktop\\App System\\Hand gestures\\x.jpg',
    'y': 'C:\\Users\\ADMIN\\OneDrive - SONA COLLEGE OF TECHNOLOGY\\Desktop\\App System\\Hand gestures\\y.jpg',
    'z': 'C:\\Users\\ADMIN\\OneDrive - SONA COLLEGE OF TECHNOLOGY\\Desktop\\App System\\Hand gestures\\z.jpg'
}


# function to display hand gesture images for a given word
# function to display hand gesture images for a given word
# function to display hand gesture images for a given word
def display_gestures(word):
    # remove any existing labels from the root window
    for widget in root.winfo_children():
        if isinstance(widget, tk.Label):
            widget.destroy()

    # initial x and y coordinates for the first image
    x, y = 170, 70

    for char in word:
        if char in gesture_map:
            # Load the hand gesture image for the character
            gesture_image = Image.open(gesture_map[char])
            # Resize the image to fit the window using the Lanczos resampling filter
            gesture_image = gesture_image.resize((100, 100), resample=Image.LANCZOS)
            # Convert the image to a Tkinter-compatible format
            tk_image = ImageTk.PhotoImage(gesture_image)
            # label to display the image
            gesture_label = tk.Label(root, image=tk_image)
            # position the label at the current x and y coordinates
            gesture_label.place(x=x, y=y)
            # say the character using pyttsx3
            engine = pyttsx3.init()
            engine.say(char)
            engine.runAndWait()
            # update the root window to display the new label
            root.update()
            # update the y coordinate for the next image
            y += 0
        else:
            print(f"No gesture image found for character '{char}'")


# function to get the input text and display the corresponding hand gesture images
def submit_text():
    # Get the input text from the text box
    word = input_text.get()
    # Display the hand gesture images for the word
    display_gestures(word)


# text box to get the input text
input_text = tk.Entry(root, width=50)
input_text.pack()

# button to display the hand gesture images
submit_button = tk.Button(root, text="Display gesture", command=lambda: submit_text())
submit_button.pack()

# main loop
root.mainloop()
