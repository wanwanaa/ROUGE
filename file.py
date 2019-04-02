# os.path
# os.path.join(path1, path2, ..., pathn) connect file path
# os.mkdir(path) create a file directory
import os


def get_data_pairs(model_filename, system_filename):
    data = []
    s_f = open(system_filename, 'r')
    m_f = open(model_filename)
    for line in s_f.readlines():
        temp = []
        temp.append(line)
        temp.append(m_f.readline())
        data.append(temp)
    return data


def write_data_for_eval(data_dir, data):
    model_dir = os.path.join(data_dir, 'model_summaries')
    system_dir = os.path.join(data_dir, 'system_summaries')

    os.mkdir(data_dir)
    os.mkdir(model_dir)
    os.mkdir(system_dir)

    for i in range(len(data)):
        model, system = data[i]
        model_file = os.path.join(model_dir, 'summary.A.%d.txt' % i)
        system_file = os.path.join(system_dir, 'summary.%d.txt' % i)

        with open(model_file, 'w', encoding='utf-8') as f:
            f.write(model)
        with open(system_file, 'w', encoding='utf-8') as f:
            f.write(system)


if __name__ == '__main__':
    model_filename = 'gold_summaries.txt'
    system_filename = 'summary.txt'
    data = get_data_pairs(model_filename, system_filename)
    data_dir = 'data'
    write_data_for_eval(data_dir, data)