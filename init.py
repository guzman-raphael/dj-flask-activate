import datajoint as dj

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
