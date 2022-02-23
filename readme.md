# Hotel-vinder

### Import data
>1. Plaats het city en hotel csv bestand in de buitenste folder.<br/>
>2. Voer het "*csv2fixture.py*" script uit. Deze is te vinden in ```website/hotel_data/scripts```<br/>
>3. Als het script correct uitgevoerd is zal er een fixture (json bestand) verschijnen in ```website/hotel_data/fixtures```<br/>
>4. Run het volgende commando ```python manage.py loaddata data.json```<br/>
>5. Als alles is verlopen zoals het hoort zal de data uit de csv bestanden nu in de SQLite database staan.

### Admin login
>Username: admin<br/>
>Password: root1234

### Omgeving
>*Python 3.6.6 x64, Win32*<br/>
>*Django 3.2.12*

## Resources

https://docs.djangoproject.com/en/4.0/howto/initial-data/<br/>
https://docs.djangoproject.com/en/4.0/topics/db/examples/many_to_one/<br/>
https://docs.djangoproject.com/en/4.0/ref/templates/language/<br/>
https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Admin_site