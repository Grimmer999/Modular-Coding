class Employee:
    # Constructor with parameters
    def __init__(self, id=123, salary=50000, designation="SDE"):
        self.id = id
        self.salary = salary
        self.designation = designation

    def travel(self,destination):
        print(f"Employee is now travelling to {destination}")

# Create an object with default values
sam = Employee(1234,10000000,"Data Science")
print(sam.id)
sam.travel("Kerala")