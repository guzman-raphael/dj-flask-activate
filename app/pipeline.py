import datajoint as dj

schema = dj.Schema()

@schema
class Student(dj.Lookup):
    definition = """
    id: int
    """

    def message(self):
        return f"Hi, I am {self.full_table_name}"