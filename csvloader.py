import csv
import MySQLdb
import re

# Connect to MySQL
mydb = MySQLdb.connect(
	host='localhost', 
	user='root',
    passwd='test1234',
    db='mydb')
cursor = mydb.cursor()
csv_data = csv.reader(file('Vendor.csv'))

# Rgular exps
zipreg = re.compile('././.{4} .{2}:.{2}')
s = 'x/x/xxxx xx:xx'

# Check duplicate VendorNum, RefNum and Name
check_dict = {}

# Generate Queries
for row in csv_data:

	# Vendor Object
	VendorNum = row[1]
	prev = check_dict.get(VendorNum)
	if prev is None:
		check_dict[VendorNum] = 0
	else:
		check_dict[VendorNum] = prev + 1
		VendorNum = VendorNum + '_' + str(prev)	
	RefNum = None	
	Name = row[2]
	prev = check_dict.get(Name)
	if prev is None:
		check_dict[Name] = 0
	else:
		check_dict[Name] = prev + 1
		Name = Name + '_' + str(prev)	
	Description = row[3]
	Default_VendorAddress_id = 1
	Default_VendorContact_id = 1
	CreditStatus = ""
	vendor_data = (
		VendorNum, 
		RefNum, 
		Name, 
		Description, 
		CreditStatus,
		False,
		False
	)
	cursor.execute("INSERT INTO Vendor(VendorNum, RefNum, Name, Description, CreditStatus, IsActive, IsDeleted) VALUES(%s, %s, %s, %s, %s, %s, %s);", vendor_data ) 
	vendor_id = cursor.lastrowid

	# Vendor_Address Object
	AddressName = "Main"
	Street = row[6]
	State = row[5]
	City = row[4]
	Zip = row[7]
	ShippingAddress_data = (
		AddressName,
		State,
		City,
		Street,
		Zip,
		vendor_id,
		"ShippingAddress",
		False,
		False		
		)
	BillingAddress_data = (
		AddressName,
		State,
		City,
		Street,
		Zip,
		vendor_id,
		"BillingAddress",
		False,
		False		
		)
	MailingAddress_data = (
		AddressName,
		State,
		City,
		Street,
		Zip,
		vendor_id,
		"MailingAddress",
		False,
		False		
		)
	cursor.execute('INSERT INTO Vendor_Address(Name, State, City, Street, Zip, Vendor_id_id, AddressType, IsDefault, IsDeleted) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s);', ShippingAddress_data) 
	cursor.execute('INSERT INTO Vendor_Address(Name, State, City, Street, Zip, Vendor_id_id, AddressType, IsDefault, IsDeleted) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s);', BillingAddress_data) 
	cursor.execute('INSERT INTO Vendor_Address(Name, State, City, Street, Zip, Vendor_id_id, AddressType, IsDefault, IsDeleted) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s);', MailingAddress_data) 	

	# Vendor_Contact Object
	FirstName = row[11]
	LastName = " "
	Position = row[12]
	Telephone = row[8]
	Cellphone = row[10]
	Fax = row[9]
	Email = row[13]
	Note = row[14]#Remark?
	ShippingContact_data = (
		FirstName,
		LastName,
		Position,
		Telephone,
		Cellphone,
		Fax,
		Email,
		Note,
		vendor_id,
		"ShippingContact",
		False,
		False			
		)
	BillingContact_data = (
		FirstName,
		LastName,
		Position,
		Telephone,
		Cellphone,
		Fax,
		Email,
		Note,
		vendor_id,
		"BillingContact",
		False,
		False			
		)
	MailingContact_data = (
		FirstName,
		LastName,
		Position,
		Telephone,
		Cellphone,
		Fax,
		Email,
		Note,
		vendor_id,
		"MailingContact",
		False,
		False			
		)
	cursor.execute('INSERT INTO Vendor_Contact(FirstName, LastName, Position, Telephone, Cellphone, Fax, Email, Note, Vendor_id_id, ContactType, IsDefault, IsDeleted) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);', ShippingContact_data) 	
	cursor.execute('INSERT INTO Vendor_Contact(FirstName, LastName, Position, Telephone, Cellphone, Fax, Email, Note, Vendor_id_id, ContactType, IsDefault, IsDeleted) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);', BillingContact_data) 
	cursor.execute('INSERT INTO Vendor_Contact(FirstName, LastName, Position, Telephone, Cellphone, Fax, Email, Note, Vendor_id_id, ContactType, IsDefault, IsDeleted) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);', MailingContact_data) 

# Close the connection to the database.
mydb.commit()
cursor.close()
print "Done"