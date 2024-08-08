#include <iostream>
#include <fstream>   
#include <string>

using namespace std;

int main(){
    ifstream file =ifstream("..\\Sample.esp");
    string content;
    std::getline(file,content);
    const char* data = content.c_str();
    if(content.size()>4){
    }
    return 0;
}