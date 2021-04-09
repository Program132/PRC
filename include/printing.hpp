#ifndef PRINTING_HPP
#define PRINTING_HPP

#include <vector>
#include <sstream>
#include <string>
#include <iterator>

namespace N
{    
    class Printing
    {
        public:
            template <typename pr>
            void doprint(pr const& arg)
            {
                std::istringstream iss(arg);
                std::vector<char> checkGuillemets((std::istream_iterator<char>(iss)), std::istream_iterator<char>());;    

                if (checkGuillemets[0] == '"' && checkGuillemets.back() == '"')
                {
                    std::string str = arg;
                    str.replace(str.find('"'), 1, "");
                    str.replace(str.find('"'), str.find_last_of("\""), "");

                    std::cout << str << std::endl;
                }
                else if (checkGuillemets.back() != '"') 
                {
                    std::cout << "Error Print : You need finish your print with a other \" if you want send a text !" << std::endl;
                }
                else if (checkGuillemets[0] != '"' ) 
                {
                    std::cout << "Error Print : You need start your print with a other \" if you want send a text !" << std::endl;
                }
                else if (checkGuillemets[0] != '"'  && checkGuillemets.back() != '"')
                {
                    std::cout << "Error Print : You need start and finish your print with a other \" if you want send a text  !" << std::endl;
                }
            }
    };
}

#endif