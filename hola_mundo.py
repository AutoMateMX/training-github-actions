import os

def main():
    nombre = os.getenv("USERNAME")
    print(f"hola mundo, este es {nombre} desde GitHub Actions")

if __name__ == "__main__":
    main()