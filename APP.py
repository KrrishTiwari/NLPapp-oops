import os
import re
from getpass import getpass

import nlpcloud

API_TOKEN = os.getenv("NLPCLOUD_API_KEY") 
EMAIL_PATTERN = re.compile(r"^[\w.+-]+@[\w-]+\.[\w.-]+$")


class NLPapp:
    def __init__(self):
        self.__database = {}
        self.__client = nlpcloud.Client("gpt-oss-120b", API_TOKEN, gpu=True)
        self.__lang_client = nlpcloud.Client("python-langdetect", API_TOKEN, gpu=False)
        self.__main_loop()

    # ---------- input helpers ----------
    def __ask(self, prompt):
        while True:
            value = input(prompt).strip()
            if value:
                return value
            print("Input cannot be empty. Try again.")

    def __ask_email(self):
        while True:
            email = self.__ask("Enter your email: ").lower()
            if EMAIL_PATTERN.match(email):
                return email
            print("Invalid email format. Try again.")

    def __ask_password(self):
        while True:
            password = getpass("Enter your password: ")
            if len(password) >= 6:
                return password
            print("Password must be at least 6 characters.")

    # ---------- menus ----------
    def __main_loop(self):
        while True:
            choice = input("""
Hi! How would you like to proceed?
1. Not a Member? Register
2. Already a Member? Login
3. Exit
""").strip()

            if choice == "1":
                self.__register()
            elif choice == "2":
                self.__login()
            elif choice == "3":
                print("Goodbye!")
                break
            else:
                print("Invalid Choice")

    def __user_menu(self):
        while True:
            choice = input("""
Hi! How would you like to proceed?
1. NER
2. Language Detection
3. Sentiment Analysis
4. Logout
""").strip()

            if choice == "1":
                self.__ner()
            elif choice == "2":
                self.__lang_analysis()
            elif choice == "3":
                self.__sentiment_analysis()
            elif choice == "4":
                print("Logged out.")
                break
            else:
                print("Invalid Choice")

    # ---------- auth ----------
    def __register(self):
        name = self.__ask("Enter your name: ")
        email = self.__ask_email()
        if email in self.__database:
            print("Already Registered")
            return
        password = self.__ask_password()
        self.__database[email] = [name, password]
        print("Registered Successfully. Now Login.")

    def __login(self):
        email = self.__ask_email()
        if email not in self.__database:
            print("Email not Registered")
            return
        password = getpass("Enter your password: ")
        if self.__database[email][1] == password:
            print("Login Successful")
            self.__user_menu()
        else:
            print("Incorrect Password")

    # ---------- features ----------
    def __ner(self):
        para = self.__ask("Enter the paragraph: ")
        search = self.__ask("What would you like to search: ")
        try:
            response = self.__client.entities(para, searched_entity=search)
            print(response)
        except Exception as e:
            print(f"Error: {e}")

    def __sentiment_analysis(self):
        para = self.__ask("Enter the paragraph: ")
        target = input("Enter a target (optional, press Enter to skip): ").strip()
        try:
            if target:
                response = self.__client.sentiment(para, target=target)
            else:
                response = self.__client.sentiment(para)
            best = max(response["scored_labels"], key=lambda x: x["score"])
            print(best["label"])
        except Exception as e:
            print(f"Error: {e}")

    def __lang_analysis(self):
        para = self.__ask("Enter the paragraph: ")
        try:
            response = self.__lang_client.langdetection(para)
            print(list(response["languages"][0].keys())[0])
        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    if not API_TOKEN:
        raise SystemExit("Set the NLPCLOUD_API_KEY environment variable first.")
    NLPapp()
