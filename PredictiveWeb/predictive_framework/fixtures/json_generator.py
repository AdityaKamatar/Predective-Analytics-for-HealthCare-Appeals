import sys
import csv
import json

MODEL = 'predictive_framework.aggregatecase'
OUTPUT_FILE = 'fixture.json'
FIELDS_NAME = ['fiscal_year', 'claims', 'request_type', 'appeal_category', 'medicare_part', 'requestor_type', 'state',
               'otr', 'psc_zpic', 'rac', 'hearing_type', 'procedure_code', 'disposition']


def main(argv):
    json_data = generate_json(argv[1])
    output_json(json_data)


def generate_json(input_file):
    with open(input_file, newline='') as file:
        reader = csv.reader(file)
        json_data = []

        next(reader)

        pk = 1
        for row in reader:
            json_instance = {'model': MODEL, 'pk': pk, 'fields': {}}

            for i in range(len(FIELDS_NAME)):

                if FIELDS_NAME[i] == 'claims':
                    json_instance['fields'][FIELDS_NAME[i]] = int(row[i])
                else:
                    json_instance['fields'][FIELDS_NAME[i]] = row[i]
            json_data.append(json_instance)
            pk += 1
    return json_data


def output_json(json_data):
    with open(OUTPUT_FILE, 'w') as writer:
        writer.write(json.dumps(json_data, indent=4))


if __name__ == '__main__':
    main(sys.argv)