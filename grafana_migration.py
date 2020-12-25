import os
import subprocess
import logging
import sys
import bcolors as b
from backup_config import wizzy_configure 

logging.basicConfig(filename="/var/log/grafana_dashboard_migration.out",level = logging.INFO,format = '%(levelname)s %(asctime)s %(message)s',datefmt = '%Y-%m-%d %H:%M:%S',filemode = 'a')
logger = logging.getLogger()

#set environment variable for ignoring https 
os.environ['NODE_TLS_REJECT_UNAUTHORIZED']='0'

print("""{}

====================  Grafana Migration using wizzy ====================

1.Congigure Grafana source.
2.Preforms Importing of dashboard and datasources form source.
3.Congigure  Grafana destination
4.Performs exporting of dashboard and datasources to destination

Note: Make sure to use Grafana user having admin access to preform migration.

==============================================================================

{}""".format(b.WARN,b.END))


def wizzy_list_dashboard():
    try:

        check_stdout=subprocess.run(['wizzy', 'list','dashboards'], stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        check_stderr=str(check_stdout.stderr.decode('utf-8'))
        if check_stdout.returncode == 0 and check_stderr !='':
            logger.info("Invalid Credentials")
            print("{} Invalid Credentials{}".format(b.ERRMSG,b.END))
            sys.exit(2)
        elif check_stdout.returncode == 0 and  check_stderr =='':
            
        #else:
            logger.info("Valid Credentials")
            print("{} Verified Credentials {}".format(b.OKMSG,b.END))


    except Exception as e:
        logger.error('Exception occoured while listing dashboard :{}'.format(e))
        print("{} Exception occoured while listing_dashboard {}".format(b.ERRMSG,b.END))

def  take_wizzy_dashboard_backup():
    try:
        
        check_stdout=subprocess.run(['wizzy', 'import','dashboards'], stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
        logger.info("Backup for dashboards Taken successfully")
        print("{} Backup for dashboards Taken successfully {}".format(b.OKMSG,b.END))
        
        
    except Exception as e:
        logger.error('Exception occoured while taking grafana dashboard backup:{}'.format(e))    
        print("{} Exception occoured while taking grafana dashboard backup {}".format(b.ERRMSG,b.END))

def  take_wizzy_datasource_backup():
    try:
        
       
        
        check_stdout=subprocess.run(['wizzy', 'import','datasources'], stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        
        if check_stdout.returncode !=0:
            
            logger.error("Error while  taking datasources backup")
            print("{} Error while  taking datasources backup ERROR:{} {}".format(b.ERRMSG,check_stdout,b.END))
        else:
            logger.info("Backup for datasources successfully")
            print("{} Backup for datasources Taken successfully {}".format(b.OKMSG,b.END))
        
        
    except Exception as e:
        logger.error('Exception occoured while taking grafana datasources backup:{}'.format(e))    
        print("{} Exception occoured while taking grafana datasources backup {}".format(b.ERRMSG,b.END))

def  export_dashboard_backup():
    try:
        
        check_stdout=subprocess.run(['wizzy', 'export','dashboards'], stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        
        if check_stdout.returncode !=0:
            
            logger.error("Error while  exporting dashboards backup")
            print("{} Error while  exporting dashboard backup {}".format(b.ERRMSG,b.END))
        
        else:
            logger.info("Dashboards exported successfully")
            print("{} Dashboards exported successfully {}".format(b.OKMSG,b.END))
        
        
    except Exception as e:
        logger.error('Exception occoured while exporting dashboard backup:{}'.format(e))    
        print("{} Exception occoured while exporting dashboard backup {}".format(b.ERRMSG,b.END))

def  export_datasource_backup():
    try:
        
       
        check_stdout=subprocess.run(['wizzy', 'export','datasources'], stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        
        if check_stdout.returncode !=0:
            
            logger.error("Error while exporting datasources backup")
            print("{} Error while exporting datasources backup {}".format(b.ERRMSG,b.END))
        else:
            logger.info("Datasources exported successfully")
            print("{} Datasources exported successfully {}".format(b.OKMSG,b.END))
        
        
    except Exception as e:
        logger.error('Exception occoured while exporting grafana datasources :{}'.format(e))    
        print("{} Exception occoured while exporting grafana datasources {}".format(b.ERRMSG,b.END))        
        

def Main():
    try:

        config_obj=wizzy_configure() 
        
        print("{} Configuring Wizzy {}".format(b.WARN,b.END))
        
        #Importing
        print("{}=====================================\nImporting Dashboard and Datasources\n===================================== {}".format(b.WARN,b.END))
        config_obj.wizzy_unset_env()    
        config_obj.wizzy_config()
        
        wizzy_list_dashboard()
        take_wizzy_dashboard_backup()
        take_wizzy_datasource_backup()
        
        print("{}======================================\nExporting Dashboard and Datasources\n====================================== {}".format(b.WARN,b.END))
        
        #Exporting
        config_obj.wizzy_unset_env()
        config_obj.wizzy_config()
        export_dashboard_backup()
        export_datasource_backup()
        
        
    except Exception as e:
        logger.error("Exception occured in main:{}".format(e))
        print("{} Exception occoured {}".format(b.ERRMSG,b.END))

if __name__=='__main__':
    Main()
