class iNeuron:
    def __init__(self):
        self.__students1 = "data science"
    
    def students(self):
        print(self.__students1)
    
    def change_new(self, new_value):
        self.__students1 = new_value

# Instantiate the class
i = iNeuron()

# Call the students() method
i.students() # Output: "data science"

# Update the value of __students1 using the change_new() method
i.change_new("value changed")

# Call the students() method again to see the updated value
i.students()
#modification