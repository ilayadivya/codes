import psycopg2
import re
conn = psycopg2.connect(
   database="d2j31492v7dru4", user='dyxrywcbctaeqj', password='434aaba30f6435d2361a72ac0e7832b17409ddfa81f4b3802467ec81b790d0b2', host='ec2-54-208-139-247.compute-1.amazonaws.com', port= '5432'
)
# database="tabin", user='postgres', password='admin', host='ec2-54-208-139-247.compute-1.amazonaws.com', port= '5432'
cursor = conn.cursor()
def getbankByIfsc(id):
   #Executing an MYSQL function using the execute() method
   match = re.compile(r"['\"]")
   cursor.execute("SELECT * FROM public.branches where ifsc='{0}'".format( re.sub(match, '', id))+" LIMIT 1")

   # Fetch a single row using fetchone() method.
   result = cursor.fetchone();
   return result
   conn.commit()

   #Closing the connection
   conn.close()
def escape(cb):
    return re.sub(re.compile(r"['\"]"), '', cb)
def getbankBycity(city,bank_name):
   #Executing an MYSQL function using the execute() method
   #match = re.compile(r"['\"]")
   cursor.execute("SELECT * FROM public.branches where city='{0}' and bank_name like '{1}%'".format(escape(city.upper()),escape(bank_name.upper()))+" LIMIT 10")

   # Fetch a single row using fetchone() method.
   result = cursor.fetchall();
   return result
   conn.commit()

   #Closing the connection
   conn.close()

#getbankByIfsc('ABHY00"\'65002')
#getbankBycity('MUMBAI','ABHYUDAYA COOPERATIVE')