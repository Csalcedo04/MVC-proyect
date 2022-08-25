import json


class Person(object):
    """
    Class used to represent an Person
    """

    def __init__(self, id_person: int, name: str = 'Name', last_name: str = "LastName"):
        """ Person constructor object.

        :param id_person: id of person.
        :type id_person: int
        :param name: name of person.
        :type name: str
        :param last_name: last name of person.
        :type last_name: str
        :returns: Person object
        :rtype: object
        """
        self._id_person = id_person
        self._name = name
        self._last_name = last_name

    def to_dict(self):
        """
                    The Avro Python library does not support code generation.
                    For this reason we must provide a dict representation of our class for serialization.
                """
        return {
            "id_person": self._id_person,
            "name": self._name,
            "last_name": self._last_name
        }

    @property
    def id_person(self) -> int:
        """ Returns id person of the person.
          :returns: id of person.
          :rtype: int
        """
        return self._id_person

    @id_person.setter
    def id_person(self, id_person: int):
        """ The id of the person.
        :param id_person: id of person.
        :type: int
        """
        self._id_person = id_person

    @property
    def name(self) -> str:
        """ Returns the name of the person.
          :returns: name of person.
          :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """ The name of the person.
        :param name: name of person.
        :type: str
        """
        self._name = name

    @property
    def last_name(self) -> str:
        """ Returns the last name of the person.
          :returns: last name of person.
          :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name: str):
        """ The last name of the person.
        :param last_name: last name of person.
        :type: str
        """
        self._last_name = last_name

    def __str__(self):
        """ Returns str of person.
          :returns: sting person
          :rtype: str
        """
        return '({0}, {1}, {2})'.format(self.id_person, self.name, self.last_name)


class PersonEncoder(json.JSONEncoder):
    """
       class used to serialize the class Person to Json diccionary str
       """
    def default(self, o):
        """

        :param o: Person: object
        :return: serialize json dictionary data
        """
        if isinstance(o, Person):
            return {'id_person': o.id_person, 'name': o.name, 'last_name': o.last_name}
        return super().default(o)


if __name__ == '__main__':
    edwin = Person(id_person=73577376, name="Edwin", last_name="Puertas")
    edwin.name = "Edwin. A"
    jsFile = json.dumps(edwin, cls=PersonEncoder, indent= 4)
    print(jsFile)
    print(edwin)

