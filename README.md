
---

# Automated Social Media Poster 🐦

A simple tool to schedule and auto-post content to platforms like Twitter. Built with Python, leveraging the Tweepy library for Twitter interactions and `tkinter` for the GUI.

## Features 🌟

- Schedule tweets with a specified delay.
- User-friendly GUI for easy interactions.
- Securely uses API keys without exposing them in the main script.

## Prerequisites 📋

- Python 3.x
- Tweepy library (`pip install tweepy`)

## Setup and Usage 🚀

1. **Setup Twitter API Keys**:
   - Create a Twitter developer account and an App to get the necessary API keys.
   - Replace the placeholders in the `API_KEYS` dictionary in the main script with your actual keys:

```python
API_KEYS = {
    'api_key': 'YOUR_API_KEY',
    'api_secret_key': 'YOUR_API_SECRET_KEY',
    'access_token': 'YOUR_ACCESS_TOKEN',
    'access_token_secret': 'YOUR_ACCESS_TOKEN_SECRET'
}
```

2. **Run the Tool**:
   - Execute the Python script.
   - A GUI will appear prompting you to enter your message and a delay (in minutes).
   - After submission, the message will be scheduled to be tweeted after the specified delay.

## Future Improvements 🛠

- Add support for more social media platforms.
- Implement advanced error handling.
- Enhance the GUI with more features like a calendar picker, option to cancel scheduled tweets, etc.
- Securely store and manage API keys.

## Contributing 🤝

Pull requests are welcome! For major changes, please open an issue first to discuss what you'd like to change.

## License 📄

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

---

