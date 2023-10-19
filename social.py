import tweepy
import tkinter as tk
from tkinter import simpledialog, messagebox
import sched
import time

# Function to post to Twitter
def post_to_twitter(api_key, api_secret_key, access_token, access_token_secret, message):
    auth = tweepy.OAuthHandler(api_key, api_secret_key)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    api.update_status(message)

# Function to schedule a tweet
def schedule_tweet(s, delay, api_keys, message):
    s.enter(delay, 1, post_to_twitter, argument=(api_keys['api_key'], api_keys['api_secret_key'], 
                                                 api_keys['access_token'], api_keys['access_token_secret'], 
                                                 message))
    s.run()

# GUI to get user input and trigger the scheduler
def launch_gui(api_keys):
    def submit():
        message = text_var.get()
        delay = int(delay_var.get()) * 60  # convert minutes to seconds
        s = sched.scheduler(time.time, time.sleep)
        schedule_tweet(s, delay, api_keys, message)
        messagebox.showinfo("Success", "Tweet scheduled successfully!")
        root.quit()

    root = tk.Tk()
    root.title("Automated Social Media Poster")

    tk.Label(root, text="Enter your message:").pack(pady=20)
    text_var = tk.StringVar()
    tk.Entry(root, textvariable=text_var, width=50).pack()

    tk.Label(root, text="Schedule delay (in minutes):").pack(pady=20)
    delay_var = tk.StringVar()
    tk.Entry(root, textvariable=delay_var, width=50).pack()

    tk.Button(root, text="Schedule Tweet", command=submit).pack(pady=20)

    root.mainloop()

if __name__ == "__main__":
    API_KEYS = {
        'api_key': 'YOUR_API_KEY',
        'api_secret_key': 'YOUR_API_SECRET_KEY',
        'access_token': 'YOUR_ACCESS_TOKEN',
        'access_token_secret': 'YOUR_ACCESS_TOKEN_SECRET'
    }
    launch_gui(API_KEYS)
