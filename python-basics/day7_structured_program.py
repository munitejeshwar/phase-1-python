class Manager:
    def __init__(self, filename):
        self.filename = filename

    def load(self):
        pass

    def add(self, item):
        pass

    def save(self, data):
        pass


def main():
    manager = Manager("data.txt")
    data = manager.load()
    # menu logic here


if __name__ == "__main__":
    main()
