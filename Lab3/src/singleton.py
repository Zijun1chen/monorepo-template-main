class Logger:
    _instance = None  # Private class variable to hold the single instance

<<<<<<< HEAD
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Logger, cls).__new__(cls)
            cls._instance.messages = [] 
            print("Logger created exactly once")
        else:
            print("Logger already created")
        return cls._instance
=======
    def __init__(self):
        self.messages = []

>>>>>>> c18438daf4a04b5b385bba5e8b3117d1947341a8
    def add_message(self, message):
        self.messages.append(message)


def main():
<<<<<<< HEAD
=======
    # Logger should only be initialized one time if it is properly
    # refactored as a singleton class
>>>>>>> c18438daf4a04b5b385bba5e8b3117d1947341a8
    for i in range(3):
        logger = Logger()
        logger.add_message(f"Adding message number: {i}")


if __name__ == "__main__":
<<<<<<< HEAD
    main()
=======
    main()
>>>>>>> c18438daf4a04b5b385bba5e8b3117d1947341a8
