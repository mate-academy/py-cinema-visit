import os

REQUIRED_INIT_PATHS = [
    "app/__init__.py",
    "app/cinema/__init__.py",
    "app/people/__init__.py"
]

def create_init_files():
    for path in REQUIRED_INIT_PATHS:
        directory = os.path.dirname(path)
        os.makedirs(directory, exist_ok=True)
        if not os.path.exists(path):
            with open(path, "w") as f:
                f.write("# Automatically created __init__.py\n")
            print(f"✅ Created: {path}")
        else:
            print(f"ℹ️ Already exists: {path}")


if __name__ == "__main__":
    create_init_files()
