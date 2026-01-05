import os

def main():
    nombre = os.getenv("USERNAME")
    print("hello world, this is {nombre} from GitHub Actions")

if __name__ == "__main__":
    main()