import os
import sys
import csv
import glob


def alert(msg):
    try:
        import ctypes
        ctypes.windll.user32.MessageBoxW(0, str(msg), "Info", 0)
    except (AttributeError, ImportError) as e:
        print(msg)


class InvalidAscentCsvException(Exception):
    def __init__(self, msg):
        self.msg = msg


class WhoIsMissing(object):

    def __init__(self, csv_path):
        self.csv_path = os.path.abspath(csv_path)
        try:
            self.check_csv_is_from_ascent()
        except InvalidAscentCsvException as e:
            alert(str(e))
            raise e

    def show_missing_files(self):
        missing_filenames = self.get_missing_filenames()
        if missing_filenames:
            missing_filenames.insert(0, "The following files could not be found:\n")
            alert('\n\t'.join(missing_filenames))
        else:
            alert("All files appear to be present and accounted for.")

    def check_csv_is_from_ascent(self):
        with open(self.csv_path, "r") as f:
            reader = csv.DictReader(f)
            required_headers = ["name", "type", "dilution_factor", "filename", "assay", "instrument", "ascentid"]
            for required_header in required_headers:
                if required_header not in reader.fieldnames:
                    raise InvalidAscentCsvException("Required header \"" + required_header + "\" not found. Are you sure it's an Ascent sequence file?")

    def get_missing_filenames(self):
        csv_contents = [l for l in csv.DictReader(open(self.csv_path, "r"))]
        missed_filenames = []
        batch_directory = os.path.dirname(self.csv_path)
        files = [os.path.basename(f).split('.')[0].lower() for f in glob.glob(batch_directory + '/*')]
        for line in csv_contents:
            filename = line['filename'].lower()
            if filename not in files:
                missed_filenames.append(line['filename'])
        return missed_filenames


def main():
    csv_file = sys.argv[1]
    WhoIsMissing(csv_file).show_missing_files()

if __name__ == "__main__":
    main()