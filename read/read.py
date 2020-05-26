# autor: Rafał Kwiatkowski
data_folder = "data/"
donor_file = "spliceDTrainKIS.dat"
acceptor_file = "spliceATrainKIS.dat"


def parse_examples(lines):
    size = len(lines) - 1
    return [(lines[i].strip('\n'), lines[i+1].strip('\n')) for i in range(0, size, 2)]


def read_file(file_name):
    with open(data_folder + file_name) as file:
        lines = file.readlines()
        return parse_examples(lines[1:])


def get_donors():
    return read_file(donor_file)


def get_acceptors():
    return read_file(acceptor_file)
