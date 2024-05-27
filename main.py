def main():
    build_report("./books/frankenstein.txt")

def count_words(str):
    return len(str.split())

def count_letters(str):
    letters_dict = {}

    lowered_str = str.lower()

    for c in lowered_str:
        if c in letters_dict:
            letters_dict[c] += 1
        else:
            letters_dict[c] = 1
    
    return letters_dict

def build_report(path):
    print(f"--- Begin report of {path} ---")
    with open("./books/frankenstein.txt") as f:
        file_contents = f.read()
        word_count = count_words(file_contents)
        print(f"{word_count} words found in the document")

        letter_count = count_letters(file_contents)
        letters_dict_list = []

        for (key, value) in letter_count.items():
            if key.isalpha():
                letters_dict_list.append({"character": key, "count": value})
        
        letters_dict_list.sort(reverse=True, key=sort_on)

        for dict in letters_dict_list:
            print(f"The '{dict["character"]}' character was found {dict["count"]} times")

        print("--- End report ---")

def sort_on(dict):
    return dict["count"]

main()