def main():
    book_name = "books/frankenstein.txt"
    with open(book_name) as f:
        file_contents = f.read()
        word_count = count_words(file_contents)
        character_counts = count_characters(file_contents)
        create_report(word_count, character_counts, book_name)


def count_words(file_contents):
    return len(file_contents.split())


def count_characters(file_contents):
    character_count = {}
    for character in file_contents.lower():
        if character in character_count:
            character_count[character] += 1
        else:
            character_count[character] = 1
    return character_count


def convert_to_list_of_dicts_of_alphabets(character_counts):
    character_counts_list = []
    for character, count in character_counts.items():
        if not character.isalpha():
            continue
        character_counts_list.append({"character": character, "count": count})
    return character_counts_list


def sort_on(dict):
    return dict["count"]


def create_report(word_count, character_counts, book_name):
    header = f"--- Begin report of {book_name} ---"
    word_count_header = f"{word_count} words found in the {book_name}"
    footer = f"--- End report of {book_name} ---"
    charater_counts_list = convert_to_list_of_dicts_of_alphabets(
        character_counts)
    charater_counts_list.sort(key=sort_on, reverse=True)
    print(header)
    print(word_count_header)
    print("\n\n")
    for character_count in charater_counts_list:
        print(f"The '{character_count['character']}' character was found {character_count['count']} times.")  # noqa
    print('\n\n')
    print(footer)


if __name__ == "__main__":
    main()
