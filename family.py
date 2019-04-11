class Person():
    def __init__(self,name,gender):
        self.name= name
        self.gender = gender
        self.mother=None
        self.father=None
        self.children=[]
        self.spouse=None

    def get_mother(self):
        return self.mother

    def get_children(self,gender):
        daughters,sons =[],[]
        for child in self.children:
            if child.gender=="F":
                daughters.append(child.name)
            else:
                sons.append(child.name)
        if gender=="F":
            return daughters
        return sons

    def get_uncle(self,relationship,gender):
        father_node =  self.father
        mother_node =  self.mother
        parent = father_node if relationship=="paternal" else mother_node
        parent_mother= parent.mother
        uncle,aunt=[],[]
        for child in parent_mother.children:
            if child.gender=="M":
                uncle.append(child.name)
            else:
                aunt.append(child.name)
        if gender=="F":
            return aunt
        return uncle


class Family():
    def __init__(self,queen_name,king_name):
        queen=Person(queen_name,"F")
        queen.spouse=Person(king_name,"M")
        self.root=queen
        self.hashmap_name_node={}
        self.hashmap_name_node[queen.name]=self.root

    def is_present(self,name):
        if name not in self.hashmap_name_node:
            print("PERSON_NOT_FOUND")
            return False
        return True

    def add_spouse_to_person(self,spouse_name,person_name,gender):
        spouse_node=self.hashmap_name_node[spouse_name]
        if spouse_node.gender==gender:
            print("ERROR: Spouse can not be of same gender")
            print("SPOUSE_NOT_ADDED",spouse_name,person_name,gender)
            return
        person =  Person(person_name,gender)
        person.spouse=spouse_node
        person.children=spouse_node.children
        spouse_node.spouse=person
        self.hashmap_name_node[person_name]=person
        print("SPOUSE_ADDITION_SUCCEEDED")


    def add_children(self, mother_name, children):
        if mother_name not in self.hashmap_name_node:
            print("PERSON_NOT_FOUND")
            return
        parent_node = self.hashmap_name_node[mother_name]
        if parent_node.gender=="M":
            print ("CHILD_ADDITION_FAILED")
            return

        mother_node=parent_node
        for child in children:
            child_node =  Person(child[0],child[1])
            mother_node.children.append(child_node)
            child_node.mother=mother_node
            child_node.father=mother_node.spouse
            self.hashmap_name_node[child[0]]=child_node
            print ("CHILD_ADDITION_SUCCEEDED")
        #print (self.hashmap_name_node)

    def get_siblings(self,person_name):
        person_node= self.hashmap_name_node[person_name]
        mother_node = person_node.mother
        siblings=[]
        for child in mother_node.children:
            if child.name != person_name:
                siblings.append(child)
                #print(child.name)
        siblings_names=[sibling.name for sibling in siblings]
        if siblings_names:
            print(siblings_names)
        else:
            print ("NONE")
        return siblings

    def find_sons(self,name):
        if name not in self.hashmap_name_node:
            print("PERSON_NOT_FOUND")
            return
        person_node=self.hashmap_name_node[name]
        print(person_node.get_children("M"))

    def find_daughters(self,name):
        if self.is_present(name):
            person_node=self.hashmap_name_node[name]
            print(person_node.get_children("F"))
        return

    def find_parental_side(self,name,gender):
        if self.is_present(name):
            person_node=self.hashmap_name_node[name]
            father_name = person_node.father.name
            siblings = self.get_siblings(father_name)
            parental_aunt, parental_uncle = [], []
            for sibling in siblings:
                if sibling.name != name and sibling.gender == "F":
                    parental_aunt.append(sibling.name)
                if sibling.name != name and sibling.gender == "M":
                    parental_uncle.append(sibling.name)
            if gender == "F":
                return parental_aunt
            return parental_uncle
        return

    def find_maternal_side(self,name,gender):
        if self.is_present(name):
            person_node=self.hashmap_name_node[name]
            mother_name = person_node.mother.name
            siblings= self.get_siblings(mother_name)
            maternal_aunt, maternal_uncle=[],[]
            for sibling in siblings:
                if sibling.name != name and sibling.gender=="F":
                    maternal_aunt.append(sibling.name)
                if sibling.name != name and sibling.gender == "M":
                    maternal_uncle.append(sibling.name)
            if gender=="F":
                return maternal_aunt
            return maternal_uncle
        return


root = Family("Anga","Shan")
root.add_children("Anga",[("Ish","M"),("Chit","M"),("Vich","M"),("Aras","M"),("Satya","F")])
root.add_spouse_to_person("Chit","Amba","F")
root.add_spouse_to_person("Vich","Lika","F")
root.add_spouse_to_person("Aras","Chitra","F")
root.add_spouse_to_person("Satya","Vyan","M")
root.add_children("Amba",[("Dritha","F"),("Tritha","F"),("Viratha","M")])
root.add_children("Lika",[("Vila","F"),("Chika","F")])
root.add_children("Chitra",[("Jnki","F"),("Ahit","M")])
root.add_children("Satya",[("Asva","M"),("Vyas","M"),("Atya","F")])
root.add_spouse_to_person("Dritha","Jaya","M")
root.add_spouse_to_person("Jnki","Arit","M")
root.add_spouse_to_person("Asva","Satvy","F")
root.add_spouse_to_person("Vich","Lika","F")
root.add_spouse_to_person("Aras","Chitra","F")
root.add_spouse_to_person("Vyas","Krpi","F")
root.add_children("Dritha",[("Yodhan","M")])
root.add_children("Jnki",[("Laki","M"),("Lavnya","F")])
root.add_children("Satvy",[("Vasa","M")])
root.add_children("Krpi",[("Kriya","M"),("Krithi","F")])
root.find_daughters("Anga")
root.find_sons("Anga")
#
# ADD_CHILD Chitra Aria Female
# GET_RELATIONSHIP Lavnya Maternal-Aunt
# GET_RELATIONSHIP Aria Siblings

root.add_children("Chitra",[("Aria","F")])
#root.find_maternal_aunt("Lavnya")
#root.find_daughters("Chitra")
root.get_siblings("Vasa")
#
# ADD_CHILD Pjali Srutak Male
# GET_RELATIONSHIP Pjali Son
root.add_children("Pjali",[("Srutak","M")])
root.find_sons("Pjali")
root.add_children("Asva",[("Srutak","M")])

#root = person.get_root(queen,king)

