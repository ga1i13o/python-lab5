import pymysql


def insert(task):
    conn = pymysql.connect(user="utente", password="piru",
                            host="localhost", database="tasklist")

    insert_t = "insert into task(todo) values(%s);"
    cursor = conn.cursor()
    cursor.execute(insert_t, (task, ))
    conn.commit()
    cursor.close()
    conn.close()


def remove(id):
    conn = pymysql.connect(user="utente", password="piru",
                            host="localhost", database="tasklist")

    delete_one = "delete from task where id_task=%s;"
    cursor = conn.cursor()
    cursor.execute(delete_one, (id,))
    conn.commit()
    cursor.close()
    conn.close()


def retrieve():
    conn = pymysql.connect(user="utente", password="piru",
                            host="localhost", database="tasklist")
    select_all = "select *\nfrom task\norder by todo;"

    cursor = conn.cursor()
    cursor.execute(select_all)
    ris = cursor.fetchall()
    cursor.close()
    conn.close()

    return ris
