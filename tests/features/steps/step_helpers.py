import csv
import os


def get_ascent_csv_file(context):
    return os.path.join(os.path.abspath(context.tmp_dir.name), 'ascent.csv')


def get_csv_writer(columns, context):
    return csv.DictWriter(context.csv_file, fieldnames=columns)


def get_empty_row(columns):
    new_row = {}
    for c in columns:
        new_row[c] = ''
    return new_row


def get_basic_csv_row(**kwargs):
    row = {'filename': '', 'name': '', 'dilution_factor': '', 'type': '', 'assay': '', 'instrument': '', 'ascentid': ''}
    for k, v in kwargs.items():
        row[k] = v
    return row