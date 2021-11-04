from requests import get

pic=get("https://api.xingzhige.com/API/zwimg/api.php").content
print(pic)