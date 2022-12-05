import os

from read import get_info_from_pdf
from run import excute

import time
start_time = time.time()

print('This program is designed by Kenneth for CS50')
time.sleep(2)
get_info_from_pdf()
excute()
print("--- %s seconds ---" % (time.time() - start_time))

os.system('pause')



