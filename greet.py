import argparse


def greet(name: str) -> str:
    return f"Hello, {name}!"


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Greet a user by name.")
    parser.add_argument("--name", required=True, help="Name to greet")
    args = parser.parse_args()
    print(greet(args.name))
