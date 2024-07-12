
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name

        # example list of members
        self._members = []

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        new_menber={
            "id":self.generatedId(),
            "fisrt_name":member["name"],
            "last_name":self.last_name,
            "age":member["age"],
            "lucky_numbers":member.lucky_numbers
        }
        self._menbers.append(new_member)
        

    def delete_member(self, id):
        #Recorrido member in members  
        for family_member in self._members:
            if family_member["id"] == id:
                self._member.remove(family_member)
                return True
        
            return False

        

    def get_member(self, id):
        for index in range(len(self._menbers)):
            if self._menbers[index].id == id:
                memberSelected = self._members[index]
                return memberSelected
            else : return None
        

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members
