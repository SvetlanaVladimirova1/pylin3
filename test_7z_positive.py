from checkout import checkout_positive
import yaml

with open("config.yaml") as f:
    data = yaml.safe_load(f)


def test_step1(make_folders, clear_folders, make_files):
    res1 = checkout_positive("cd {}; 7z a {}/arx1.7z".format(data['folder_in'], data['folder_out']),
                             "Everything is Ok"), "Test1 Fail"
    res2 = checkout_positive("ls {}".format(data['folder_out']), "arx1.7z"), "Test1 Fail"
    assert res1 and res2, "Test Fail"


def test_step2(clear_folders, make_files):
    res = []
    res.append(
        checkout_positive("cd {}; 7z a {}/arx1.7z".format(data['folder_in'], data['folder_out']), "Everything is Ok"))
    res.append(checkout_positive("cd {}; 7z e arx1.7z -o{} -y".format(data['folder_out'], data['folder_ext']),
                                 "Everything is Ok"))
    for item in make_files:
        res.append(checkout_positive("ls {}".format(data['folder_ext']), item))
    assert all(res)


def test_step3():
    assert checkout_positive("cd {}; 7z t {}/arx1.7z".format(data['folder_in'], data['folder_out']),
                             "Everything is Ok"), "Test1 Fail"


def test_step4():
    assert checkout_positive("cd {}; 7z u {}/arx1.7z".format(data['folder_in'], data['folder_out']),
                             "Everything is Ok"), "Test1 Fail"


def test_step5(clear_folders, make_files):
    res = []
    res.append(
        checkout_positive("cd {}; 7z a {}/arx1.7z".format(data['folder_in'], data['folder_out']), "Everything is Ok"))
    for item in make_files:
        res.append(checkout_positive("cd {}; 7z l arx1.7z".format(data['folder_out']), item))
    assert all(res)


def test_step7():
    assert checkout_positive("7z d {}/arx1.7z".format(data['folder_out']), "Everything is Ok"), "Test1 Fail"