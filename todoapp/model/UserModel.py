import pymysql

def addUser(request, mysql):
  try:		
    sql = "INSERT INTO tb_user(usr_name, usr_cpf, usr_email, usr_password) VALUES(%s, %s, %s, %s)"
    data = (
      request.json['usr_name'],
      request.json['usr_cpf'],
      request.json['usr_email'],
      request.json['usr_password']
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
    
def findByName(name, mysql):
  try:
    sql = "SELECT * FROM tb_user WHERE usr_name = %s"
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    cursor.execute(sql, name)
    rows = cursor.fetchall()
    return rows
  except Exception as e:
    print(e)
  finally:
    cursor.close()
    conn.close()

def valideteLogin(email, password, mysql):
  try:
    sql = "SELECT usr_email, usr_password, usr_id FROM tb_user WHERE usr_email = %s"
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    cursor.execute(sql, email)
    rows = cursor.fetchall()

    if (email == rows[0]['usr_email'] and password == rows[0]['usr_password']):
      return rows
    else:
      return None

  except Exception as e:
    print(e)
  finally:
    cursor.close()
    conn.close()
    