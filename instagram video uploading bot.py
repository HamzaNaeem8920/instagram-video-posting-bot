import tkinter as tk
from tkinter import filedialog
from instabot import Bot

class InstagramBotGUI:
    def __init__(self, master):
        self.master = master
        master.title("Instagram Bot")

        # Create the labels and entry fields for username and password
        tk.Label(master, text="Username:").grid(row=0)
        self.username_entry = tk.Entry(master)
        self.username_entry.grid(row=0, column=4)
        tk.Label(master, text="Password:").grid(row=1)
        self.password_entry = tk.Entry(master, show="*")
        self.password_entry.grid(row=1, column=4)

        # Create the "Browse" button for selecting the video file to post
        tk.Label(master, text="Video file:").grid(row=2)
        self.video_path_entry = tk.Entry(master)
        self.video_path_entry.grid(row=2, column=4)
        self.browse_button = tk.Button(master, text="Browse", command=self.select_video_file)
        self.browse_button.grid(row=2, column=5)

        # Create the label and entry field for the post caption
        tk.Label(master, text="Caption:").grid(row=3)
        self.caption_entry = tk.Entry(master)
        self.caption_entry.grid(row=3, column=4)

        # Create the "Post" button
        self.post_button = tk.Button(master, text="Post", command=self.post_video)
        self.post_button.grid(row=4, column=4)

    def select_video_file(self):
        # Open a file dialog box to select the video file
        file_path = filedialog.askopenfilename()
        # Update the video path entry field with the selected file path
        self.video_path_entry.delete(0, tk.END)
        self.video_path_entry.insert(0, file_path)

    def post_video(self):
        # Get the username, password, video path, and caption from the GUI inputs
        username = self.username_entry.get()
        password = self.password_entry.get()
        video_path = self.video_path_entry.get()
        caption = self.caption_entry.get()

        # Initialize the bot
        bot = Bot()

        # Login to your Instagram account
        bot.login(username=username, password=password)

        # Post the video
        bot.upload_video(video_path, caption=caption)

        # Logout from your account
        bot.logout()

        # Show a message box to indicate that the video has been posted
        tk.messagebox.showinfo("Success", "Your video has been posted!")

if __name__ == '__main__':
    root = tk.Tk()
    root.geometry("600x600")
    insta_bot_gui = InstagramBotGUI(root)
    root.mainloop()
