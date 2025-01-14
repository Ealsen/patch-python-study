 # name,公司名
 # stock_price,当前股价
 # stock_code,股票代码
 # stock_price_daily_growth_factor,股票每日增长系数
 # growth_days,增长天数
 # finally_stock_price,增长过后的股价

name = "传智播客"
stock_price = 19.99
stock_code = "003032"
stock_price_daily_growth_factor = 1.2
growth_days = 7
finally_stock_price = stock_price * stock_price_daily_growth_factor ** growth_days
print(f"公司：{name}，股票代码：{stock_code},当前股价：{stock_price}")
print("每日增长系数是：%.1f,经过%d天后,股价达到了：%.2f" % (stock_price_daily_growth_factor,growth_days,finally_stock_price))