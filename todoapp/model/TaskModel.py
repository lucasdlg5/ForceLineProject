import pymysql

def addTask(request, mysql):
  try:		
    sql = '''INSERT INTO tb_task(tsk_name, tsk_description, usr_id)
           VALUES(%s, %s, %s)'''
    data = (
      request.json['name'],
      request.json['description'],
      request.json['id']
    )
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(sql, data)
    conn.commit()
    return True
  except Exception as e:
    print(e)
  finally:
    cursor.close()
    conn.close()

def getAllTasks(id, mysql):
  try:
    sql = 'SELECT * FROM tb_task WHERE usr_id = %s'
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    cursor.execute(sql, id)
    rows = cursor.fetchall()
    return rows
  except Exception as e:
    print(e)
  finally:
    cursor.close()
    conn.close()

def removeTask(id, mysql):
  try:
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM tb_task WHERE tsk_id=%s', (id))
    conn.commit()
    return True
  except Exception as e:
    print(e)
  finally:
    cursor.close()
    conn.close()