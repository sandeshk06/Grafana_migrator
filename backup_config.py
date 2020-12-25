import subprocess
import bcolors as b
import getpass
import logging
import os
import sys

os.environ['PYTHONIOENCODING']='utf-8'

class wizzy_configure:

    def __init__(self):
        print("{} Initailizing ...{}".format(b.OKMSG,b.END))    
        

    def wizzy_unset_env(self):
        try:
       
            check_stdout=subprocess.run(['wizzy', 'unset','grafana','username'], stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        
            check_stdout=subprocess.run(['wizzy', 'unset','grafana','password'], stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        
            check_stdout=subprocess.run(['wizzy', 'init'], stdout=subprocess.PIPE)
            print("{} Wizzy env unset done successfully {}".format(b.OKMSG,b.END))    
            
            logging.info("Wizzy env unset done successfully")
        
        except exception as e:
            print("[-] problem on resetting wizzy config {}".format(e))
            logging.error("problem on resetting wizzy config")

    def wizzy_config(self):
        try:
        
            url=str(input("{}[+] Enter Grafana Url :{}".format(b.WARN,b.END)))
            username=str(input("{}[+] Enter Grafana Admin User :{}".format(b.WARN,b.END)))
            pwd=getpass.getpass("{}[+] Enter password :{}".format(b.WARN,b.END))
        
 
            check_stdout=subprocess.run(['wizzy', 'set','grafana','url',url], stdout=subprocess.PIPE)
            
            check_stdout=subprocess.run(['wizzy', 'set','grafana','username',username], stdout=subprocess.PIPE)
            
            check_stdout=subprocess.run(['wizzy', 'set','grafana','password',pwd], stdout=subprocess.PIPE)
            
            check_stdout=subprocess.run(['wizzy', 'set','grafana','debug_api','true'], stdout=subprocess.PIPE)
        
            if url == '' or username == '' or pwd=='':
                print("{}[-] Enter Valid URL/UserName/Password {}".format(b.ERRMSG,b.END))
                self.wizzy_config()
                
        
            else:
                print("{} Wizzy Setup Done.{}".format(b.OKMSG,b.END))
                logging.info("Wizzy Setup Done.")    
              
        except Exception as e:
            print("[-] Incomplet Wizzy config {}".format(e))
            logging.error("Incomplet Wizzy config")
