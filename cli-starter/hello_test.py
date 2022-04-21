import hello


def test_main(capsys):
    # capture system output
    hello.main(['Jay'])
    out, err = capsys.readouterr()
    assert out == 'Hello Smexy Person Jay\n'
    assert err == ''


def test_main_error_with_empty_string(capsys):
    # with pytest.raises(SystemExit) as excinfo:
    #     hello.main([''])
    # retv, = excinfo.value.args
    # assert retv == 1
    hello.main([''])
    out, err = capsys.readouterr()
    assert out == ''
    assert err == "Person's name must not be empty!\n"
