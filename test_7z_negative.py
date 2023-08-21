from checkout import checkout_negative
import yaml

with open("config.yaml") as f:
    data = yaml.safe_load(f)


def test_step1(clear_folders, make_files, make_badarx):
    assert checkout_negative("cd {}; 7z e badarx.7z -o{} -y".format(data['folder_out'], data['folder_ext']),
                             "ERROR"), "Test1 Fail"


def test_step2(clear_folders, make_files, make_badarx):
    assert checkout_negative("cd {}; 7z t badarx.7z".format(data['folder_out']), "ERROR"), "Test2 Fail"