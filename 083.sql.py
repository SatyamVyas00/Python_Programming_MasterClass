import sqlite3

db = sqlite3.connect("contacts.sqlite")
db.execute("CREATE TABLE if not exists contacts (name text, phone integer, email text)")
db.execute("insert into contacts(name, phone, email) values('SATYAM', 65387323, 'satyam@mail.com')")
db.execute("INSERT INTO contacts VALUES('Brian',  1234, 'brian@mail.com')")

cursor = db.cursor()
cursor.execute("select * from contacts")

#print(cursor.fetchall())

print(cursor.fetchone())
print(cursor.fetchone())
print(cursor.fetchone())

for name, phone, email in cursor:
    print(name)
    print(phone)
    print(email)
    print("-"*20)

cursor.close()
db.commit()
db.close()
