# In this script I'll tuch opon 
# Display System Information, 
# Manage Services (Start, Stop, Restart),
# Monitor and Log System Resources,
# Automate Directory Backups,
# Provide a Comprehensive CLI Interface

def get_sys_info():
    #Imports a libary to get/check the OS
    import platform
    import psutil
    print('Operating System: ' + platform.system() + ' v' + platform.version())
    print('CPU Usages: ' + str(psutil.cpu_percent(1)) + '%')
    print('Total RAM avalible: ' + str(round(psutil.virtual_memory().total/1073741824)) + ' GB')
    print('Used RAM: ' + str(round(psutil.virtual_memory().used/1073741824)) + ' GB')
    print('Free RAM: ' + str(round(psutil.virtual_memory().free/1073741824)) + ' GB')
    print('Used Diskspace: ' + str(psutil.disk_usage('/').percent) + '% ' + 'of ' + str(round(psutil.disk_usage('/').total/1073741824)) + ' GB')
    print('Unused Diskspace: ' + str(round(psutil.disk_usage('/').free/1073741824)) + ' GB')
    print('Python version: ' + platform.python_version())

def main():
    get_sys_info()

main()

