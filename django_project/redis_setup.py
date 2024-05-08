import redis

from django_project.environment_variables import EnvironmentVariables

redis_instance = redis.StrictRedis(host=EnvironmentVariables.REDIS['host'],
                                   port=EnvironmentVariables.REDIS['port'],
                                   db=EnvironmentVariables.REDIS['db'],
                                   password=EnvironmentVariables.REDIS['password'])
