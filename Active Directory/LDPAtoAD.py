from ldap3 import Server, Connection, ALL, NTLM

# Define the AD server and port
server = Server('your_ad_server', get_info=ALL)

# Define the connection
conn = Connection(server, user='your_domain\\your_username', password='your_password', authentication=NTLM)

# Bind to the server
if not conn.bind():
    print('Error in bind:', conn.result)
else:
    print('Bind successful')

    # Define the search parameters
    search_base = 'dc=your_domain,dc=com'
    search_filter = '(sAMAccountName=your_username)'
    search_attributes = ['cn', 'givenName', 'sn']

    # Perform the search
    conn.search(search_base, search_filter, attributes=search_attributes)

    # Process the search results
    for entry in conn.entries:
        print(entry)

    # Close the connection
    conn.unbind()
