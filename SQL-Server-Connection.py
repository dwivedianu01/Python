import pyodbc 
cnxn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                      "Server=<server>,<port>;"
                      "Database=<DB>;"
                      "UID=<user>;"
                      "PWD=<password>;"
                      "Trusted_Connection=no;")


records = cnxn.cursor()
print(records)
records.execute('SELECT * FROM [[dbo].[TABLE]]')

print("Printing each row")

# df = pd.DataFrame(records)
# for key, value in df.iteritems():
#     print(key, value)
#     print()

for row in records:
    print('row = %r' % (row,))

#df = pd.DataFrame(records)
#print(df)
