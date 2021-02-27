import os
from fabric.api import run, env, cd, roles, local

def deploy(message: str):
    local("git add .")
    local('git commit -m "%s"' % message)
    local("heroku local")

def clear_migrations():
    local('find ./src/apps/*/migrations/*.py -not -name "__init__.py" -delete')
    local('find ./src/apps/*/migrations/__pycache__/*.pyc -not -name "*__init__*" -delete')
    local('sudo -u postgres psql -d musexplorer -f delete_all_tables.sql postgres')
