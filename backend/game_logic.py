from collections import Counter


def word_checker(guess_word: str, secret_word: str) -> list:
    results = []
    countered_letters = Counter(secret_word)

    # Check for right letters on right positions
    for guess_letter, correct_letter in zip(guess_word, secret_word):
        if guess_letter == correct_letter:
            result = 1
            countered_letters[guess_letter] -= 1
        else:
            result = 0
        results.append({"letter": guess_letter, "result": result})

    # Check for right letters on wrong positions
    counter = 0
    for guess_letter, correct_letter in zip(guess_word, secret_word):
        if guess_letter == correct_letter:
            counter += 1
            continue
        if guess_letter in secret_word and countered_letters[guess_letter] > 0:
            result = 2
            countered_letters[guess_letter] -= 1
        else:
            result = 0
        results[counter].update({"letter": guess_letter, "result": result})
        counter += 1

    return results
