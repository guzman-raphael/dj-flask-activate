import datajoint as dj
import os

conn = dj.conn(host=os.getenv("DJ_ROOT_HOST"),
               user=os.getenv("DJ_ROOT_USER"),
               password=os.getenv("DJ_ROOT_PASS"),
               reset=True)

raphael_schema = dj.Schema("raphael_university")

@raphael_schema
class Student(dj.Lookup):
    definition = """
    id: int
    """
    contents = [(1,)]

drew_schema = dj.Schema("drew_university")

@drew_schema
class Student(dj.Lookup):
    definition = """
    id: int
    """
    contents = [(100,)]

conn.query("CREATE USER 'raphael'@'%%' IDENTIFIED BY 'raphael';")
conn.query("GRANT SELECT ON `raphael_university`.`#student` TO 'raphael'@'%%';")

conn.query("CREATE USER 'drew'@'%%' IDENTIFIED BY 'drew';")
conn.query("GRANT SELECT ON `drew_university`.`#student` TO 'drew'@'%%';")