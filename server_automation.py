# In this script I'll tuch opon Display System Information, 
# Manage Services (Start, Stop, Restart),
# Monitor and Log System Resources,
# Automate Directory Backups,
# Provide a Comprehensive CLI Interface

def get_sys_info():
    #Imports a libary to get/check the OS
    import platform
    import psutil
    print('Operating System: ' + platform.system() + ' v' + platform.version())
    print('CPU Usages: ' + psutil.getloadavg())


def main():
    get_sys_info()

main()

