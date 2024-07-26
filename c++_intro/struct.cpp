// Structures (also called structs) are a way to group several related variables into one place. Each variable in the structure is known as a member of the structure.

// Unlike an array, a structure can contain many different data types (int, string, bool, etc.).

struct {             // Structure declaration
    int myNum;         // Member (int variable)
    string myString;   // Member (string variable)
} myStructure;       // Structure variable

// Assign values to members of myStructure
myStructure.myNum = 1;
myStructure.myString = "Hello World!";

// Print members of myStructure
cout << myStructure.myNum << "\n";
cout << myStructure.myString << "\n";
