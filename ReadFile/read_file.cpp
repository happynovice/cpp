#include<string>
#include<vector>
#include<iostream>
#include<direct.h>
#include<io.h>
#include<opencv.hpp>
using	std::string;
using	std::vector;
using   std::cout; using std::endl;

void FindFile(string FileDir, vector<string> &files)
{
	string PictureType = "jpg";
	files.clear();
	//const char * dir = FileDir.c_str();
	//_chdir(dir);
	static _finddata_t FileInf;
	string PictureTypeBuff = FileDir+ "*." + PictureType + "*";
	long HFile = (long)_findfirst(PictureTypeBuff.c_str(), &FileInf);
	if (HFile != -1)
	{
		do
		{
			if (!(FileInf.attrib&_A_SUBDIR))
			{
				string FileNameBuff = FileInf.name;
				files.push_back(FileNameBuff);
				cout << FileNameBuff << endl;
			}
		} while (_findnext(HFile, &FileInf) == 0);
		_findclose(HFile);
	}
}

bool write_yuv_bin(string resize_folder,vector<string> pic_name_list, string yuv_folder)
{
	for (auto pic_path : pic_name_list)
	{
		//std::ofstream write_file("E:/convert_pic/yuv_test.txt", std::ios::out);
		cv::Mat RGB_B = cv::imread(resize_folder+pic_path);
		if (RGB_B.rows == 0)
		{
			printf("read picture faild\n");
			return false;
		}
		//cv::imshow("1", RGB_B);
		//cv::waitKey(100);
		int begin = pic_path.find_last_of("/");
		int end = pic_path.find_last_of(".");
		string pic_name = pic_path.substr(0, end - begin);
		FILE *p2 = NULL;
		p2 = fopen((yuv_folder + pic_name + "yuv").c_str(), "wb");

		int PicSize = (int)(1920 * 1080 * 1.5);
		unsigned char *YUV_Write = (unsigned char *)malloc(PicSize * sizeof(unsigned char));
		unsigned char * ptr_YUV_Write = (unsigned char *)YUV_Write;
		for (int i = 0; i < RGB_B.rows; i++)
		{
			for (int j = 0; j < RGB_B.cols; j++)
			{
				int   B = RGB_B.at<cv::Vec3b>(i, j)[0];
				int   G = RGB_B.at<cv::Vec3b>(i, j)[1];
				int   R = RGB_B.at<cv::Vec3b>(i, j)[2];
				*(ptr_YUV_Write++) = (int)((0.257*R + 0.098*B + 0.504*G) + 16);
				//if (j % 4 == 0)
				//	write_file << endl;
				//write_file << (int)((0.257*R + 0.098*B + 0.504*G) + 16) << " ";
			}
		}
		for (int i = 0; i < RGB_B.rows / 2; i++)
		{
			for (int j = 0; j < RGB_B.cols / 2; j++)
			{
				int  B_V = RGB_B.at<cv::Vec3b>(i * 2, j * 2)[0];
				int  G_V = RGB_B.at<cv::Vec3b>(i * 2, j * 2)[1];
				int  R_V = RGB_B.at<cv::Vec3b>(i * 2, j * 2)[2];
				int  B_U = RGB_B.at<cv::Vec3b>(i * 2, j * 2)[0];
				int  G_U = RGB_B.at<cv::Vec3b>(i * 2, j * 2)[1];
				int  R_U = RGB_B.at<cv::Vec3b>(i * 2, j * 2)[2];
				//if (j % 2 == 0)
				//	write_file << endl;
				*(ptr_YUV_Write++) = (int)(0.439*R_V - 0.368*G_V - 0.071*B_V + 128);
				//write_file << (int)(0.439*R_V - 0.368*G_V - 0.071*B_V + 128) << " ";
				*(ptr_YUV_Write++) = (int)(-0.148*R_U - 0.291*G_U + 0.439*B_U + 128);
				//write_file << (int)(-0.148*R_U - 0.291*G_U + 0.439*B_U + 128) << " ";

			}
		}

		fwrite(YUV_Write, 1, PicSize * sizeof(char), p2);
		cout << "pic_name: " << pic_name << endl;
		free(YUV_Write);
		YUV_Write = NULL;
		fclose(p2);
	}
	//cv::imshow("1", RGB_B);
	//cv::waitKey(500);
}
