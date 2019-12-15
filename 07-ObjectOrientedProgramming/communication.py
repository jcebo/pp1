from message import Message
from sms import Sms
from email import Email

sms=Sms(512452125,698548421)
sms.set_message('INFORMUJĘ, ŻE Nasze Czwartkowe spotkanie ZOstało odwołANE.')
sms.send()

email=Email('Marek','Staszek','Zajęcia')
email.set_message('INFORMUJĘ, ŻE Nasze Czwartkowe spotkanie ZOstało odwołANE.')
email.send()