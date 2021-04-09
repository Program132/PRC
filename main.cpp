#include <iostream>
#include <string>
#include <vector>
#include <fstream>
#include <sstream>
#include <unordered_map>
#include <iterator>
#include <string_view>

#include "include/printing.hpp" 

std::unordered_map<std::string, std::string> variables{};
using namespace N;

int main()
{
    Printing dPrint;

    std::ifstream myFile {"main.prc"};

    std::string lignes;

    while (std::getline(myFile, lignes))
    {
        std::string cc;


        std::istringstream iss(lignes);
        std::vector<std::string> tab((std::istream_iterator<std::string>(iss)), std::istream_iterator<std::string>());

        if (tab[0] == "print")
        {
            for (int i = 1; i < tab.size(); i++)
            {
                cc += tab[i];
                cc += ' ';
            }

            dPrint.doprint(cc);
        }
    }

    return 0;
}