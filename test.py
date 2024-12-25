from app import TelegramDevApi
from utiles import ManyTries, CodeInvalid

TelegramApp = TelegramDevApi("<PHONE_NUMBER>")
try:
    TelegramApp.SEND_CODE()
except ManyTries as e :
    print(e)
    
try:
    TelegramApp.LOGIN(input('Enter a Code : '))
except CodeInvalid as e:
    print(e)
    
api_id, api_hash = TelegramApp.GET_API()
print(api_id)
print(api_hash)
