from puzzle import Puzzle

def load_word_list(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file]

def main():
    word_list = load_word_list('C:\\Users\\Shahr\\Desktop\\Task\\Dsa\\Tasks\\Data\\word.txt')
    puzzle = Puzzle(20, word_list)
    puzzle.generate()
    puzzle.display()

if __name__ == "__main__":
    main()