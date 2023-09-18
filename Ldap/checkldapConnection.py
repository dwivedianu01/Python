import ldap3 as ldap

SERVER_NAME = 'ldap://host:389'
DN = 'uid='
USERNAME = 'user'
PASSWORD = 'password'

server = ldap.Server(SERVER_NAME)
connection = ldap.Connection(server, user='{}\\{}'.format(DN, USERNAME), password=PASSWORD)
connection.open()
if connection.bind():
    print('Authenticated!')
else:
    print('Not Authenticated')
    print(connection.result)
