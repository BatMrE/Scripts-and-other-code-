from collections import Counter 
  
text = "Python is an interpreted, high-level, general-purpose programming language. Created by Guido van Rossum and first released in 1991, Python's design philosophy emphasizes code readability with its notable use of significant whitespace. Its language constructs and object-oriented approach aim to help programmers write clear, logical code for small and large-scale projects.[28] Python is dynamically typed and garbage-collected. It supports multiple programming paradigms, including structured (particularly, procedural), object-oriented, and functional programming. Python is often described as a 'batteries included' language due to its comprehensive standard library Python was conceived in the late 1980s as a successor to the ABC language. Python 2.0, released in 2000, introduced features like list comprehensions and a garbage collection system with reference counting"
  
def commonWord(text):
    split_it = text.split() 
    counter = Counter(split_it) 
    trendingWord = counter.most_common(4) 
      
    #most_occur is of type list 
    print(trendingWord) 
    
    #To access the data
    #most_occur[1]
    
commonWord(text)    