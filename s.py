Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import sys
>>> sys.path
['', 'C:\\Users\\asus\\AppData\\Local\\Programs\\Python\\Python311\\Lib\\idlelib', 'C:\\Users\\asus\\AppData\\Local\\Programs\\Python\\Python311\\python311.zip', 'C:\\Users\\asus\\AppData\\Local\\Programs\\Python\\Python311\\DLLs', 'C:\\Users\\asus\\AppData\\Local\\Programs\\Python\\Python311\\Lib', 'C:\\Users\\asus\\AppData\\Local\\Programs\\Python\\Python311', 'C:\\Users\\asus\\AppData\\Local\\Programs\\Python\\Python311\\Lib\\site-packages']
>>> for i in sys.path
SyntaxError: expected ':'
>>> for i in sys.path:
... 
...     print(i)
... 
...     

C:\Users\asus\AppData\Local\Programs\Python\Python311\Lib\idlelib
C:\Users\asus\AppData\Local\Programs\Python\Python311\python311.zip
C:\Users\asus\AppData\Local\Programs\Python\Python311\DLLs
C:\Users\asus\AppData\Local\Programs\Python\Python311\Lib
C:\Users\asus\AppData\Local\Programs\Python\Python311
C:\Users\asus\AppData\Local\Programs\Python\Python311\Lib\site-packages
>>> sys.version
'3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)]'
