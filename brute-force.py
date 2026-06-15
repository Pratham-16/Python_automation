def brute_force():
    pin = "2847"     
    attempts = 0
    print("Cracking the PIN...")

    for guess in range(10000):
        current = str(guess).zfill(4)   
        attempts = attempts + 1
        if current == pin:
            print(f"Found the PIN: {current} ✅")
            print(f"Total attempts: {attempts}")
            break
        else:
            print(f"Trying: {current}")  # optional

def main():
    brute_force()

if __name__ == "__main__":
    main()