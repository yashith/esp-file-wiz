#include <iostream>
#include <fstream>   
#include <string>

using namespace std;

// int main(){
//     ifstream file =ifstream("..\\Sample.esp");
//     string content;
//     std::getline(file,content);
//     const char* data = content.c_str();
//     if(content.size()>4){
//     }
//     return 0;
// }

struct HEDR {
    char hedr[4];
    uint16_t size;       // 4 bytes: float32
    uint64_t version;       // 4 bytes: float32
    uint32_t recordCount;  // 4 bytes: uint32_t
    uint32_t nextObjectID; // 4 bytes: uint32_t
};
// struct RHEADR {
//     char signature[4]; 
//     _int32 dataSize;
//     flags;
//     formId
// };

int main(){
// Open the file in binary mode
    std::ifstream file("..\\Sample.esp", std::ios::binary);

    if (!file) {
        std::cerr << "Error: Could not open the file!" << std::endl;
        return 1;
    }
    file.seekg(24, std::ios::beg);
    // Create an instance of HEDR
    HEDR header;

    // Read the header data
    file.read(reinterpret_cast<char*>(&header.hedr), sizeof(header.hedr));
    file.read(reinterpret_cast<char*>(&header.size), sizeof(header.size));
    file.read(reinterpret_cast<char*>(&header.version), sizeof(header.version));
    file.read(reinterpret_cast<char*>(&header.recordCount), sizeof(header.recordCount));
    file.read(reinterpret_cast<char*>(&header.nextObjectID), sizeof(header.nextObjectID));

    // Close the file
    file.close();

    // Output the read values
    std::cout << "HEDR: " << header.hedr<< std::endl;
    std::cout << "Size: " << header.size<< std::endl;
    std::cout << "Version: " << header.version << std::endl;
    std::cout << "Record Count: " << header.recordCount << std::endl;
    std::cout << "Next Object ID: " << header.nextObjectID << std::endl;

    return 0;
}