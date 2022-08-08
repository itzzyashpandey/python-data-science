from data import story
print(f"total chars in story: {len(story)}")
words=story.split()
print(f"total words in story: {len(words)}")
print(f"total unique words in story: {len(set(story))}")
print(words)

sentences=story.split('.')
print(f"total sentences in story: {len(sentences)}")

lines=story.split('\n')
print(f"total lines in story: {len(lines)}")

poem_list=[
    'twinkle twinkle little star,',
    "how i wonder what you are ,",
    "up above the world soo high ",
    "like a dimond in the  sky ",
    
]

poem="\n".join(poem_list)
print(poem)
poem=poem.replace(' ','')
print(poem)