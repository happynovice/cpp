#include "stdafx.h"
#include "Sales_item.h"
#include<string>
#include<vector>
#include<iostream>
using std::string;
using std::cin; using std::cout; using std::endl;
struct sales_data {
	std::string isbin() const { return bookNo; }
	sales_data & combine(const sales_data &);
	double avg_price() const;
	std::string bookNo;
	unsigned units_sold = 0;
	double revenue = 0.0;

};
sales_data & sales_data::combine(const sales_data &rhs){
	units_sold += rhs.units_sold;
	revenue += rhs.revenue;
	return *this;
}
double sales_data::avg_price() const{
	if (units_sold){
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
	cin >> person1.names >> person2.names;
	cout << person2.name() << " " << person1.name()<<endl;

}

