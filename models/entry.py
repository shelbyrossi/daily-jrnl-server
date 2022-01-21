class Entry():

    # Class initializer. It has 5 custom parameters, with the
    # special `self` parameter that every method on a class
    # needs as the first parameter.
    def __init__(self, id, subject, date, time_spent, moods_id):
        self.id = id
        self.subject = subject
        self.date = date
        self.time_spent = time_spent
        self.moods_id = moods_id
       
 