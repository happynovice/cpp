import mysql

import akshare as ak
import numpy as np
from datetime import datetime, timedelta
import mysql.connector.cursor
print(mysql.connector.cursor.CursorBase.__name__)

date = "日期"
close = "收盘"
code = "代码"
name = "名称"

def get_rps(_mycursor: mysql.connector.cursor.MySQLCursor, rps_rank, rps_range):
    _sql_query = "SELECT DISTINCT code,date,price FROM stock ORDER BY date DESC"
    _mycursor.execute(_sql_query)
    stock_price_list = _mycursor.fetchall()
    if stock_price_list == []:
        print("NULL")
        return 
    #for i in _myresult:
    _date_db_latest = stock_dict["000001"]
    print("_date_db_latest:", _date_db_latest)
    # date_before = close_date.values[close_date.values.size - 1 - rps_range]
    # date_latest_db = close_date.values[close_date.values.size - 1]
    # print("date_before:",date_before)
    # print("date_latest_db:",date_latest_db)
    _stock_dict = {}
    for _stock_info in stock_price_list:

        #print("_stock_info:",_stock_info)
        if _stock_info[0] not in _stock_dict.keys():
            _stock_dict[_stock_info[0]]=[[_stock_info[1],_stock_info[2]]]
        else:
            #print("before _stock_dict[_stock_info[0]]:", _stock_dict[_stock_info[0]])
            _stock_dict[_stock_info[0]].append([_stock_info[1],_stock_info[2]])
            #print("after _stock_dict[_stock_info[0]]:", _stock_dict[_stock_info[0]])
    #print("_stock_dict:",_stock_dict)
    print("stock_price_list.size:",len(stock_price_list))
    print("_stock_dict.size:",len(_stock_dict))

    #print("stock[0]:",result[0]," result[1]:",result[1])
    
    for _stock in _stock_dict:
        _len = len(_stock)
        #print("len(stock):",len(_stock))
        #print("_stock_dict[_stock]:",_stock_dict[_stock])
        if _stock_dict[_stock][0][0] != _date_db_latest or len(_stock_dict[_stock])  < rps_range + 1:
            continue

        price_latest = float(_stock_dict[_stock][0][1])
        #print("_stock_dict[_stock][0]:",_stock_dict[_stock][0])
        #print("price_latest:",price_latest)
        price_before = float(_stock_dict[_stock][rps_range][1])
        #stock_history = db.hgetall(stock)
        #if date_latest_db 
        #if stock_history == {}:
            #print("stock ",stock," is empty:")
        #    continue
            
        # if db.hexists(stock, date_latest_db) == False or db.hexists(stock, date_before) == False :
        #     #print("stock data:",stock," is empty:")
        #     continue
        #if stock_history[date_today] == 
        # price_today = float(stock_history[date_latest_db])
        # price_before = float(stock_history[date_before])
        tmp_rps = (price_latest - price_before)/price_before
        #print("stock:",stock, " rps:",tmp_rps)
        rps_rank.append([tmp_rps,_stock,0])
    rps_rank.sort()
    _len = len(rps_rank)
    for i in range(0, _len):
        rps_rank[i][2] = i/_len
 
    print("rps_rank:",len(rps_rank))
    return 

def update_stock_list(_mycursor: mysql.connector.cursor.MySQLCursor, arr_stock_code, arr_stock_name):
    for i in range(0, arr_stock_code.size):
        
            #print("code:", arr_stock_code[i]," name", arr_stock_name[i])
        _sql_query = "SELECT code FROM stock_list WHERE code = '{}'".format(arr_stock_code[i])
        
        _mycursor.execute(_sql_query)
        _myresult = _mycursor.fetchall()
        #print("_sql_query:{}   ,_myresult:{}\n".format(_sql_query,_myresult))
        if _myresult == []:
            print("_sql_query:{}   ,_myresult:{}\n".format(_sql_query,_myresult))
            _sql_write = "INSERT INTO stock_list(code, name)\
                        VALUES (%s, %s)"
            val = (arr_stock_code[i], arr_stock_name[i])
            _mycursor.execute(_sql_write, val)
            _myresult = _mycursor.fetchall()
            print("_sql_write:{}\n,_myresult:{}\n".format(_sql_write,_myresult))
            #db.hset("stock_list", arr_stock_code[i], arr_stock_name[i])
    mydb.commit()
    return

def update_stock_info(_mycursor: mysql.connector.cursor.MySQLCursor):
    _mycursor.execute("SELECT code,name FROM stock_list")

    stock_list = _mycursor.fetchall()
    #print("SELECT code,name FROM stock_list\n:",stock_list)
    # sql_read = "SELECT code FROM stock"
    # _mycursor.execute(sql_read)
    # _myresult = _mycursor.fetchall()
    # print("_mycursor:", _myresult)

    print(" start_date:",date_latest_db," end_date:",date_today)

    # date_latest_db = latest_db_date_tmp
    # if date_latest_db == date_latest_trading_day:
    #     return
    print(" date_latest_db:",date_latest_db)
    for stock in stock_list:
        #print("stock:",stock)
        # _sql_query = "SELECT code FROM stock_invalid WHERE code = '{}'".format(stock[0])
        # _mycursor.execute(_sql_query)
        # _result = _mycursor.fetchall()
        # if _result != []:
        #     print("useless code:",_result)
        #     continue

        # _sql_query = "SELECT date FROM stock WHERE code = '{}' ORDER BY date DESC".format(stock[0])
        # _mycursor.execute(_sql_query)
        # _result = _mycursor.fetchall()
        
        #print("code:",stock[0])
        if stock[0] in stock_invalid.keys():
            #print("useless code:",stock[0])
            continue
        
        _date_latest_db_tmp = date_latest_db
        if stock[0] in stock_dict.keys():
            #print("already new, stock[0]:",stock[0], " date_latest_db_origin:",date_latest_db_origin)

            if stock_dict[stock[0]] == date_latest_db_origin:
                
                continue
            _date_latest_db_tmp = (datetime.strptime(stock_dict[stock[0]],"%Y-%m-%d") + timedelta(days=1)).strftime("%Y-%m-%d")
            _date_latest_db_tmp = datetime.strptime(_date_latest_db_tmp,"%Y-%m-%d").strftime("%Y%m%d")
            print("_date_latest_db_tmp:",_date_latest_db_tmp)
            #_sql_delete = "DELETE FROM stock WHERE code = '{}'".format(stock[0])
            #_mycursor.execute(_sql_delete)
            #mydb.commit()
                        
        print("stock[0]:",stock[0]," _date_latest_db_tmp:", _date_latest_db_tmp, " date_latest_trading_day_input:",date_latest_trading_day_input)
        for i in range(1,3):
            try:
                stock_daily_df = ak.stock_zh_a_hist(symbol=stock[0], start_date = _date_latest_db_tmp,\
                                                  end_date = date_latest_trading_day_input, adjust="qfq")
                break
            finally:
                print("stock_zh_a_hist failed time:", i)
            

        if stock_daily_df.empty or stock_daily_df[date].empty or stock_daily_df[close].empty:
            print("useless stock:",stock, " start_date:",date_latest_db," end_date:",date_latest_trading_day_input)
            _sql_write = "INSERT INTO stock_invalid(code,name)\
                        VALUES (%s, %s)"
            val = (stock[0], stock[1])
            _mycursor.execute(_sql_write, val)
            mydb.commit()
            continue
        _index_tmp = stock_daily_df[date].values.size - 1
        print("_index_tmp",_index_tmp)
        if stock_daily_df[date].values[_index_tmp] < date_latest_trading_day_output:
            print("date_latest_trading_day_output:",date_latest_trading_day_output,\
                   " stock_daily_df[date].values[_index_tmp]:",stock_daily_df[date].values[_index_tmp])
            continue
        print("date_latest_trading_day_output:",date_latest_trading_day_output,\
                   " stock_daily_df['date'].values[_index_tmp]:",stock_daily_df[date].values[_index_tmp])

        for i in range(0,stock_daily_df[close].values.size):
            _sql_write = "INSERT INTO stock(date, code, name, price)\
                        VALUES (%s, %s, %s, %s)"
            val = (stock_daily_df[date].values[i], stock[0], stock[1], float(stock_daily_df[close].values[i]))

            #db.hset(stock, stock_daily_df['date'].values[i], stock_daily_df[close].values[i])
            if i == 0:
                print("date:", stock_daily_df[date].values[i],\
                     " price:", stock_daily_df[close].values[i],\
                     " code:", stock[0]," name:", stock[1], \
                     " stock_daily_df[close].values.size:", stock_daily_df[close].values.size)
            _mycursor.execute(_sql_write, val)
            mydb.commit()
            #
        
    return

mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password="123456",
  database="stockdb"
)

cursor = mydb.cursor()
date_today = datetime.now().strftime('%Y%m%d')

#mycursor.execute("CREATE DATABASE IF NOT EXISTS stockdb")
#mycursor.execute("USE stockdb")

#mycursor.execute("DROP TABLE stock_list")
#cursor.execute("DROP TABLE stock")
print("mydb:",mydb)

cursor.execute(
  "CREATE TABLE IF NOT EXISTS stock(\
	date VARCHAR(32) NOT NULL,\
	code VARCHAR(32) NOT NULL,\
	name VARCHAR(32) NOT NULL,\
	price FLOAT NOT NULL,\
	PRIMARY KEY (date, code)\
);")

cursor.execute(
  "CREATE TABLE IF NOT EXISTS stock_list(\
	code VARCHAR(32) NOT NULL,\
	name VARCHAR(32) NOT NULL,\
  exchange VARCHAR(32),\
	PRIMARY KEY (code)\
);")
#cursor.execute("DROP TABLE stock_invalid")
cursor.execute(
  "CREATE TABLE IF NOT EXISTS stock_invalid(\
	code VARCHAR(32) NOT NULL,\
	name VARCHAR(32) NOT NULL,\
  exchange VARCHAR(32),\
	PRIMARY KEY (code)\
);")
print("mydb:",mydb)
cursor.execute("SHOW TABLES")
result = cursor.fetchall()
print("ret:",result[0])

#########################################################################
stock_daily_df = ak.index_zh_a_hist(symbol="000016", period="daily")

# get close date

close_date = stock_daily_df[date]
date_latest_db_origin = close_date.values[close_date.values.size - 1]
print("date_latest_db_origin:",date_latest_db_origin)
date_latest_db = "20221111"
print("date_latest_db:",date_latest_db)
#exit()
date_latest_trading_day = datetime.strptime(close_date.values[close_date.values.size - 1], "%Y-%m-%d")
date_latest_trading_day_input = date_latest_trading_day.strftime('%Y%m%d')
date_latest_trading_day_output = date_latest_trading_day.strftime('%Y-%m-%d')
# print 
print("date_latest_trading_day_output:",date_latest_trading_day_output," date_latest_trading_day_input:",date_latest_trading_day_input)


stock_zh_a_spot_em_df = ak.stock_zh_a_spot_em()

arr_stock_code = stock_zh_a_spot_em_df[code].values
arr_stock_name = stock_zh_a_spot_em_df[name].values



update_stock_list(cursor, arr_stock_code, arr_stock_name)


_sql_query = "SELECT code,name FROM stock_invalid"
cursor.execute(_sql_query)
results = cursor.fetchall()
stock_invalid = {}
for result in results:
    stock_invalid[result[0]] = result[1]
#print("stock_invalid:",stock_invalid)
#########################################################################
_sql_query = "SELECT DISTINCT code,date FROM stock ORDER BY date"
cursor.execute(_sql_query)
results = cursor.fetchall()
stock_dict = {}
for result in results:
    #print("stock[0]:",result[0]," result[1]:",result[1])
    stock_dict[result[0]] = result[1]
#########################################################################
update_stock_info(cursor)
#print("stock:\n",stock)
#########################################################################
_sql_query = "SELECT DISTINCT code,date FROM stock ORDER BY date"
cursor.execute(_sql_query)
results = cursor.fetchall()
stock_dict = {}
for result in results:
    #print("stock[0]:",result[0]," result[1]:",result[1])
    stock_dict[result[0]] = result[1]
########################################################################


#ak.stock_zh_a_hist(symbol="000001", start_date = _date_latest_db_tmp,\
#                                              end_date = date_latest_trading_day_input, adjust="qfq")
#_sql_query = "SELECT date FROM stock WHERE code = {} ORDER BY date".format(stock[0])
rsp_rank = []
rps_range = 5
get_rps(cursor, rsp_rank, rps_range)

#print("rsp_rank:",rsp_rank)
for stock in rsp_rank:
    if stock[2] > 0.9 and stock[1][0] != '8':
        #print("")
        print(" code:", stock[1], " rps:", stock[2], " value:", stock[0])
# cursor.execute("SELECT * FROM stock_list")
# result_tmp = "2023-05-20"

# result = cursor.fetchall()
# for i in result:
#   i.__sizeof__()
  #print("i:",i[0],i[1],i[2]," i.__len__():",i.__len__())