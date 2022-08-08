from data import story

print(f"total lenngth of story: {len(story)}")

#counting substring in alarge string
#counting a particular character
a_count=story.count('a')
print(f"a occur:{(a_count)} times")

the_count=story.lower().count('the')
print(f"the occur:{(the_count)} times")

# repalce
ustory= story.replace('o','a')
print(ustory) 

#removing data
ustory= story.replace('of','')
print(ustory)

#removing all words
no_vowel_story=story.replace('a','').replace('e','').replace('i','').replace('o','').replace('u','')
print(no_vowel_story)

#retaining all vowels
only_vowel_story=''
for char in story:
    if char in 'aeiouAEIOU ':
        only_vowel_story+= char
print(only_vowel_story)        