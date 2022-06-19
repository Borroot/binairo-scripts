import load
import pic
import latex

def main():
    filename_puzzles = "puzzles.txt"
    filename_booklet = "booklet.tex"
    folder_images = "images"

    # load all the generated puzzles
    puzzles = load.loadpuzzles(filename_puzzles)

    # convert the puzzles to images
    for index, puzzle in enumerate(puzzles):
        print(f"creating {folder_images}/{index:02d}p.png")
        pic.draw(puzzle["puzzle"],   f"{folder_images}/{index:02d}p")
        print(f"creating {folder_images}/{index:02d}s.png")
        pic.draw(puzzle["solution"], f"{folder_images}/{index:02d}s")

    # put the images in a latex file
    with open(filename_booklet, "w") as f:
        tex = latex.booklet(folder_images, len(puzzles))
        f.seek(0)
        f.write(tex)
        f.truncate()

if __name__ == "__main__":
    main()
