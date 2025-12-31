from zxcvbn import zxcvbn

print("[+] ########################")
print("     PASSWORD STRENGTH CHECKER")
print("[+] ########################\n")

while True:
    password = input("Enter password (or type 'exit' to quit): ")

    if password.lower() == "exit":
        print("\nExiting Password Checker...")
        break

    result = zxcvbn(password)

    print("\n[+] ########################")
    print(f"Value: {password}")
    print(f"Password Score: {result['score']}/4")
    print(
        "Crack Time:",
        result['crack_times_display']['offline_fast_hashing_1e10_per_second']
    )
    print("Feedback:", result['feedback']['suggestions'])
    print()
