from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name
        self._next_id = 1
        self._members = []

    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        member["id"] = self._generateId()
        member["last_name"] = self.last_name
        self._members.append(member)
        return member

    def delete_member(self, id):
        for member in self._members:
            if member["id"] == id:
                self._members.remove(member)
                return {"done": True}
        return {"done": False}

    def get_member(self, id):
        for member in self._members:
            if member["id"] == id:
                return member
        return None

    # def update_member(self, id, member):
    #     for i, existing_member in enumerate(self._members):
    #         if existing_member["id"] == id:
    #             self._members[i] = {
    #                 "id": id,
    #                 "last_name": self.last_name,
    #                 "first_name": member["first_name"],
    #                 "age": member["age"],
    #                 "lucky_numbers": member["lucky_numbers"]
    #             }
    #             return {"done": True}
    #     return {"done": False}

    def get_all_members(self):
        return self._members
