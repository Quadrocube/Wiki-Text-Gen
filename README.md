#Simple Wiki-Taught Markov Text Generator 
  
##Usage 
`./run-all.sh LINK_COUNT DOMAIN`
  
##Disclaimer
*This* is a (a little bit more advanced than totally dummy) example of a 
weekend-long project to improve your skills at Python programming and general problem solving.  
It covers rather broad variety of topics including:
- Basic python syntax and libs
- Networking and html processing (with `BeautifulSoup` and `urllib`)
- Separation code in logic parts (one can go further and introduce an 
object-oriented hierarchy of classes)
- Serialization (with `pickle`)
- (Primitive) data mining and processing
- (Primitive) statistic models
- (Not implemented here but highly encouraged) Python multithreading for bfs-like-crawl part
- (Optional) possibility to interactively play with the model in IPython notebook 
  
##Double-Disclaimer:
I acknowledge that the code is *awfully* undocumented and I *will* try to fix it someday not to call the rage of open-source-karma-gods upon my shoulders.
  
##Comments
For all of you wondering about the misterious Markov model -- the basic idea (completely satisfactory for the means of this project though) is to assume that there exists a probability distribution on the words in a text that relies solely on the n words (grams) that precede it. And your task is to infer this probability distribution. The code in this repo takes the 3-gram model to analyze the text and the maximum-likelihood function to generate new texts. See `analyze_data.py` and `generate_text.py`. Also google n-gram-based text generation.
  
P.s. LurkMOAR!
