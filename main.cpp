#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <fstream>
#include <sstream>
#include <unordered_map>
#include <iterator>

#include "include/printing.hpp" 
#include "include/ModPRC.hpp"

std::unordered_map<std::string, std::string> variables{};

int main()
{
    N::Printing dPrint;
    N::ModPRC ModPRC;

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

            dPrint.do_print(cc);
        }
        else if (tab[0] == "prc")
        {
            if (std::find(tab.begin(), tab.end(), "doc") != tab.end() || std::find(tab.begin(), tab.end(), "discord") != tab.end() || std::find(tab.begin(), tab.end(), "about") != tab.end()) 
            {
                if (tab[1] == "doc")
                {
                    ModPRC.prc_doc();
                }
                else if (tab[1] == "discord")
                {
                    ModPRC.prc_discord();
                }
                else if (tab[1] == "about")
                {
                    ModPRC.prc_about();
                }
                else
                {
                    ModPRC.error();
                }
            }
            else
            {
                ModPRC.error();
            }
        }
    }

    return 0;
}