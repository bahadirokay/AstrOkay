import sqlite3
import os

"""Database oluştur."""
def create_database():
    #Database ismi oluştur.
    db_file = "astrophotography.db"
    conn = sqlite3.connect(db_file)
    #Tablo ekleme işlemi
    c = conn.cursor()
    '''''LightFrame'''''
    c.execute("""
        CREATE TABLE IF NOT EXISTS LightFrame (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            filename TEXT NOT NULL,
            path TEXT NOT NULL,
            width INTEGER,
            height INTEGER
        );
    """)
    """"FlatFrame"""""
    c.execute("""
        CREATE TABLE IF NOT EXISTS FlatFrame (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            filename TEXT NOT NULL,
            path TEXT NOT NULL,
            width INTEGER,
            height INTEGER
        );
    """)
    """""DarkFrame"""
    c.execute("""
        CREATE TABLE IF NOT EXISTS DarkFrame (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            filename TEXT NOT NULL,
            path TEXT NOT NULL,
            width INTEGER,
            height INTEGER
        );
    """)
    """""DarkFlatFrame"""
    c.execute("""
        CREATE TABLE IF NOT EXISTS DarkFlatFrame (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            filename TEXT NOT NULL,
            path TEXT NOT NULL,
            width INTEGER,
            height INTEGER
        );
    """)
    """""BiasFrame"""
    c.execute("""
        CREATE TABLE IF NOT EXISTS BiasFrame (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            filename TEXT NOT NULL,
            path TEXT NOT NULL,
            width INTEGER,
            height INTEGER
        );
    """)
    """""MotherFrame"""
    c.execute("""
        CREATE TABLE IF NOT EXISTS MotherFrame (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            filename TEXT NOT NULL,
            path TEXT NOT NULL,
            width INTEGER,
            height INTEGER
        );
    """)
    """""MasterDarkFlatFrame"""
    c.execute("""
        CREATE TABLE IF NOT EXISTS MasterDarkFlatFrame (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            filename TEXT NOT NULL,
            path TEXT NOT NULL,
            width INTEGER,
            height INTEGER
        );
    """)
    """""MasterDarkFrame"""
    c.execute("""
        CREATE TABLE IF NOT EXISTS MasterDarkFrame (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            filename TEXT NOT NULL,
            path TEXT NOT NULL,
            width INTEGER,
            height INTEGER
        );
    """)
    """""MasterFlatFrame"""
    c.execute("""
        CREATE TABLE IF NOT EXISTS MasterFlatFrame (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            filename TEXT NOT NULL,
            path TEXT NOT NULL,
            width INTEGER,
            height INTEGER
        );
    """)
    """""BiasFrame"""
    c.execute("""
        CREATE TABLE IF NOT EXISTS BiasFrame (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            filename TEXT NOT NULL,
            path TEXT NOT NULL,
            width INTEGER,
            height INTEGER
        );
    """)
    """""MasterBiasFrame"""
    c.execute("""
        CREATE TABLE IF NOT EXISTS MasterBiasFrame (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            filename TEXT NOT NULL,
            path TEXT NOT NULL,
            width INTEGER,
            height INTEGER
        );
    """)
    #Tabloyu Kaydet
    conn.commit()
    #Veritabanını kapat
    conn.close()

def create_folder_database():
    #Database ismi oluştur.
    db_file = "foldername.db"
    conn = sqlite3.connect(db_file)
    #Tablo ekleme işlemi
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS FolderName (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            foldername TEXT NOT NULL,
            path TEXT NOT NULL
        );
    """)
    #Tabloyu Kaydet
    conn.commit()
    #Veritabanını kapat
    conn.close()

"""Database'ye veri ekleme"""
def add_data(table, data):
    #Database adını seç
    db_file = "astrophotography.db"
    #Database ile bağlantı kur
    with sqlite3.connect(db_file) as connection:
        cursor = connection.cursor()
        #create_database'de eklenen tablolara karışık gelen değer bilgilerini tıklanan butona göre iste.
        if table == 'FlatFrame':
            cursor.execute(
                "CREATE TABLE IF NOT EXISTS FlatFrame (filename TEXT, path TEXT, width INTEGER, height INTEGER)")
        elif table == "LightFrame":
            cursor.execute(
                "CREATE TABLE IF NOT EXISTS LightFrame (filename TEXT, path TEXT, width INTEGER, height INTEGER)")
        cursor.execute(f"INSERT INTO {table} (filename, path, width, height) VALUES (?, ?, ?, ?)", data)
        connection.commit()

def add_folder(table):
    #Database adını seç
    conn = sqlite3.connect('foldername.db')
    #Database ile bağlantı kur
    cursor = conn.cursor()
    if table == 'FolderName':
        cursor.execute("CREATE TABLE IF NOT EXISTS FolderName (foldername TEXT, path TEXT)")
    cursor.execute("CREATE TABLE IF NOT EXISTS FolderName (foldername TEXT, path TEXT)")
    conn.commit()


"""Veritabanındaki veriyi çağırma, gösterme ve kullanma işlemi"""
def get_data(table):
    db_file = "astrophotography.db"
    with sqlite3.connect(db_file) as connection:
        cursor = connection.cursor()
        #tablo seç
        cursor.execute(f"SELECT * FROM {table}")
        data = cursor.fetchall()
        #Burasıni kendim tabloyu görebilmek için yaptım.
        #Döndür
        for row in data:
            print(row)
        return data

def get_folder(table):
    db_file = "foldername.db"
    with sqlite3.connect(db_file) as connection:
        cursor = connection.cursor()
        #tablo seç
        cursor.execute(f"SELECT * FROM {table}")
        data = cursor.fetchall()
        #Burasıni kendim tabloyu görebilmek için yaptım.
        print(data)
        #Döndür


"""Database'yi komple sil."""
def delete_db():
    db_file = "astrophotography.db"
    connection = sqlite3.connect(db_file)
    cursor = connection.cursor()
    # Veritabanı bağlantısını kes
    connection.commit()
    connection.close()
    # Veritabanı dosyasını sil
    os.remove('astrophotography.db')

def delete_folder_db():
    db_file = "foldername.db"
    connection = sqlite3.connect(db_file)
    cursor = connection.cursor()
    # Veritabanı bağlantısını kes
    connection.commit()
    connection.close()
    # Veritabanı dosyasını sil
    os.remove('foldername.db')

"""Veri Tabanından sonradan girilen verileri sil"""
def delete_table(table):
    db_file = "astrophotography.db"
    with sqlite3.connect(db_file) as connection:
        cursor = connection.cursor()
        #Seçilen tablodaki sonradan girilen değeri sil.
        cursor.execute(f"DELETE FROM {table}")
        #Kaydet
        connection.commit()
        #Örnek; delete_table('FlatFrame')

def delete_folder_table(table):
    db_file = "foldername.db"
    with sqlite3.connect(db_file) as connection:
        cursor = connection.cursor()
        #Seçilen tablodaki sonradan girilen değeri sil.
        cursor.execute(f"DELETE FROM {table}")
        #Kaydet
        connection.commit()
        #Örnek; delete_table('FlatFrame')
