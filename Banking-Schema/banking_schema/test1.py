 #!/usr/bin/python
# -*- coding: utf-8 -*-

import MySQLdb as mdb
import sys
import string
import random
db = mdb.connect('localhost', 'root','sahil', 'bank');

cursor = db.cursor()
'''
id_lno = list(xrange(1,1000000))
random.shuffle(id_lno)

id_ano = list(xrange(10000000, 100000000))
random.shuffle(id_ano)

'''

for i in range(0,1000):

	#	For Branch Insertion  	#
	 def id_bname(size=10, chars=string.ascii_lowercase):
	 	return ''.join(random.choice(chars) for x in range(size))
	 def id_bcity(size=3, chars=string.ascii_lowercase):
	 	return ''.join(random.choice(chars) for x in range(size))
	 def id_depname(size=2, chars=string.ascii_lowercase):
	 	return ''.join(random.choice(chars) for x in range(size))
	 def id_ename(size=2, chars=string.ascii_lowercase):
	 	return ''.join(random.choice(chars) for x in range(size))
	 def id_cname(size=2, chars=string.ascii_lowercase):
	 	return ''.join(random.choice(chars) for x in range(size))
	 def id_ccity(size=2, chars=string.ascii_lowercase):
	 	return ''.join(random.choice(chars) for x in range(size))
	 def id_cstreet(size=2, chars=string.ascii_lowercase):
	 	return ''.join(random.choice(chars) for x in range(size))
	 def id_ctype(size=2, chars=string.ascii_lowercase):
	 	return ''.join(random.choice(chars) for x in range(size))
	 		
	 id_assets = random.randint(1, 100)
	 bname = id_bname()
	 #	For Loan Insertion	#

	 id_lno = random.randint(100, 1000000)
	 
	 id_amount = random.randint(100, 500)
	 #	For account Insertion	#
	 id_ano = random.randrange(100, 1000000)
	 id_balance = random.randrange(0,100)
	 
	 #	Employee	Insertion	#
	 id_eid = random.randint(100, 100000)
	 id_start_date = random.randint(1, 100)
	 id_telnumber = random.randint(10, 100)
	 id_elength = random.randint(1, 100)
	 
	 #	Payment insertion		#
	 id_pno = random.randint(1, 1000000)
	 id_pdate = random.randint(1, 100)
	 id_pamount = random.randint(10, 100)
	 
	 #	Customer Insertion	#
	 id_cid = random.randint(1, 1000000)

	 #	Borrower Insertion	#
	 id_bdate = random.randint(10,100)
	 sql1 = " INSERT INTO branch(bname , bcity, assets)  VALUES ( '%s' , '%s', %d ) " %(bname , id_bcity() , id_assets)
	 
	 sql2 = " INSERT INTO account(ano , balance, bname)  VALUES ( %d , %d, '%s' ) " %(id_ano , id_balance , bname)	
	 
	 sql3 =  " INSERT INTO loan(lno , amount, bname)  VALUES ( %d , %d, '%s' ) " %(id_lno , id_amount , bname)
	 
	 sql4 =  " INSERT INTO employee(eid , depname, start_date,ename,telno,elength)  VALUES ( %d , '%s', %d,'%s', %d, %d ) " %(id_eid , id_depname() , id_start_date,id_ename(),id_telnumber,id_elength)	
	 
	 sql5 =  " INSERT INTO payment(pno , pamount, pay_date)  VALUES ( %d , %d, %d ) " %(id_pno , id_pamount , id_pdate)
	 
	 sql6 =  " INSERT INTO loan_payment(pno , lno)  VALUES ( %d , %d  ) " %(id_pno , id_lno)
	 
	 sql7 =  " INSERT INTO customer(cid , cstreet,ccity,ctype,cname,eid)  VALUES ( %d , '%s', '%s', '%s', '%s',%d ) " %(id_cid  , id_cstreet(),id_ccity(),id_ctype(),id_cname(),id_eid)	
	 
	 sql8 =  " INSERT INTO borrower(lno ,cid)  VALUES ( %d , %d ) " %(id_lno , id_cid )
	 
	 sql9 =  " INSERT INTO depositor(ano ,cid,access_date)  VALUES ( %d , %d, %d ) " %(id_ano , id_cid, id_bdate )
	  
#	 sql1 = str (sql)
#	 print sql1
	 try:
	 	cursor.execute(sql1)
	 	cursor.execute(sql2)
	 	cursor.execute(sql3)
	 	cursor.execute(sql4)
	 	cursor.execute(sql5)
	 	cursor.execute(sql6)
	 	cursor.execute(sql7)
	 	cursor.execute(sql8)
	 	cursor.execute(sql9)
	 	db.commit()
	 except:
		db.rollback()
		cursor.execute(sql1)
	 	cursor.execute(sql2)
	 	cursor.execute(sql3)
	 	cursor.execute(sql4)
	 	cursor.execute(sql5)
	 	cursor.execute(sql6)
	 	cursor.execute(sql7)
	 	cursor.execute(sql8)
	 	cursor.execute(sql9)
	 	
db.close()	


