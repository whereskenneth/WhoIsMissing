import os
import sys
import csv
import ctypes
import glob


class WhoIsMissing(object):

    def __init__(self, csv_path):
        self.csv_path = os.path.abspath(csv_path)
        try:
            self.check_csv_is_from_ascent()
            self.show_missing_files()
        except Exception as e:
            self.alert(str(e))

    def check_csv_is_from_ascent(self):
        with open(self.csv_path, "r") as f:
            csv_file = csv.DictReader(f)
            required_headers = ["name", "type", "dilution_factor", "filename"]
            for required_header in required_headers:
                if required_header not in csv_file.fieldnames:
                    raise Exception(required_header + " not found. Are you sure it's an Ascent sequence file?")

    def show_missing_files(self):
        missing_filenames = self.get_missing_filenames()
        if missing_filenames:
            missing_filenames.insert(0, "The following files could not be found:\n\n")
            self.alert('\n'.join(missing_filenames))
        else:
            self.alert("All files appear to be present and accounted for.")

    def get_missing_filenames(self):
        csv_contents = [l for l in csv.DictReader(open(self.csv_path, "r"))]
        missed_filenames = []
        batch_directory = os.path.dirname(self.csv_path)
        files = [os.path.splitext(os.path.basename(f))[0] for f in glob.glob(batch_directory + '/*')]
        print('\n'.join(files))
        for line in csv_contents:
            filename = line['filename']
            if filename not in files:
                missed_filenames.append(filename)
        return missed_filenames

    @staticmethod
    def alert(msg):
        ctypes.windll.user32.MessageBoxW(0, str(msg), "Info", 0)


def main():
    csv_file = sys.argv[1]
    WhoIsMissing(csv_file)

if __name__ == "__main__":
    main()