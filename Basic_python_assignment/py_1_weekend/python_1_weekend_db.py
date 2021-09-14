import psycopg2

try:
    connection = psycopg2.connect(
        host = "127.0.0.1",
        database = "Leapfrog",
        user = "postgres",
        password = " ",
        port = 5432
    )
    cursor = connection.cursor()
    
    create_schema = '''create schema py_weekend'''
    cursor.execute(create_schema)
    
    
    create_user = '''
                    CREATE TABLE IF NOT EXISTS py_weekend.users
                    (id SERIAL,
                    name VARCHAR(50),
                    DOB DATE,
                    profession VARCHAR(50),
                    PRIMARY KEY(id));
                    '''
    cursor.execute(create_user)
    
    create_address = '''
                    CREATE TABLE IF NOT EXISTS py_weekend.address
                    (id SERIAL,
                    permanent_address VARCHAR(50),
					temporary_address VARCHAR(50),
                    PRIMARY KEY(id),
					FOREIGN KEY(id) REFERENCES py_weekend.users(id)
					);
                    '''
    cursor.execute(create_address)
    
    user_ins = '''
                INSERT INTO py_weekend.users ("name", DOB, "profession") VALUES
                ('xyz', '2055-03-25', 'yze'),
                ('xyza', '2054-03-15', 'yfaee'),
                ('xfaeyz', '2030-03-25', 'faeyze')
                '''
    cursor.execute(user_ins)
    
    address_ins = '''
                INSERT INTO py_weekend.address ("permanent_address", "temporary_address") VALUES
                ('abc', 'abc'),
                ('abcfaewf', 'afae'),
                ('abafec', 'abcfaewfd')
                '''
    cursor.execute(address_ins)

    display = '''
                select * from py_weekend.users inner join py_weekend.address on py_weekend.address.id = py_weekend.users.id
                '''
    cursor.execute(display)
    
    display1 = '''
                select py_weekend.users.id from py_weekend.users inner join py_weekend.address on py_weekend.address.id = py_weekend.users.id
                '''
    cursor.execute(display1)
    
    display2 = '''
                select py_weekend.users.profession, py_weekend.address.permanent_address from py_weekend.users inner join py_weekend.address on py_weekend.address.id = py_weekend.users.id
                '''
    cursor.execute(display2)
    
    add_col = '''
                alter table py_weekend.users add Age int
                '''   
    cursor.execute(add_col)

    update_age = '''update py_weekend.users set Age = '25' where py_weekend.users.id = 1'''
    cursor.execute(update_age)
    
    update_age1 = '''update py_weekend.users set Age = '19' where py_weekend.users.id = 2'''
    cursor.execute(update_age1)
    
    update_age2 = '''update py_weekend.users set Age = '30' where py_weekend.users.id = 3'''
    cursor.execute(update_age2)
    connection.commit()
except Exception as e:
    print("A error has occured :", e)
    
finally:
    print("done")
