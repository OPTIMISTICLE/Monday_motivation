import smtplib
import datetime
import random
email = "bibalefai@gmail.com"
password ="hudcwbcrhotbhmjr"
connections = smtplib.SMTP("smtp.gmail.com")
connections.starttls()
connections.login(user= email, password=password)

date = datetime.datetime.now()
print(date.weekday())
if date.weekday() == 6:
    with open("quotes", "r", encoding="utf-8") as quotes_file:
        quotes = quotes_file.readlines()
        quote = random.choice(quotes)
        quote = f"Subject: Daily quote \n\n{quote}".encode("utf-8")
        print(quote)
        connections.sendmail(
            to_addrs="doumb46@gmail.com",
            from_addr=email,
            msg= quote)