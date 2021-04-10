#ifndef PRINTING_HPP
#define PRINTING_HPP

#include <vector>
#include <sstream>
#include <string>
#include <iterator>
#include <string_view>

namespace N
{    
    class Printing
    {
        private:
            void missingA()
            {
                std::cout << "Error Print : You need start and finish your print with a other \" if you want send a text  !" << std::endl;
            }
            void missingOther(int const& arg)
            {
                if (arg == 1)
                {
                    std::cout << "Error Print : You need finish your print with a other \" if you want send a text !" << std::endl;
                }
                else if (arg == 2)
                {
                    std::cout << "Error Print : You need start your print with a other \" if you want send a text !" << std::endl;
                }
            }

        public:
            void do_print(std::string const& arg)
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
                    missingOther(1);
                }
                else if (checkGuillemets[0] != '"' ) 
                {
                    missingOther(2);
                }
                else if (checkGuillemets[0] != '"'  && checkGuillemets.back() != '"')
                {
                    missingA();
                }
            }
    };
}

#endif