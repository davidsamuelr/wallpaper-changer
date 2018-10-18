# Author: David Samuel
# Version 1.0

from winreg import OpenKey, SetValueEx, QueryValueEx, HKEY_CURRENT_USER, KEY_ALL_ACCESS, REG_DWORD

def modifyReg():

    key = OpenKey(HKEY_CURRENT_USER, r'Software\Microsoft\Windows\CurrentVersion\Policies\ActiveDesktop', 0, KEY_ALL_ACCESS)
    valueName = "NoChangingWallPaper"
    SetValueEx(key, valueName, 0, REG_DWORD, 0)