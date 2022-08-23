# Binairo scripts
Scripts for generating a book full of binairo puzzles.

1. First create a file called `puzzles.txt` with every line being `size puzzle solution`, save this in the root of this directory.
2. Create a folder called `images` in the root of this directory.
3. Next run the python script as `python src/main.py`.
4. Now open and compile the generated `booklet.tex`.
5. Now run `./2up.sh booklet.pdf`, this will give you the final booklet.

# Arch packages
For Arch make sure the following packages are installed: `clang`, `z3` and `texlive-latexextra`.
