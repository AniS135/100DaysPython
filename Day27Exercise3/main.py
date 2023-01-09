# Use List data type to store the questions and their correct answer
# Display the final amount the person is taking home after playing the game

questions = ['1 Which of the following corresponds to ‘ek bataa do’?', 
            '2 Which of the following gods is also known as ‘Gauri Nandan’?', 
            '3 In the game of ludo the discs or tokens are of how many colours?',
            '4 Which of these are names of national parks located in Madhya Pradesh?',
            '5 Where was the BRICS summit held in 2014?',
            '6 Who wrote the introduction to the English translation of Rabindranath Tagore’s Gitanjali?',
            '7 Which of these leaders was a recipient of a gallantry award in 1987 by a state government for saving two girls from drowning?',
            '8 The wife of which of these famous sports persons was once captain of Indian volleyball team?',
            '9 Who is the only leader to be elected Prime Minister of Pakistan three times?',
            '10 Which of these terms can only be used for women?']

options = [['(A) Pura', '(B) Sawa', '(C) Adha', '(D) Pauna'],
            ['(A) Agni', '(B) Indra', '(C) Hanuman', '(D) Ganesha'],
            ['(A) One', '(B) Two', '(C) Three', '(D) Four'],
            ['(A) Krishna and Kanhaiya', '(B) Kanha and Madhav', '(C) Ghanshyam and Murari', '(D) Girdhar and Gopal'],
            ['(A) Brazil', '(B) India', '(C) Russia', '(D) China'],
            ['(A) P.B. Shelley', '(B) Alfred Tennyson', '(C) W.B. Yeats', '(D) T.S. Elliot'],
            ['(A) Anandiben Patel', '(B) Vasundhara Raje Scindia', '(C) Uma Bharti', '(D) Mamata Banerjee'],
            ['(A) K.D.Jadav', '(B) Dhyan Chand', '(C) Prakash Padukone', '(D) Milkha Singh'],
            ['(A) Syed Yousaf Raza Gillani', '(B) Benazir Bhutto', '(C) Liaqat Ali Khan', '(D) Nawaz Sharif'],
            ['(A) Dirghaayu', '(B) Suhagan', '(C) Chiranjeevi', '(D) Sushil']]

answers = ['C', 'D', 'D', 'B', 'A', 'C', 'A', 'D', 'D', 'B']

prizepool = [5000, 10000, 20000, 40000, 80000, 160000, 320000, 640000, 1250000, 2500000]

name = input("Enter your name : ")
print(f"Congratulations {name} fastest finger first round jeetke aap aagaye hm hot seat par")
print("Aur isse ke saath shuru karte hn Kaun Banega Crorepati")

amount = 0

for i in range(10):
    print(f"Toh agla sawal {prizepool[i]}Rs ke liye yeah raha aapki screen pe")
    print(questions[i])

    for op in options[i]:
        print(op)

    optionchoosen = input("Enter the choosen option from (A, B, C, D) : ")

    if(optionchoosen == answers[i]):
        if i == 9 :
            print("Congratulations Kaun Banega Crorepati Jeet liya hn saare swalo ke sahi jawab deke")
        else :
            print(f"Sahi jawab aur isse ke saath aap jeette hn {prizepool[i]}Rs")
        amount = prizepool[i]
    else:
        print("Sorry aapka jawab galat hn, aur isse ke saath khel yahi khatam hota hn")
        break

print(f"Toh isse ke saath app Kaun Banega Crorepati se jeet ke jaa rahe hn puree {amount}Rs")
    
