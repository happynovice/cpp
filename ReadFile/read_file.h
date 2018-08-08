#pragma once
#ifndef READ_FILE_H
#include<string>
#include<vector>
bool write_yuv_bin(std::string resize_folder,std::vector<std::string> pic_name_list, std::string yuv_folder);
//bool resize_draw(std::string src_folder, std::vector<std::string> file_list, std::string WriteFolder);
void FindFile(std::string FileDir, std::vector<std::string> &files);
#endif
