import getopt
import sys

from analizer import create_dump_analyzer, create_diff_analyzer
from parser.stepik_progress_parser import StepikProgressParser
from utils import save, load

if __name__ == '__main__':
    argumentList = sys.argv[1:]
    options = "cdp:"

    long_options = ["Create_DB", "Diff", "Path="]

    try:
        work_mode = 0
        path_to_file = ''
        arguments, values = getopt.getopt(argumentList, options, long_options)
        if len(arguments) != 2:
            raise getopt.GetoptError("Problems in input args")
        for currentArgument, currentValue in arguments:

            if currentArgument in ("-c", "--Create_DB"):
                work_mode = 1
                print('Create_DB mode')

            elif currentArgument in ("-d", "--Diff"):
                work_mode = 2

            elif currentArgument in ("-p", "--Path"):
                path_to_file = currentValue

        if work_mode == 1 and path_to_file != '':
            parser = StepikProgressParser(path_to_file)
            students = parser.parse()
            save(students, 'db')
            print('DataBase was created')
            analyzer = create_dump_analyzer(students)
            analyzer.run()
        elif work_mode == 2 and path_to_file != '':
            old_students_data = load('db.json')
            parser = StepikProgressParser(path_to_file)
            new_students_data = parser.parse()
            analyzer = create_diff_analyzer(old_students_data,
                                            new_students_data)
            analyzer.run()
        else:
            ...

    except getopt.error as err:
        print(str(err))


