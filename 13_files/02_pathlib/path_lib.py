import os
from pathlib import Path

# Pathlib vs OS module
# Build paths inside the project like this: os.path.join(base_dir, 'subdir')
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Build paths inside the project like this: base_dir / 'subdir'
base_dir = Path(__file__).resolve().parent.parent

# Basic file operations
# Current file path
print(Path.cwd())

# Show list of file paths inside current path
for p in Path().iterdir():
    print(p)

# Path metadata
my_dir = Path('01_directory')
my_file = Path('01_file.txt')

print(my_dir.name)
print(my_file.name)

# Show with extension
print(my_dir.suffix)
print(my_file.suffix)

# Show without extension
print(my_dir.stem)
print(my_file.stem)

# Creating and checking paths
new_file_01 = my_dir / '01_new_file.txt'
new_file_02 = my_dir.joinpath('02_new_file.txt')

print(new_file_01)
print(new_file_02)

print(new_file_01.exists())  # False - not exist yet
print(new_file_02.exists())  # False - not exist yet

# Parent directories
print(my_dir.parent)  # .
print(my_file.parent)
print(new_file_01.parent)  # 01_directory
print(new_file_02.parent)

# Absolut path resolution
print(my_dir.absolute())
print(my_dir.resolve())

p = Path('..').resolve()
print(p)

p = Path(__file__).resolve().parent
print(p)

# Home directory manipulation
p = Path('~/dotfiles').expanduser()
print(p)
p = Path.home() / 'dotfiles'
print(p)

# Advanced file searching
dotfiles = Path.home() / "projects" / "python-practice"

# rglob - recursive searches globally
# by defaul case_sensitive is True
for p in dotfiles.rglob("*loop*", case_sensitive=False):
    print(p)

# Opening files
dotfiles = Path.home() / "projects" / "python-practice" / \
    "08_loops" / "while_loops.py"
with open(dotfiles) as f:
    print(f.read())

# Creading and Deleting
p = Path('temp_dir1')
if p.exists():
    p.rmdir()  # delete
p.mkdir()  # create

# subdirectory
p = Path('temp_dir/sub_dir')
if p.exists():
    p.rmdir()  # delete
p.mkdir(parents=True)  # create

# Moving and Renaming Files
p = Path('temp_file.txt')
p.touch()  # creates
if (temp := Path('TempFile.txt')).exists():
    temp.unlink()
p = p.rename('TempFile.txt')
p.replace('temp_file.txt')
