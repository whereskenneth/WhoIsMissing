import ast
import glob
import json
import os
import behave
from WhoIsMissing import WhoIsMissing, InvalidAscentCsvException
from tests.features.steps import step_helpers


@behave.given('an Ascent csv file with columns {columns}')
def given_an_ascent_csv_file(context, columns):
    context.csv_file_path = step_helpers.get_ascent_csv_file(context)
    context.csv_file = open(context.csv_file_path, "w")
    columns = ast.literal_eval(columns)
    writer = step_helpers.get_csv_writer(columns, context)
    writer.writeheader()
    context.csv_writer = writer


@behave.given('an Ascent csv file with minimum required columns')
def given_an_ascent_csv_file_with_columns(context):
    context.csv_file_path = step_helpers.get_ascent_csv_file(context)
    context.csv_file = open(context.csv_file_path, "w")
    columns = ['filename', 'name', 'dilution_factor', 'type', 'assay', 'instrument', 'ascentid']
    writer = step_helpers.get_csv_writer(columns, context)
    writer.writeheader()
    context.csv_writer = writer


@behave.given('it has a full row with {row_data}')
def it_has_a_full_row(context, row_data):
    row_data = json.loads(row_data)
    row = step_helpers.get_basic_csv_row(**row_data)
    context.csv_writer.writerow(row)


@behave.when('I add all injections in the sequence file with a {extension} extension')
def i_add_all_injections_in_the_sequence_file(context, extension):
    context.csv_file.close()
    wim = WhoIsMissing(context.csv_file_path)
    tmp_dir_files = glob.glob(context.tmp_dir.name + '/*')
    tmp_dir_files.remove(context.csv_file_path)
    for old_injection_file in tmp_dir_files:
        os.remove(old_injection_file)

    for mf in wim.get_missing_filenames():
        open(os.path.join(os.path.abspath(context.tmp_dir.name), mf + extension), "w").close()


@behave.when('I remove injections {removed_injections}')
def i_add_all_injections_in_the_sequence_file(context, removed_injections):
    for old_injection_file in ast.literal_eval(removed_injections):
        for match in glob.glob(os.path.join(context.tmp_dir.name, old_injection_file) + '*'):
            os.remove(match)


@behave.then('I should not have any missing injections')
def i_should_not_have_any_missing_injections(context):
    context.csv_file.close()
    wim = WhoIsMissing(context.csv_file_path)
    assert len(wim.get_missing_filenames()) == 0


@behave.then('I should have missing injections: {filenames}')
def i_should_have_missing_injections(context, filenames):
    context.csv_file.close()
    filenames = ast.literal_eval(filenames)
    wim = WhoIsMissing(context.csv_file_path)
    assert filenames == wim.get_missing_filenames()


@behave.then('I should be able to instantiate my class')
def then_i_should_be_able_to_instantiate(context):
    context.csv_file.close()
    WhoIsMissing(context.csv_file_path)


@behave.then('I should get an InvalidAscentCsvException')
def then_i_should_get_an_exception(context):
    context.csv_file.close()
    try:
        WhoIsMissing(context.csv_file_path)
    except InvalidAscentCsvException:
        pass
    except Exception as e:
        raise e
