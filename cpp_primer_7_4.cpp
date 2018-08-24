#include<string>
#include<vector>
#include "Sales_item.h"
#include<iostream>
#include<fstream>
using std::string;
using std::cin; using std::cout; using std::endl;
struct sales_data {
	std::string isbn() const { return bookNo; }
	sales_data & combine(const sales_data &);
	double avg_price() const;
	std::string bookNo;
	unsigned units_sold = 0;
	double revenue = 0.0;

};
sales_data & sales_data::combine(const sales_data &rhs) {
	units_sold += rhs.units_sold;
	revenue += rhs.revenue;
	return *this;
}
double sales_data::avg_price() const {
	if (units_sold) {
		return revenue / units_sold;
	}
	else {
		return 0;
	}

}
struct person {
	std::string names;
	std::string addresses;
	string name() {
		return this->names;
	};
	string address() {
		return this->addresses;
	};

};
std::istream &read(std::istream &is, sales_data &item)
{
	double price = 0;
	is >> item.bookNo >> item.units_sold >> price;
	item.revenue = price * item.units_sold;
	cout << item.bookNo <<" "<< item.units_sold<<" " << price << endl;
	return is;
}
std::ostream &write(std::ostream &os, const sales_data & item)
{
	os << item.isbn() << " " << item.units_sold << " "
		<< item.revenue << " " << item.avg_price();
	return os;
}
int main()
{
	//sales_data data1, data2;
	//std::cin >> data1.bookNo>>data1.units_sold>>data1.revenue;
	//std::cin >> data2.bookNo>> data2.units_sold >> data2.revenue;
	//if (data1.bookNo == data2.bookNo)
	//	return 0;
	//else
	//	std::cout << data2.revenue + data1.revenue << " " << data1.units_sold + data2.units_sold << " " << std::endl;
	//   return 0;
	person person1, person2;
	sales_data data;

	std::filebuf str_buff;
	if (str_buff.open("E:/code/1.txt", std::ios::in))
	{
		std::istream is(&str_buff);
		read(is, data);

		//cout << read(is, data) << endl;
	}
	//cin >> person1.names >> person2.names;
	//cout << person2.name() << " " << person1.name()<<endl;

}
