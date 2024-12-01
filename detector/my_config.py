from config import Config

class my_Config(Config):


    """Configuration for training on the TACO dataset using SmartCycle."""
    NAME = "SmartCycle"

    NUM_CLASSES = 61  # 60 classes + 1 background

    def __init__(self):
        """Initialize additional computed attributes or properties if needed."""
        super().__init__()  # Call the parent class constructor
        
if __name__ == "__main__":
    my_config = my_Config()
    my_config.display()        