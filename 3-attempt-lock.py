   
def main():
    error = 0
    for i in range(3):
      username = input("Enter the username: ")
      password = input("Enter the password: ")
      if password == "admin123" and username == "admin":
        print("Access granted!")
        break
      else:
        print("Access denied! Incorrect username or password.")
        error = error + 1
      
    if error == 3:
         print("Too many failed attempts. Access denied.")
if __name__ == "__main__":
    main()
