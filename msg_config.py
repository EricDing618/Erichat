'''
A module for config server.

format:
    SIGNIN:@sign:<FCID/name> <pwd>
    QUIT:@quit:<name>
    SAY:@say:<name> <string>
    IS_SERVER:@ser:<type>
    IS_CLIENT:@cli:<FCID>
    ERROR:@err:<string>
'''
VERSION='0.1'
SIGNIN='@sign:'#setting.json,login_mode=true
QUIT='@quit'
SAY='@say:'
IS_SERVER='@ser:'
IS_CLIENT='@cli:'
ERROR='@err:'