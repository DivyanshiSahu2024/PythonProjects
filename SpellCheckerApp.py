#Step1 importing the required library 
# a third party library that provides readymade functions to detect and correct the spelling mistakes
from spellchecker import SpellChecker

#Step2 creating the app class
#Advantage of building a class is that it allows us to encapsulate the functionality of the spell checker in a single unit, making it easier to manage and extend in the future.
class SpellCheckerApp:
    def __init__(self):
        self.spell=SpellChecker()

    def correct_text(self,text):
        words= text.split() 
        corrected_words=[]

        for word in words:
            corrected_word=self.spell.correction(word)
            if corrected_word !=word.lower():
                print(f'Correcting"{word}" to "{corrected_word}"')
            corrected_words.append(corrected_word)
                
            #Step-4 : Returning the corrected text  
        return ' '.join(corrected_words)
            

#Step-5 running the app

    def run(self):
        print("\n ----SPELL CHECKER APP----")

        while True:
            text=input('Enter text to check (or type "exit" to quit): ')

            if text.lower()=="exit":
                print('Closing the program.....')
                break
            corrected_text=self.correct_text(text)
            print(f'Corrected Text:{corrected_text}')

#STEP-6 running the main program
if __name__=="__main__":
    SpellCheckerApp().run()     
