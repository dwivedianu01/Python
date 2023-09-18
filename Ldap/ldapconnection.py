import ldap3

# LDAP server details
ldap_server = 'ldap://host:389'
ldap_user = 'user'
ldap_password = 'password'
base_dn = 'O=x.dhl.com'  # Change this to the base DN of your LDAP server
search_filter = '(uid=ramsing)'  # Modify the filter as needed

# Establish an LDAP connection
server = ldap3.Server(ldap_server, get_info=ldap3.ALL)

# Bind to the LDAP server with credentials
conn = ldap3.Connection(server, user=ldap_user, password=ldap_password, auto_bind=True)

# Perform the LDAP search
conn.search(
    search_base=base_dn,
    search_filter=search_filter,
    attributes=ldap3.ALL_ATTRIBUTES  # Fetch all attributes of the found user
)

# Check if any entries were found
if conn.entries:
    for entry in conn.entries:
        # Print the user's DN and attributes
        print(f'DN: {entry.entry_dn}')
        for attribute in entry:
            print(f'{attribute}: {entry[attribute].value}')
else:
    print('User not found in LDAP.')

# Close the LDAP connection
conn.unbind()
