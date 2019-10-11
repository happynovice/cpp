#include<functional>
#include<string>
#include<map>
#include<iostream>
// TODO: reference any additional headers you need in STDAFX.H
// and not in this file
typedef std::function<void(void)> Fun;
typedef std::map<std::string, Fun> FunMap;
FunMap fun_map;
class Class_FunMap {
public:
	Class_FunMap(std::string str, Fun fun) {
		fun_map[str] = fun;
	}
};
void test_fun1() {
	std::cout << "test_fun1 \n";
}
void test_fun2() {
	std::cout << "test_fun2 \n";
}
#define FUN_MAP_DEF(fun) Class_FunMap Test##fun(#fun,test_##fun)
FUN_MAP_DEF(fun1);
FUN_MAP_DEF(fun2);
void test(std::string str) {
	fun_map[str]();
}
