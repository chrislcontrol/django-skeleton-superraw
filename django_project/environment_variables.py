import os

from environ import Env

from django_project.project_setup import ProjectSetup


def _create_env() -> Env:
    env_instance = Env()
    dotenv = os.path.join(ProjectSetup.BASE_DIR, '../.env')
    if os.path.isfile(dotenv):
        env.read_env(dotenv)

    return env_instance


env = _create_env()


class EnvironmentVariables:
    # Database
    DATABASE_URL = env.db_url('DATABASE_URL', default="postgres://postgres:postgres@localhost:5432/postgres")

    # Cache
    REDIS = {
        'host': env.str('REDIS_HOST', '127.0.0.1'),
        'port': env.int('REDIS_PORT', 6379),
        'password': env.str('REDIS_PASSWORD', 'redis'),
        'db': env.str('REDIS_DB', 1)
    }
