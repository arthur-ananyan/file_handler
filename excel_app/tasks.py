from excel_proj.celery import app
from .models import Contact
import pandas
import datetime


@app.task()
def handle_file(file_url):
    df = pandas.read_excel(file_url, index_col=0,)
    for row_index in df.index:
        name = df['Name'][row_index]
        phone_number = df['Phone'][row_index]
        email = df['Email'][row_index]
        three_min_flag = datetime.datetime.now() - datetime.timedelta(minutes=3)

        if not pandas.isna(phone_number):
            contact = Contact.objects.filter(
                phone_number=int(phone_number), email=email).order_by('-create_date').first()
            if contact:

                if contact.create_date < three_min_flag:
                    contact_to_save = Contact(
                        name=name, phone_number=int(phone_number), email=email)
                    contact_to_save.save()
                else:
                    pass
            else:
                contact_to_save = Contact(
                    name=name, phone_number=int(phone_number), email=email)
                contact_to_save.save()
        else:
            pass
