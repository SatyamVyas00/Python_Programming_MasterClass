import sqlite3

db = sqlite3.connect("contacts.sqlite")

update_sql = "update contacts set email = 'updated@mail.com' where contacts.phone = 1234"
update_cursor = db.cursor()
update_cursor.execute(update_sql)
print("{} rows updated".format(update_cursor.rowcount))

print()
print("Are connections the same: {}".format(update_cursor.connection == db))
print()

update_cursor.connection.commit()
update_cursor.close()

for name, phone, email in db.execute("select * from contacts"):
    print(name)
    print(phone)
    print(email)
    print("-"*20)

db.close()
