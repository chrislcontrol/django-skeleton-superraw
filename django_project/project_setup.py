import os


class ProjectSetup:
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    ABSOLUT_PATH = os.getcwd()
    PROJECT_FOLDER = os.path.split(BASE_DIR)[-1]
