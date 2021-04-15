from fileinput import input
from optparse import OptionParser


def read_file(input_file, scope, outfile):
    m_list = []
    l_count = 0

    for line in input(input_file):
        m_list.append(line)
        l_count += 1

        try:
            if line == '\n' and m_list[l_count-2] == "\n" and m_list[l_count-3] == "\n" and m_list[0] == "======================================================\n" and m_list[2] == "======================================================\n":
                if scope not in m_list[1]:
                    continue

                with open(outfile, "a+", encoding='utf-8') as output:
                    for req in m_list:
                        output.write(str(req))

                m_list.clear()
                l_count = 0

        except Exception:
            continue


if __name__ == '__main__':
    parser = OptionParser(usage="usage:  %prog [options]")
    parser.add_option("-i", action="store", dest="input_file", help="BurpSuite Log file")
    parser.add_option("-s", action="store", dest="scope", help="Scope e.g. www.google.com")
    parser.add_option("-o", action="store", dest="output_file", help="Parsed BurpSuite Log file output")

    (options, args) = parser.parse_args()

    input_file = options.input_file
    scope = options.scope
    output_file = options.output_file

    if not input_file or not scope or not output_file:
        parser.print_help()
        exit()

    read_file(input_file, scope, output_file)
