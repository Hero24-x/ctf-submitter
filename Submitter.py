from core.utils import submit_flag

def load_flags(filename="flags.txt"):
    flags = []
    try:
        with open(filename, "r") as f:
            flags = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print(f"⚠️ Warning: '{filename}' file not found! Please create and add flags.")
    return flags

def main():
    print("🚀 CTF Submitter Started...\n")

    flags = load_flags()

    if not flags:
        print("⚠️ No flags found to submit. Exiting.")
        return

    for flag in flags:
        submit_flag(flag)

    print("\n🏁 Submission Completed.")

if __name__ == "__main__":
    main()
