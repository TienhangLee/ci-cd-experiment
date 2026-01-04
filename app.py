def read_config():
    with open("config.txt") as f:
        return int(f.read().split("=")[1])

def run():
    value = read_config()
    result = 100 / value
    print("Result:", result)

if __name__ == "__main__":
    run()
