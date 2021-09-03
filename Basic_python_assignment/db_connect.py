# from typing import Counter
import psycopg2

try:
    connection = psycopg2.connect(
        host = "localhost",
        database = "Leapfrog",
        user = "postgres",
        password = " ",
        port = 5432
    )
    cursor = connection.cursor()
    
    create_schema = '''CREATE SCHEMA IF NOT EXISTS python_db'''
    cursor.execute(create_schema)
    
# Using psycopg2 connect to a local database and create the following tables:
# Doctor (id, name, specialization (FK), phone_number)
# Patient (id, name, date_of_birth, gender)
# Appointment (id, doctor_id (FK), patient_id (FK), fee, diagnosis)
# Doctor Specialization (id, specialization_type)
    doctor_specialization_create_query = '''
        CREATE TABLE IF NOT EXISTS python_db.doctor_specialization(
        id SERIAL,
        specialization_type VARCHAR(100) NOT NULL,
        PRIMARY KEY(id)
        )'''
    cursor.execute(doctor_specialization_create_query)
    doctor_create_query = '''
        CREATE TABLE IF NOT EXISTS python_db.doctor(
        id SERIAL,
        name VARCHAR(100) NOT NULL,
        specialization INT NOT NULL,
        phone_number VARCHAR(10) NOT NULL, 
        PRIMARY KEY(id),
        FOREIGN KEY(specialization) REFERENCES python_db.doctor_specialization(id)
        )
        '''
    cursor.execute(doctor_create_query)

    patient_create_query = '''
        CREATE TABLE IF NOT EXISTS python_db.patient(
        id SERIAL,
        name VARCHAR(50) NOT NULL,
        date_of_birth DATE NOT NULL,
        gender VARCHAR(12) NOT NULL,
        PRIMARY KEY(id)
        )
    '''
    cursor.execute(patient_create_query)
    appointment_create_query = '''
        CREATE TABLE IF NOT EXISTS python_db.appointment(
        id SERIAL,
        doctor_id INT NOT NULL,
        patient_id INT NOT NULL,
        fee INT NOT NULL,
        diagnosis varchar(20),
        PRIMARY KEY(id),
        FOREIGN KEY(doctor_id) REFERENCES python_db.doctor(id),
        FOREIGN KEY(patient_id) REFERENCES python_db.patient(id)
        )
        '''
    cursor.execute(appointment_create_query)
    
    
    # INSERT the following data in the tables. Use both execute() and executemany() methods with parameter binding.
    doctor_specialization_ins_query = '''
        INSERT INTO python_db.doctor_specialization("specialization_type") 
        VALUES 
        ('Anaesthesiologist'),
        ('Surgeon'),
        ('Psychiatrist')
        '''
    # cursor.execute(doctor_specialization_ins_query)
    
    doctor_ins_query = '''
        INSERT INTO python_db.doctor("name", "specialization", "phone_number")
        VALUES
        (%s, %s, %s)
        '''
    doctor_data =[
        ('Lionel Smart', 1, '2811232323'),
        ('Michelle Sanders', 2, '1899912310'),
        ('Pretti Patel', 3, '1899912310'),
        ('Sadiq Khan', 1, '7983129813'),
        ('Chaz Smith', 2, '7983129813'),
        ]

    # cursor.executemany(doctor_ins_query, doctor_data)
    patient_ins_query = '''
        INSERT INTO python_db.patient("name", "date_of_birth", "gender")
        VALUES
        (%s, %s, %s)
        '''
    patient_data =[
        ('Jane Henderson', '1989-9-19', 'Female'),
        ('Alice Sprigg', '1991-11-12', 'Female'),
        ('Dave Carr', '1995-3-28', 'Male'),
        ('Morris Beckman', '2001-7-7', 'Male')
        ]

    # cursor.executemany(patient_ins_query, patient_data)
    
    appointment_ins_query = '''
        INSERT INTO python_db.appointment("doctor_id", "patient_id", "fee", "diagnosis")
        VALUES
        (%s, %s, %s, %s)
        '''
    appointment_data = [
        (1,2,1000,''),
        (1,4,1000,'Headache'),
        (4,3,2000,''),
        (2,1,1500,'Back Pain')
        ]  
    # cursor.executemany(appointment_ins_query, appointment_data) 
    
    def fetch_data(do_query):
        cursor.execute(do_query)
        rows = cursor.fetchall()
        while rows is not None:
            print(rows)
            rows = cursor.fetchone()
            
    # GET the count of patients born after 1990.
    search_dob_after_1990_query = '''
        SELECT * FROM python_db.patient 
        WHERE TO_CHAR(date_of_birth, 'YYYY') > '1990'
        '''
    fetch_data(search_dob_after_1990_query)
    
    # GET the appointments made with “Surgeon” specialized doctors.
    search_appoint_surgeon_query = '''
        SELECT specialization_type, name, phone_number, fee, diagnosis FROM ((python_db.doctor_specialization 
        LEFT JOIN python_db.doctor ON python_db.doctor_specialization.id = specialization)
		RIGHT JOIN python_db.appointment ON python_db.doctor.id = doctor_id ) WHERE specialization_type = 'Surgeon' 
        '''    
    fetch_data(search_appoint_surgeon_query)
    
    # UPDATE fees of appointments and reduce them by 25%.
    update_fee = '''
        UPDATE python_db.appointment 
        SET fee = python_db.appointment.fee * 0.25
        '''
    # cursor.execute(update_fee)
    
    # UPDATE phone_number of Chaz Smith to 1231292310.
    update_phone_num_query = '''
        UPDATE python_db.doctor
        SET phone_number = '1231292310' WHERE name = 'Chaz Smith'
        '''
    # cursor.execute(update_phone_num_query)
    
    # DELETE all doctors who are specialized as “Psychiatrist”.
    del_doc_query = '''
        DELETE FROM (python_db.doctor_specialization
        NATURAL JOIN python_db.doctor on python_db.doctor_specialization.id = specialization) 
        WHERE specializtion_type = 'Psychiastrist'
        '''
    cursor.execute(del_doc_query)
    connection.commit()

except Exception as e:
    print("A error has occured :", e)

finally:
    print("done")
    
    

DELETE FROM (SELECT * FROM python_db.doctor 
LEFT JOIN python_db.doctor_specialization ON
python_db.doctor.specialization = python_db.doctor_specialization.id) WHERE specialization_type = 'Psychiatrist'
		
    