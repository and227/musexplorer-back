import os
from fabric.api import run, env, cd, roles, local

def deploy(message: str):
    local("git add .")
    local('git commit -m "%s"' % message)
    local("heroku local")
