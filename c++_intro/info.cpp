// #include <iostream>
// #include <fstream>
// // #include <ifstream>
// // #include <ofstream>


// int ipnum(int a, int b, std::string c);
// void mydoc(std::string nm);

// int main(){
//     int a = 10;
//     int b = 20;
//     std::string name = "Usman Musa";
//     // std::cout << "What is your name: ";
//     // getline(std::cin, name);
//     std::cout << "My name is " << name << std::endl;
//     ipnum(6, 9, "you");
//     return 0;
// }

// int ipnum(int a, int b, std::string c){
//     std::cout << a << std::endl;
//     std::cout << b << std::endl;
//     std::cout << c << std::endl;
//     return 0;
// }

// void mydoc(std::string nm){
//     std::cout << "Wow I created my file!";
//     std::ofstream MyFile("file.txt");
//     MyFile << "Lorem";
//     MyFile.close();
// }
#include <fstream>
#include <iostream>
using namespace std;

int main () {
    char data[100];

    // open a file in write mode.
    ofstream outfile;
    outfile.open("file.py");

    cout << "Writing to the file" << endl;
    cout << "Enter your name: "; 
    cin.getline(data, 100);

    // write inputted data into the file.
    outfile << data << endl;

    cout << "Enter your age: "; 
    cin >> data;
    cin.ignore();

    // again write inputted data into the file.
    outfile << data << endl;

    // close the opened file.
    outfile.close();

    // open a file in read mode.
    ifstream infile; 
    infile.open("file.py"); 

    cout << "Reading from the file" << endl; 
    infile >> data; 

    // write the data at the screen.
    cout << data << endl;

    // again read the data from the file and display it.
    infile >> data; 
    cout << data << endl; 

    // close the opened file.
    infile.close();
    return 0;
}
