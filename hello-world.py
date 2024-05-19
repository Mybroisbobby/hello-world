import argparse

def greet(name: str) -> str:
    return f"Hello, {name}!"

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Greet someone.")
    parser.add_argument('name', type=str, help='Name of the person to greet')
    args = parser.parse_args()

    print(greet(args.name))
