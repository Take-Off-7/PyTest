def test_tmpdir(tmpdir):
    print(f"Temporary directory: {tmpdir}")
    a_file = tmpdir.join('something.txt')
    a_sub_dir = tmpdir.mkdir('anything')
    another_file = a_sub_dir.join('something_else.txt')

    a_file.write('contents may settle during shipping')
    another_file.write('something different')

    print("Root contents:", tmpdir.listdir())
    print("Subdirectory contents:", a_sub_dir.listdir())

    assert a_file.read() == 'contents may settle during shipping'
    assert another_file.read() == 'something different'


def test_tmpdir_factory(tmpdir_factory):
    a_dir = tmpdir_factory.mktemp('mydir')
    base_temp = tmpdir_factory.getbasetemp()
    print('base: ', base_temp)
    print('temporary_dir: ', a_dir)

    a_file = a_dir.join('something.txt')
    a_sub_dir = a_dir.mkdir('anything')
    another_file = a_sub_dir.join('something_else.txt')

    a_file.write('contents may settle during shipping')
    another_file.write('something different')

    assert a_file.read() == 'contents may settle during shipping'
    assert another_file.read() == 'something different'

