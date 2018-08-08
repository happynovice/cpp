#include<string>
#include<vector>
#include<iostream>
#include<fstream>
#include<opencv.hpp>
#include<io.h>
#include<stdio.h>
#include<direct.h>
#include<string.h>
#include<stdlib.h>
#include"read_file.h"
using	std::string;
using	std::vector;
using std::cout; using std::endl;
struct {
	int row;
	int	col;
}	BigSize = { 1920, 1080 },
	SmallSize = { 256, 160 };
bool resize_draw(string src_folder, vector<string> file_list, string WriteFolder)
{
	for (auto PicName : file_list)
	{
		cout << "Pic Name: " << PicName << endl;
		cv::Mat src = cv::imread(src_folder + PicName);
		if (src.rows == 0)
		{
			printf("read picture faild \n");
			return false;
		}
		cv::resize(src, src, cv::Size(BigSize.col, BigSize.row));
		cout << WriteFolder + PicName << endl;
		cv::imwrite(WriteFolder + PicName, src);

	}
}
int main()
{

	vector<string> NameList;
	string SearchFolder = "./src/";
	string resize_folder = "./src_resize/";
	string yuv_save_folder="./yuv/";
	//std::ofstream read_file("./config.txt",std::ios::in);
	cout << "img row: " << endl;
	std::cin>> BigSize.row  ;
	cout << "img col: " << endl;
	std::cin >>  BigSize.col ;
	FindFile(SearchFolder, NameList);
	resize_draw(SearchFolder,NameList, resize_folder);
	write_yuv_bin(resize_folder,NameList, yuv_save_folder);

	
	return 0;
}
