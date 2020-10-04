from faker import Factory
import csv
import random
from faker.providers import credit_card

#pylint: disable=no-member



def get_transaction_amount():
    return round(random.randint(1, 1000) * random.random(), 2)

def get_transaction_date(fake):
    return fake.date_time_between(start_date=2020-10-1, end_date=2020-10-2).isoformat()

def create_customer_record(customer_id):
    fake = Factory.create('en_GB')
    return [customer_id, fake.name(), fake.last_name(), fake.street_address().replace('\n', ', '), fake.city(), fake.postcode(), fake.email()]

def create_financials_record(customer_id):
    fake = Factory.create('en_GB')
    return [customer_id, fake.credit_card_number(), get_transaction_amount(), get_transaction_date(fake)]


def flush_records(records, filename):
    with open(filename, 'a') as file:
        csv_writer=csv.writer(file, delimiter = ',', quotechar = '"', quoting = csv.QUOTE_MINIMAL)
        for record in records:
            csv_writer.writerow(record)
    records.clear()


def create_customer_files(customer_count=1000):
    customer_records = []
    financial_records = []
    for id in range(1, customer_count):
        customer_id = str(id).zfill(10)
        customer_records.append(create_customer_record(customer_id))
        financial_records.append(create_financials_record(customer_id))
        if len(customer_records) == 1000:
            flush_records(customer_records, 'customer.csv')
            flush_records(financial_records, 'financials.csv')
    flush_records(customer_records, 'customer.csv')
    flush_records(financial_records, 'financials.csv')

create_customer_files()