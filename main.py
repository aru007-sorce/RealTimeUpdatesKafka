def signup_user ():
    "Continously Takes User Email and Stores it in a file Until the User exist"
    while True:
        email = input("Enter your email for Sign up (or type Exit to Quit): ")
        if email.lower()=='exit':
            print("Exiting Sign up Process")
            break
        with open("emails.txt", "a") as file:
            file.write(email + "\n")
        print(f"Email {email} has been signed up successfully.")

if __name__ == "__main__":
    signup_user()    