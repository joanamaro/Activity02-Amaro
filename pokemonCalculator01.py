Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:05:16) [MSC v.1915 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #charizard vs feraligatr
>>> charizard = 90
>>> feraligatr = 95
>>> modifier = round((1 * 1 * 1 * 2 * 0.85 * 1.5 * 0.25 ),2)
>>> damage = round(((((((2*90)/5)+2)*110*(205/188))/50)+2),2)
>>> tdamage = round ((damage * modifier),2)
>>> print('Damage Dealt: ', tdamage)
Damage Dealt:  59.62
>>> 
