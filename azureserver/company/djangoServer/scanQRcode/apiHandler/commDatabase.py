#import MySQLdb
import traceback
from django.db import connections


class database():

    def __init__(self, database='default'):

        self.db = None
        try:
            self.connect_db(database)
        except:
            print("Errored while connecting to database")
            print("database: %s"%(self.db))
            #return False
        print("database: %s"%(self.db))

    def connect_db(self, database):
        """
        connect to the database

        param: db
        param: host
        param: user
        param password
        """

        self.db = connections[database]
        cursor = self.db.cursor()
        #cursor.execute('use %s'%(db))
        cursor.close()

    def create_tables(self, cmd):
        """
        create table in the database
        """

        cursor = self.db.cursor()
        cursor.execute(cmd)
        print("response: %s"%(cursor.fetchall()))
        cursor.close()

    def insert_data(self, cmd):
        """
        insert data into database
        """

        cursor = self.db.cursor()
        cursor.execute(cmd)
        self.db.commit()
        cursor.close()

    def get_raw_query(self, query):

        try:
            cursor = self.db.cursor()
            cursor.execute(query)
            data = cursor.fetchall()
            cursor.close()
            return data
        except:
            return False

    def get_id(self, Id, table, name, val):

        try:
            cursor = self.db.cursor()
            cmd = "select %s from %s where %s=%s"%(Id, table, name, val)
            print("cmd: "%cmd)
            cursor.execute(cmd)
            data = cursor.fetchall()
            cursor.close()
            return data[0][0]
        except:
            return False

    def get_data(self,name ,tableName,row,val):
        """
        :param tableName: Name of table
        :param row: Data to be fetch from row
        :return:
        """
        cursor = self.db.cursor()
        cmd = 'SELECT %s FROM  %s' %(name, tableName) +' WHERE %s="%s"'%(row,val)
        cursor.execute(cmd)
        data = cursor.fetchall()
        cursor.close()
        #print("data: %s"%data)
        return [row[0] for row in data]

    def check_interies(self, query):

        try:
            cursor = self.db.cursor()
            cursor.execute(query)
            data = cursor.fetchall()
            cursor.close()
            print("rowcount: %s"%cursor.rowcount)
            return cursor.rowcount
        except:
            print("exception : %s"%traceback.format_exc())
            return False

if __name__ == '__main__':
    db=database()
    #print(db.get_data('flag', 'company_qrcode', 'company_id', 1))
