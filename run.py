from src import SimulationManager
from dotenv import load_dotenv, find_dotenv


if __name__ == "__main__":
    load_dotenv(find_dotenv())

    sm = SimulationManager()
    sm.run()
