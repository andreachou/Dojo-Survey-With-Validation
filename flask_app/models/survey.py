from flask import flash
from flask_app.config.mysqlconnection import connectToMySQL


class Dojo:
    my_db = "dojo_survey_schema"
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.location = data['location']
        self.language = data['language']
        self.comment = data['comment']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    @classmethod
    def save(cls, data):
        query = "INSERT INTO dojos(name, location, language, comment) VALUES (%(name)s, %(location)s, %(language)s, %(comment)s);"
        return connectToMySQL(cls.my_db).query_db(query, data)

    @classmethod
    def get_last_one(cls):
        query = "SELECT * FROM dojos ORDER by dojos.id DESC LIMIT 1;"
        result = connectToMySQL(cls.my_db).query_db(query)
        # Check to see if there were any results, if not, the email does not exist in the db
        if len(result) < 1:
            return False
        return cls(result[0])

    # Static methods don't have self or cls passed into the parameters.
    # We do need to take in a parameter to represent our dojo
    @staticmethod
    def validate_dojo(dojo):
        is_valid = True
        if len(dojo['name']) < 3:
            is_valid = False
            flash("Name must be at least 3 characters.")
        if len(dojo['location']) < 1:
            is_valid = False
            flash("Must choose a dojo location.")
        if len(dojo['language']) < 1:
            is_valid = False
            flash("Must choose a favorite language.")
        if len(dojo['comment']) < 3:
            is_valid = False
            flash("Comments must be at least 3 characters.")
        return is_valid
