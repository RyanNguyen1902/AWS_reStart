import os, subprocess

# os.system("ls")
# subprocess.run("ls")

import logging

def checkvalue(valuetocheck):
    assert (type(valuetocheck) is int), "you must enter a number"
    assert (valuetocheck > 0), "Value entered must be greater than 0"
    if valuetocheck > 4:
        print("value is greater than 4")

var = int(input("enter a number greater than 0:"))
checkvalue(var)

logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.DEBUG)
logging.debug('This message should go to the log file')
logging.info('So should this')
logging.warning('And this, too')
logging.error('And non-ASCII stuff, too, like Øresund and Malmö')