#ifndef MODPRC_HPP
#define MODPRC_HPP

namespace N
{    
    class ModPRC
    {
        public:
            void prc_doc()
            {
                std::cout << "Documentation : https://github.com/Program132/PRC/tree/PRC#documentation" << std::endl;
            }

            void prc_about()
            {
                std::cout << "PRC is an interpreted language. This language will be improved over time ! Other informations : https://github.com/Program132/PRC/tree/PRC#about" << std::endl;
            }

            void prc_discord()
            {
                std::cout << "Discord : https://discord.com/invite/FjS9jvwvhS" << std::endl;
            }

            void error()
            {
                std::cout << "Error, please give me this argument : doc, about or disocrd !" << std::endl;
            }
    };
}

#endif