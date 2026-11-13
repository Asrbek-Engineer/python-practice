try:
    f = open('testfile.txt')
except Exception:  # General catch
    print('Sorry. This file does not exist')

try:
    f = open('testfile.txt')
except FileNotFoundError:
    print('Sorry. This file does not exist')

try:
    f = open('test_file.txt')
    var = bad_var
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print(e)

try:
    f = open('test_file.txt')
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print(e)
else:  # executes if try part passes successfully
    print(f.read())
    f.close()
finally:  # executes after all process done in try except
    print('Executing Finally...')


try:
    f = open('currupt_file.txt')
    # if f.name == 'currupt_file.txt':
    #     raise Exception
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print('Error!')
else:
    print(f.read())
    f.close()
finally:
    print('Executing Finally...')
