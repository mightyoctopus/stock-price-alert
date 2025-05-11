import news_api
import stock_api
import messaging_api

#-------------------------------------- OPERATION LOGIC ---------------------------------------#
company = "Tesla"
price_change = stock_api.check_price_change()
article_t_1= news_api.get_title(0)
article_t_2= news_api.get_title(1)
article_d_1= news_api.get_brief(0)
article_d_2= news_api.get_brief(1)


if abs(stock_api.check_price_change()) >= 4:
    messaging_api.send_sms(company, price_change, article_t_1, article_t_2, article_d_1, article_d_2)
    print("Message has been sent successfully!")
else:
    print("The price change is less than 5%")






