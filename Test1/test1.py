import time
from bittrex2.bittrex import Bittrex
import pprint

#init
pp = pprint.PrettyPrinter(indent=3)
f = open('MSUMS_JUN1.csv', 'a')

#loop
br = Bittrex(None, None)
i = 0

while (True):
    res = br.get_market_summaries()
    #pp.pprint(res)
    i += 1
    t_now = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(time.time()))
    print(t_now + " Lines written: " + str(i))
    s = '\n' + str(t_now) + '\t'+ str(res)
    f.write(s)  # python will convert \n to os.linesep
    time.sleep(300)

f.close()  # you can omit in most cases as the destructor will call it