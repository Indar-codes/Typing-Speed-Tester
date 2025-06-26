import time
import random

sentences = [
    "Python is a powerful programming language.",
    "Typing fast improves productivity.",
    "Learning to code opens up new opportunities.",
    "GitHub is a platform for hosting code.",
    "Consistency beats motivation in the long run."
]

def calculate_wpm(start, end, typed_text):
    time_taken = end - start
    words = len(typed_text.split())
    wpm = (words / time_taken) * 60
    return round(wpm, 2)

def calculate_accuracy(original, typed):
    original_words = original.split()
    typed_words = typed.split()
    correct = 0

    for o, t in zip(original_words, typed_words):
        if o == t:
            correct += 1

    accuracy = (correct / len(original_words)) * 100
    return round(accuracy, 2)

def typing_test():
    print("⌨️ Typing Speed Tester\n")
    input("Press Enter to start...")
    sentence = random.choice(sentences)
    print("\nType this sentence:\n")
    print(f"👉 {sentence}\n")

    start_time = time.time()
    typed = input("\nYour input: ")
    end_time = time.time()

    wpm = calculate_wpm(start_time, end_time, typed)
    accuracy = calculate_accuracy(sentence, typed)

    print(f"\n⏱️ Time Taken: {round(end_time - start_time, 2)} seconds")
    print(f"🚀 WPM: {wpm}")
    print(f"🎯 Accuracy: {accuracy}%")

typing_test()
