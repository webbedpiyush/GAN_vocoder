#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main(int argc, char *argv[])
{
    // Check if filename is provided as argument
    if (argc != 2)
    {
        cerr << "Usage: " << argv[0] << " <filename>" << endl;
        return 1;
    }

    // Concatenate filename with ".txt"
    string filepath = string(argv[1]) + ".txt";

    // Open the file
    ifstream file(filepath);

    // Check if the file is opened successfully
    if (!file.is_open())
    {
        cerr << "Error: Unable to open file." << endl;
        return 1;
    }

    // Read the file line by line
    string line, filecontent;
    int i = 0;
    while (getline(file, line))
    {
        filecontent += line;
    }

    // Close the file
    file.close();
    cout << "At the end, the final text is:\n " << filecontent << endl;

    return 0;
}
