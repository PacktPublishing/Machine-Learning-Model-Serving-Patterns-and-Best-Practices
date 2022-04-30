class DbConnection(object):

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            print("Creating database connection")
            cls.instance = super(DbConnection, cls).__new__(cls)
            return cls.instance
        else:
            print("Connection is already established!")
            return cls.instance


if __name__=="__main__":
    con1 = DbConnection()
    con2 = DbConnection()
    con3 = DbConnection()