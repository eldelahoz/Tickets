import sqlite3
from sqlite3 import Error

def dbticket_connection():
    """
    The function create the connection to the database

    Returns:
        con: The object connetion database
    """

    try:
        con = sqlite3.connect('dbtickets.db')
        return con
    except Error:
        print(Error)

def sql_table_show(table):
    """
    The function show all data in the tables
    """

    cursorObj = dbticket_connection().cursor()
    cursorObj.execute(f"SELECT * FROM {table} ORDER BY Nombre")
    rows = cursorObj.fetchall()
    return rows

# Add ticket item
# //////////////////////////////////////
def tableTicketsAdd(Prioridad, Descripcion, AbiertoDia, Informado):
    """
    The function add in the ticket table
    """

    con = dbticket_connection()
    cursorObj = con.cursor()

    try:
        cursorObj.execute("INSERT INTO tickets (Estado, Prioridad, Descripcion, AbiertoDia, Informado) VALUES(?, ?, ?, ?, ?)", ('Abierto', Prioridad, Descripcion, AbiertoDia, Informado))
        return con.commit()
    except:
        return 0
    

def showLastTicket():
    """
    The function show number the last ticket
    """

    cursorObj = dbticket_connection().cursor()
    cursorObj.execute("SELECT Noticket FROM tickets ORDER BY Noticket DESC LIMIT 1")
    rows = cursorObj.fetchall()

    if not rows:
        return (0)
    else:
        return(rows[0][0])

def showUsersNoms():
    """
    The function return list in the name users
    Returns:
        rows: A list with the users names
    """

    cursorObj = dbticket_connection().cursor()
    cursorObj.execute("SELECT Nombre FROM Users")
    rows = cursorObj.fetchall()

    return rows

def tableTickets():
    """
    The function retur all data in the table tickets
    Returns:
        rows: List all data tickets
    """
    cursorObj = dbticket_connection().cursor()
    cursorObj.execute("SELECT * FROM tickets")
    rows = cursorObj.fetchall()

    return rows

def tableUsersWrite(Cedula, Nombre, Usuario, Equipo, Ext):
    """
    The function write in the ticket Users
    """

    con = dbticket_connection()
    cursorObj = con.cursor()

    try:
        cursorObj.execute("INSERT INTO Users (Cedula, Nombre, Usuario, Equipo, Ext) VALUES(?, ?, ?, ?, ?)", (Cedula, Nombre, Usuario, Equipo, Ext))
        return con.commit()
    except:
        return 0

def tableResueltoWrite(Noticket, DescripResuelto, CerradoDia):
    """
    The function write in the ticket Resuelto
    """

    con = dbticket_connection()
    cursorObj = con.cursor()

    try:
        cursorObj.execute("INSERT INTO resueltos (Noticket, DescripResuelto) VALUES(?, ?)", (Noticket, DescripResuelto))
        cursorObj.execute("UPDATE tickets SET Estado=?, CerradoDia=?, Resuelto=? WHERE Noticket=?", ('Cerrado', CerradoDia, 'Si', Noticket))
        return con.commit()
    except:
        return 0

def showCountUser():
    con = dbticket_connection()
    cursorObj = con.cursor()

    try:
        cursorObj = dbticket_connection().cursor()
        cursorObj.execute("SELECT COUNT(*) FROM Users")
        rows = cursorObj.fetchall()
        return rows[0][0]
    except:
        return 0

