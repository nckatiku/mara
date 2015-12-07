"""
Talker-style communication and commands
"""
from mara import util

from .core import service
from .users import User

# Add command handler
from mara.contrib.commands import CommandRegistry
commands = CommandRegistry(service)

#
# Built-in commands
#

# Register standard built-in commands
from mara.contrib.commands import register_cmds as cmds_register_cmds
cmds_register_cmds(commands, admin=True)

# Add user commands
from mara.contrib.users import register_cmds as users_register_cmds
users_register_cmds(commands)

# Add user extensions
from mara.contrib.users.gender import cmd_gender
commands.register('gender', cmd_gender)

from mara.contrib.users.password import ChangePasswordHandler
commands.register('password', ChangePasswordHandler())

from mara.contrib.users.admin import register_cmds as admin_register_cmds
admin_register_cmds(commands)

# Add social commands
from mara.contrib.commands.socials import gen_social_cmds
gen_social_cmds(service, commands, User)

