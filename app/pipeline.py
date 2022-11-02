import datajoint as dj

schema = dj.Schema()

@schema
class Student(dj.Lookup):
    definition = """
    id: int
    """