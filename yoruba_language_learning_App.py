import random
words = [
    {"yoruba": "ẹja", "english": "fish"},
    {"yoruba": "ọkọ", "english": "farm"},
    {"yoruba": "ilè", "english": "house"},
    {"yoruba": "àago", "english": "clock"},
    {"yoruba": "omó", "english": "child"},
    {"yoruba": "ọkọ", "english": "husband"},
    {"yoruba": "ìyá", "english": "mother"},
    {"yoruba": "bàbá", "english": "father"},
    {"yoruba": "omi", "english": "water"},
    {"yoruba": "osù", "english": "moon"},
    {"yoruba": "òrun", "english": "sky"},
    {"yoruba": "òkò", "english": "vehicle"},
    {"yoruba": "àjà", "english": "dog"},
    {"yoruba": "òlogbọ", "english": "cat"},
    {"yoruba": "ewé", "english": "leaf"},
    {"yoruba": "ìrìn", "english": "iron"},
    {"yoruba": "iṣẹ́", "english": "work"},
    {"yoruba": "ìsàlẹ̀", "english": "down"},
    {"yoruba": "òran", "english": "problem"},
    {"yoruba": "ire", "english": "good"},
    {"yoruba": "bàtà", "english": "shoe"},
    {"yoruba": "apá", "english": "arm"},
    {"yoruba": "ẹ̀rọ", "english": "machine"},
    {"yoruba": "ìdí", "english": "reason"},
    {"yoruba": "pẹ̀lú", "english": "with"},
    {"yoruba": "bẹ́ẹ̀ni", "english": "yes"},
    {"yoruba": "rárá", "english": "no"},
    {"yoruba": "jẹ", "english": "eat"},
    {"yoruba": "lọ", "english": "go"},
    {"yoruba": "wá", "english": "come"},
    {"yoruba": "kọ", "english": "write"},
    {"yoruba": "ka", "english": "read"},
    {"yoruba": "sọ", "english": "speak"},
    {"yoruba": "gbà", "english": "accept"},
    {"yoruba": "àlá", "english": "dream"},
    {"yoruba": "tí", "english": "if"},
    {"yoruba": "nítorí", "english": "because"},
    {"yoruba": "ifẹ", "english": "love"},
    {"yoruba": "kò", "english": "not"},
    {"yoruba": "mọ", "english": "know"},
    {"yoruba": "ní", "english": "have"},
    {"yoruba": "dá", "english": "create"},
    {"yoruba": "lẹ́yìn", "english": "after"},
    {"yoruba": "saaju", "english": "before"},
    {"yoruba": "eyìí", "english": "this"},
    {"yoruba": "iyẹn", "english": "that"},
    {"yoruba": "ẹ̀dá", "english": "being"},
    {"yoruba": "nǹkan", "english": "thing"},
    {"yoruba": "ilana", "english": "method"},
    {"yoruba": "afẹ́fẹ́", "english": "air"},
    {"yoruba": "àṣa", "english": "culture"},
    {"yoruba": "ẹnìyàn", "english": "person"},
    {"yoruba": "oṣu", "english": "month"},
    {"yoruba": "ọsẹ", "english": "week"},
    {"yoruba": "ọjọ́", "english": "day"},
    {"yoruba": "ọdún", "english": "year"},
    {"yoruba": "kó", "english": "gather"},
    {"yoruba": "dáhùn", "english": "answer"},
    {"yoruba": "pẹ́", "english": "long"},
    {"yoruba": "ṣé", "english": "do"},
    {"yoruba": "tan", "english": "spread"},
    {"yoruba": "wọn", "english": "they"},
    {"yoruba": "áwọn", "english": "them"},
    {"yoruba": "nítorí náà", "english": "therefore"},
    {"yoruba": "kì", "english": "who"},
    {"yoruba": "ki", "english": "when"},
    {"yoruba": "níbo", "english": "where"},
    {"yoruba": "báwo", "english": "how"},
    {"yoruba": "kí", "english": "what"},
    {"yoruba": "tó bá", "english": "until"},
    {"yoruba": "gbogbo", "english": "all"},
    {"yoruba": "tí gbogbo", "english": "everything"},
    {"yoruba": "ẹ̀kó", "english": "learning"},
    {"yoruba": "mo", "english": "I"},
    {"yoruba": "o", "english": "you"},
    {"yoruba": "àwa", "english": "we"},
    {"yoruba": "ẹ", "english": "you (plural)"},
    {"yoruba": "wọ́", "english": "they (plural)"},
    {"yoruba": "àwọn", "english": "those"},
    {"yoruba": "ní", "english": "at"},
    {"yoruba": "lati", "english": "to"},
    {"yoruba": "nibo", "english": "from"},
    {"yoruba": "pẹ̀lú", "english": "and"},
    {"yoruba": "kò sí", "english": "there is no"},
    {"yoruba": "sì", "english": "still"},
    {"yoruba": "jù", "english": "more"},
    {"yoruba": "tóbi", "english": "big"},
    {"yoruba": "kekere", "english": "small"},
    {"yoruba": "mà", "english": "do not"},
    {"yoruba": "tani", "english": "who"},
    {"yoruba": "bá", "english": "meet"},
    {"yoruba": "mo ní", "english": "I have"},
    {"yoruba": "mi o", "english": "I don't"},
    {"yoruba": "nítorí náà", "english": "so"},
    {"yoruba": "ẹ̀sìn", "english": "religion"},
    {"yoruba": "tìkò", "english": "nothing"}
]

def quiz_user(words, questionsPerRound=10):
    totalScore = 0
    totalRounds = len(words) // questionsPerRound + (1 if len(words)% questionsPerRound > 0 else 0)
    
    for roundNo in range(1, totalRounds+1):
        print(f"\n Round {roundNo} - Answer the following {min(questionsPerRound, len(words))} questions: ")
        random.shuffle(words)
        currRoundWords = words[:questionsPerRound]
        score = 0
        for word in currRoundWords:
            print(f"What is {word['yoruba']} in English?")
            userAnswer = input("Your answer: ").strip().lower()
            correctAnswer = word['english'].lower()
            
            if userAnswer == correctAnswer:
                print('Correct!!\n')
                score += 1
            else:
                print(f"Wrong. The correct answer is '{word['english']}'. \n")
        totalScore += score
        print(f"Round {roundNo} complete! Your score : {score}/ {len(currRoundWords)}")
        #remove answered words from the list
        words = words[questionsPerRound:]
        
        if words:
            continueQuiz = input("Do you want to go to the next round? (yes/no)")
            if continueQuiz != 'yes' or 'Yes' or 'y':
                break
        else:
            print(f"Quiz complete. You got {totalScore} out of 100 words right")
            break
        

def main():
    print("Welcome to the Language Learning App where we have 100 Yoruba words for you to practice")
    input("Press enter to start the quiz...")
    quiz_user(words)
    
if __name__ == "__main__":
    main()