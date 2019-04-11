

class Expense:
    id=0
    def __init__(self,user,user_list,group,amount):
        self.added_by=user
        self.involved_users=user_list
        self.group = group
        self.amount=amount
        self.id=Expense.id+1
        Expense.id +=1


class User:
    id=0
    def __init__(self,name):
        self.name=name
        self.id = User.id+1
        self.group=None
        self.balance = 0
        self.transaction=[]
        self.expense=[]
        self.credit_list=[]
        self.debit_list=[]
        User.id +=1

    def add_expense(self,group,user_list,amount):
        group_id = group.id
        for user in user_list:
            if user.group.id != group_id:
                print("All users need to be from same group")
                return
        individual=amount/len(user_list)
        self.balance += amount-individual
        for user in user_list:
            print (user.id,user.name)
            user.balance -= individual
        self.expense=Expense(self,user_list,group,amount)

    def make_transaction(self,user,type,amount):
        if type=="credit":
            self.balance -= amount
            user.balance += amount
            if user.id in self.credit_list:
                pass

class Group:
    id=0
    def __init__(self,name):
        self.name=name
        self.id=Group.id+1
        self.users=[]
        Group.id+=1


    def add_user(self,users):
        for user in users:
            if user.id not in self.users:
                self.users.append(user)
                user.group=self
            else:
                print("this user already present")

    def display(self):
        print("group")
        for user in self.users:
            print ("{} has balance of {}".format(user.name,user.balance))



class Transaction:
    id=0
    def __init__(self,user1,user2,amount,group):
        if user1.group.id==user2.group.id:
            pass


user1=User("rahul")
user2=User("vikas")
user3=User("sagar")
user4=User("piyush")
user5=User("anshul")
user6=User("pushpi")
user7=User("tushar")
group1 = Group("JainHeights")
group2 = Group("Sriven")
group1.add_user([user1,user2,user3,user4,user5])
group2.add_user([user4,user6,user1,user7])
group1.display()
group2.display()
user1.add_expense(group1,[user2,user3],90)
group1.display()


