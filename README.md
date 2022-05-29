# zyzzyva_anki
Convert zyzzyva output to anki flashcards

The repository contains two python file that can convert zyzzyva output to Anki cards. 

The only file that is needed to run is the convert_zyz_to_anki.py This requires a few things to run.  You need to make an appropriate output file from Zyzzyva.  To do this you need to follow the following steps in Zyzzyva

# Generating a list with Zyzzyva
1) Generate the desired list with the search function
2) Right click on the list in the main window, select "Save List"
3) Change the "Format" box to "Anagram Question/Answer
4) Make sure the last column is either "Playability Order" or "Probability Order" depending on which order you want to study
5) Make sure you include Lexicon symbols if you want
6) Save the file

At this point you should have a raw file with input lines that look like this:

    Q: EIILLOPRS
    A:  PILLORIES  PILLORY, to hold up to public ridicule [v] 13574
    A:  PILLORISE# d#s# to pillory, also PILLORIZE [v PILLORISED, PILLORISING, PILLORISES] 13575

This example includes lexicon symbols, front hooks (there are none) back hooks, definitions, and playability order

Before converting to anki, you need to do one more thing.  If you've used definitions, you need to edit the whole file to remove any appearances of semicolons ";".  A symbol find replace, switching semicolons with commas is good enough.  This is because we will use semicolons as a delimiter for Anki

# Converting to Anki
After that you're ready to go.  In the "convert_zyz_to_anki.py" file edit the "filename" field to be the file you just made, and the "writefile" field to be the location to save the file to.  Then you should be able to run the script.  You should get outputs like:

    EIILLOPRS (2); PILLORIES PILLORY, to hold up to public ridicule [v] <br>PILLORISE# d#s# to pillory, also PILLORIZE# [v PILLORISED#, PILLORISING#, PILLORISES#]
    
The ";" provides the difference between the front part of the card and the back part of the card
    
(You'll notice that the definitions also have CSW marks for PILLORIZE# and the inflections.  If you want to do this also, you'll need to run the second file, but if you don't care about marking words with # properly you can go right ahead to importint to anki

# Importing to Anki

In Anki on the computer, you will go to File -> Import.  You will then need to select the file you just created.  In the "Fields Separated By" column, select "semicolon", Make sure you check the box for "Allow HTML in Fields".  For the "Type" field on the top left select Basic.  You can either import the cards into an existing deck or create a new deck.  Congrats, you now have an anki deck!

# Edit raw defs

edit_raw_defs.py is an extra file that will edit the definitions of a zyzzyva output so that all the words in the definition have the correct symbol (#).  That is, it will read through the definitions of a word, extract all the words with only capital letters, and check them against a CSW list.  That is it will mark the following definition as such.  This acts on the output from zyzzyva, so it needs to be done before you've converted to Anki, if you want it.

    GALLABEAH# s# (Arabic) a cloak with a hood and wide sleeves, also DJELLABA, DJELLABAH, GALABEA#, GALABEAH#, GALABIA, GALABIAH#, GALABIEH, GALABIYA, GALABIYAH, GALLABEA#, GALLABIA#, GALLABIAH#, GALLABIEH#, GALLABIYA#, GALLABIYAH#, GALLABIYEH#, JELAB#, JELLABA, JELLABAH#
    
To run this file you'll need to generate a full list of the CSW words with the proper lexicon symbols.  It should be a simple word list that looks something like this

    ...
    ABAMP
    ABAMPERE
    ABAMPERES
    ABAMPS
    ABAND#
    ABANDED#
    ABANDING#
    ...
    
 This can be done with Zyzzyva provided you have an up to date copy of the CSW and NWL word lists and a powerful enough computer (sometimes zyzzyva can crash when trying to make long lists like this).
