#pragma once
#ifndef MY_HEADER
#define MY_HEADER
#include <iostream>
#include <string>
#include<iostream>
using std::string;
class screen {
public:
	typedef std::string::size_type pos;
	screen() = default;
	screen(pos ht, pos wd,int num) :height(ht), weight(wd), contents(num,0) {};
	screen(pos ht, pos wd, char * c) :height(ht),weight(wd),contents(c) {};
	screen(pos ht, pos wd, string  c) :height(ht), weight(wd), contents( c) {};
	screen(pos ht, pos wd, char  c) :height(ht), weight(wd), contents(1,c) {};
	std::string print() {

		return contents; 
	};
private:
	pos cursor = 0;
	pos height = 0, weight = 0;
	std::string contents;
};
#endif
