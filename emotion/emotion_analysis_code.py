# import pandas as pd
# import numpy as np
# import nltk
# import re
# import pickle
# import itertools
# from nltk.stem.wordnet import WordNetLemmatizer 
# from django.conf import settings
# import os
# from sklearn.svm import SVC
# import sklearn.svm
# import types

# sklearn.svm.classes = types.SimpleNamespace(SVC=sklearn.svm.SVC)



# # tweet = 'Layin n bed with a headache  ughhhh...waitin on your call...'

# class emotion_analysis_code():

#     lem = WordNetLemmatizer()

#     def cleaning(self, text):
#         txt = str(text)
#         txt = re.sub(r"http\S+", "", txt)
#         if len(txt) == 0:
#             return 'no text'
#         else:
#             txt = txt.split()
#             index = 0
#             for j in range(len(txt)):
#                 if txt[j][0] == '@':
#                     index = j
#             txt = np.delete(txt, index)
#             if len(txt) == 0:
#                 return 'no text'
#             else:
#                 words = txt[0]
#                 for k in range(len(txt)-1):
#                     words+= " " + txt[k+1]
#                 txt = words
#                 txt = re.sub(r'[^\w]', ' ', txt)
#                 if len(txt) == 0:
#                     return 'no text'
#                 else:
#                     txt = ''.join(''.join(s)[:2] for _, s in itertools.groupby(txt))
#                     txt = txt.replace("'", "")
#                     txt = nltk.tokenize.word_tokenize(txt)
#                     #data.content[i] = [w for w in data.content[i] if not w in stopset]
#                     for j in range(len(txt)):
#                         txt[j] = self.lem.lemmatize(txt[j], "v")
#                     if len(txt) == 0:
#                         return 'no text'
#                     else:
#                         return txt

#     def predict_emotion(self, tweet):
#         import sklearn.svm
#         import types

#     # Patch the old import path for backward compatibility
#         sklearn.svm.classes = types.SimpleNamespace(SVC=sklearn.svm.SVC)

#         tweet_in_pandas = pd.Series(' '.join(self.cleaning(tweet)))

#         path_vec = os.path.join(settings.MODELS, 'vectorizer.pickle')
#         path_model = os.path.join(settings.MODELS, 'finalized_model.sav')

#     # Load vectorizer
#         with open(path_vec, 'rb') as f_vec:
#             vectorizer = pickle.load(f_vec)
#         # import pickle
#     # Load trained model
#         with open(path_model, 'rb') as f_model:
#             model = pickle.load(f_model)
        
#         with open('finalized_model.sav', 'wb') as f:
#             pickle.dump(model, f)
#         #         # # Load trained model
#         # with open(path_model, 'rb') as f_model:
#         #     model = pickle.load(f_model)


#     #     test = vectorizer.transform(tweet_in_pandas)
#     #     predicted_sentiment = model.predict(test)
#     #     final_sentiment = predicted_sentiment[0]

#     # # Convert raw prediction to readable emotion
#     #     emotion_map = {
#     #         'worry': 'Worry',
#     #         'sadness': 'Sadness',
#     #             'happiness': 'Happiness',
#     #         'love': 'Love',
#     #         'hate': 'Hate'
#     #     }

#     #     return emotion_map.get(final_sentiment, 'Unknown')




#         test = vectorizer.transform(tweet_in_pandas)
#         predicted_sentiment = model.predict(test)
#         final_sentiment = (predicted_sentiment[0])
#         if final_sentiment == 'worry':
#             return 'Worry'
#         elif final_sentiment == 'sadness':
#             return 'Sadness'
#         elif final_sentiment == 'happiness':
#             return 'Happiness'
#         elif final_sentiment == 'love':
#             return 'Love'
#         elif final_sentiment == 'hate':
#             return 'Hate'
# import pandas as pd
# import numpy as np
# import nltk
# import re
# import pickle
# import itertools
# from nltk.stem.wordnet import WordNetLemmatizer 
# from django.conf import settings
# import os

# # tweet = 'Layin n bed with a headache  ughhhh...waitin on your call...'

# class emotion_analysis_code():

#     lem = WordNetLemmatizer()

#     def cleaning(self, text):
#         txt = str(text)
#         txt = re.sub(r"http\S+", "", txt)
#         if len(txt) == 0:
#             return 'no text'
#         else:
#             txt = txt.split()
#             index = 0
#             for j in range(len(txt)):
#                 if txt[j][0] == '@':
#                     index = j
#             txt = np.delete(txt, index)
#             if len(txt) == 0:
#                 return 'no text'
#             else:
#                 words = txt[0]
#                 for k in range(len(txt)-1):
#                     words+= " " + txt[k+1]
#                 txt = words
#                 txt = re.sub(r'[^\w]', ' ', txt)
#                 if len(txt) == 0:
#                     return 'no text'
#                 else:
#                     txt = ''.join(''.join(s)[:2] for _, s in itertools.groupby(txt))
#                     txt = txt.replace("'", "")
#                     txt = nltk.tokenize.word_tokenize(txt)
#                     data.content[i] = [w for w in data.content[i] if not w in stopset]
#                     for j in range(len(txt)):
#                         txt[j] = self.lem.lemmatize(txt[j], "v")
#                     if len(txt) == 0:
#                         return 'no text'
#                     else:
#                         return txt

#     def predict_emotion(self, tweet):

#         tweet_in_pandas = pd.Series(' '.join(self.cleaning(tweet)))

#         path_vec = os.path.join(settings.MODELS, 'vectorizer.pickle')
#         path_model = os.path.join(settings.MODELS, 'finalized_model.sav')

#         # load vectorizer
#         # vec_file = 'vectorizer.pickle'
#         vectorizer = pickle.load(open(path_vec, 'rb'))

#         # load trained model
#         # filename = 'finalized_model.sav'
#         model = pickle.load(open(path_model, 'rb'))




#         test = vectorizer.transform(tweet_in_pandas)
#         predicted_sentiment = model.predict(test)
#         final_sentiment = (predicted_sentiment[0])
#         if final_sentiment == 'worry':
#             return 'Worry'
#         elif final_sentiment == 'sadness':
#             return 'Sadness'
#         elif final_sentiment == 'happiness':
#             return 'Happiness'
#         elif final_sentiment == 'love':
#             return 'Love'
#         elif final_sentiment == 'hate':
#             return 'Hate'


# import pandas as pd
# import numpy as np
# import nltk
# import re
# import pickle
# import itertools
# from nltk.stem.wordnet import WordNetLemmatizer
# from django.conf import settings
# import os
# from sklearn.svm import SVC
# import sklearn.svm
# import types
# import sys

# # Better compatibility patch that will work when loading the model
# # Apply the patch before any pickle loading happens
# if not hasattr(sklearn.svm, 'classes'):
#     # Create the missing module structure to ensure backward compatibility
#     sklearn.svm.classes = types.ModuleType('sklearn.svm.classes')
#     sys.modules['sklearn.svm.classes'] = sklearn.svm.classes
#     sklearn.svm.classes.SVC = sklearn.svm.SVC

# class emotion_analysis_code():
#     lem = WordNetLemmatizer()
    
#     def __init__(self):
#         # Pre-load the model and vectorizer on initialization to avoid loading them for each prediction
#         self.vectorizer = vectorizer
#         self.model = model
#         self.emotions = ['happy', 'love', 'sad', 'anger', 'surprised']
        
#     def load_model_and_vectorizer(self):
#         """Load model and vectorizer if not already loaded"""
#         if self.model is None or self.vectorizer is None:
#             path_vec = os.path.join(settings.MODELS, 'vectorizer.pickle')
#             path_model = os.path.join(settings.MODELS, 'finalized_model.sav')
            
#             # Load vectorizer
#             try:
#                 with open(path_vec, 'rb') as f_vec:
#                     self.vectorizer = pickle.load(f_vec)
#             except Exception as e:
#                 raise Exception(f"Failed to load vectorizer: {str(e)}")
                
#             # Load trained model
#             try:
#                 with open(path_model, 'rb') as f_model:
#                     self.model = pickle.load(f_model)
#             except Exception as e:
#                 raise Exception(f"Failed to load model: {str(e)}")
                
#     def cleaning(self, text):
#         """Clean and preprocess text data"""
#         txt = str(text)
#         txt = re.sub(r"http\S+", "", txt)
        
#         if len(txt) == 0:
#             return 'no text'
            
#         txt = txt.split()
#         # Remove mentions (@username)
#         txt = [word for word in txt if not word.startswith('@')]
        
#         if len(txt) == 0:
#             return 'no text'
            
#         # Join words back together
#         txt = ' '.join(txt)
#         # Remove non-word characters
#         txt = re.sub(r'[^\w]', ' ', txt)
        
#         if len(txt) == 0:
#             return 'no text'
            
#         # Handle repeated characters (limit to 2)
#         txt = ''.join(''.join(s)[:2] for _, s in itertools.groupby(txt))
#         txt = txt.replace("'", "")
        
#         # Tokenize
#         txt = nltk.tokenize.word_tokenize(txt)
        
#         # Lemmatize
#         txt = [self.lem.lemmatize(word, "v") for word in txt]
        
#         if len(txt) == 0:
#             return 'no text'
            
#         return txt


#     def predict_emotion(self, tweet):
#         """Predict emotion from tweet text"""
#         # Ensure model and vectorizer are loaded
#         self.load_model_and_vectorizer()
        
#         # Clean the tweet
#         cleaned_tweet = self.cleaning(tweet)
#         if cleaned_tweet == 'no text':
#             return 'Neutral'  # Default response for empty/invalid text
            
#         # Convert to format expected by vectorizer
#         tweet_in_pandas = pd.Series(' '.join(cleaned_tweet))
        
#         # # Transform and predict
#         try:
#             test = self.vectorizer.transform(tweet_in_pandas)
#             predicted_sentiment = self.model.predict(test)
#             final_sentiment = predicted_sentiment[0]
#         except Exception as e:
#             print(f"Prediction error: {str(e)}")
#             return 'Error'
            
#         # # Map raw prediction to readable emotion
#         emotion_map = {
#             'worry': 'Worry',
#             'sadness': 'Sadness',
#             'happiness': 'Happiness',
#             'love': 'Love',
#             'hate': 'Hate'
#         }
        
#         return emotion_map.get(final_sentiment, 'Unknown')
        
import pandas as pd
import numpy as np
import nltk
import re
import pickle
import itertools
from nltk.stem.wordnet import WordNetLemmatizer
from django.conf import settings
import os
from sklearn.svm import SVC
import sklearn.svm
import types
import sys

# Better compatibility patch that will work when loading the model
# Apply the patch before any pickle loading happens
if not hasattr(sklearn.svm, 'classes'):
    # Create the missing module structure to ensure backward compatibility
    sklearn.svm.classes = types.ModuleType('sklearn.svm.classes')
    sys.modules['sklearn.svm.classes'] = sklearn.svm.classes
    sklearn.svm.classes.SVC = sklearn.svm.SVC

class emotion_analysis_code():
    lem = WordNetLemmatizer()
    
    def __init__(self):
        # Initialize the model and vectorizer as None first
        self.vectorizer = None
        self.model = None
        self.emotions = ['happy', 'love', 'sad', 'anger', 'surprised']
        # Load model and vectorizer immediately to avoid issues
        self.load_model_and_vectorizer()
        
        # Backup dictionary-based approach for when the model fails
        self.emotion_words = {
            'happiness': ['happy', 'joy', 'delighted', 'glad', 'pleased', 'happiness', 'cheerful', 'excited', 'yay', 'enjoy', 
                    'wonderful', 'great', 'awesome', 'excellent', 'fantastic', 'thrilled', 'ecstatic', 'content', 'satisfied'],
            'sadness': ['sad', 'unhappy', 'depressed', 'downcast', 'miserable', 'heartbroken', 'crying', 'depressing', 
                        'sorrow', 'grief', 'disappointed', 'upset', 'down', 'blue', 'gloomy', 'melancholy', 'hopeless', 'despair','anymore'],
            'hate': ['angry', 'furious', 'mad', 'annoyed', 'irritated', 'enraged', 'hate', 'frustrating', 'outraged', 
                      'resent', 'disgusted', 'offended', 'frustrated', 'bitter', 'hostile', 'dislike'],
            'worry': ['afraid', 'scared', 'terrified', 'frightened', 'nervous', 'worried', 'anxious', 'panic', 'horror', 
                     'terror', 'dread', 'alarmed', 'fearful', 'paranoid', 'concern', 'uneasy', 'stress', 'stressed'],
            'love': ['love', 'adore', 'cherish', 'loving', 'fond', 'affection', 'like', 'passionate', 'devotion',
                     'romantic', 'infatuated', 'smitten', 'admire', 'appreciate', 'care', 'beloved', 'dear']
        }
        
    def load_model_and_vectorizer(self):
        """Load model and vectorizer if not already loaded"""
        if self.model is None or self.vectorizer is None:
            try:
                path_vec = os.path.join(settings.MODELS, 'vectorizer.pickle')
                path_model = os.path.join(settings.MODELS, 'finalized_model.sav')
                
                # Load vectorizer with error handling
                try:
                    with open(path_vec, 'rb') as f_vec:
                        self.vectorizer = pickle.load(f_vec)
                except Exception as e:
                    print(f"Failed to load vectorizer: {str(e)}")
                    # Create a fallback for testing
                    self.vectorizer = None
                    
                # Load trained model with error handling
                try:
                    with open(path_model, 'rb') as f_model:
                        self.model = pickle.load(f_model)
                except Exception as e:
                    print(f"Failed to load model: {str(e)}")
                    # Create a fallback for testing
                    self.model = None
            except Exception as e:
                print(f"Error in path configuration: {str(e)}")
                self.vectorizer = None
                self.model = None
                
    def cleaning(self, text):
        """Clean and preprocess text data"""
        txt = str(text)
        txt = re.sub(r"http\S+", "", txt)
        
        if len(txt) == 0:
            return 'no text'
            
        txt = txt.split()
        # Remove mentions (@username)
        txt = [word for word in txt if not word.startswith('@')]
        
        if len(txt) == 0:
            return 'no text'
            
        # Join words back together
        txt = ' '.join(txt)
        # Remove non-word characters
        txt = re.sub(r'[^\w]', ' ', txt)
        
        if len(txt) == 0:
            return 'no text'
            
        # Handle repeated characters (limit to 2)
        txt = ''.join(''.join(s)[:2] for _, s in itertools.groupby(txt))
        txt = txt.replace("'", "")
        
        # Tokenize
        txt = nltk.tokenize.word_tokenize(txt)
        
        # Lemmatize
        txt = [self.lem.lemmatize(word, "v") for word in txt]
        
        if len(txt) == 0:
            return 'no text'
            
        return txt

    def fallback_emotion_detection(self, text):
        """Dictionary-based fallback for emotion detection"""
        text = text.lower()
        scores = {emotion: 0 for emotion in self.emotion_words.keys()}
        
        # Check for exact words
        for emotion, words in self.emotion_words.items():
            for word in words:
                if word in text:
                    scores[emotion] += 1
        
        # Special cases for common expressions
        if "i love" in text:
            scores["love"] += 3
        if "i am happy" in text or "i'm happy" in text:
            scores["happiness"] += 3
        if "i hate" in text:
            scores["hate"] += 3
        if "i am sad" in text or "i'm sad" in text:
            scores["sadness"] += 3
            
        # Find the highest scoring emotion
        max_score = max(scores.values())
        if max_score == 0:
            return 'Neutral'
        
        # Get the emotion with the highest score
        max_emotions = [emotion for emotion, score in scores.items() if score == max_score]
        # Capitalize first letter for consistency
        return max_emotions[0].capitalize()

    def predict_emotion(self, tweet):
        """Predict emotion from tweet text"""
        # Handle empty tweets
        if not tweet or tweet.strip() == '':
            return 'Neutral'
            
        # Try using the ML model first
        if self.vectorizer is not None and self.model is not None:
            try:
                # Clean the tweet
                cleaned_tweet = self.cleaning(tweet)
                if cleaned_tweet == 'no text':
                    return 'Neutral'  # Default response for empty/invalid text
                    
                # Convert to format expected by vectorizer
                tweet_in_pandas = pd.Series(' '.join(cleaned_tweet))
                
                # Transform and predict
                test = self.vectorizer.transform(tweet_in_pandas)
                predicted_sentiment = self.model.predict(test)
                final_sentiment = predicted_sentiment[0]
                
                # Map raw prediction to readable emotion
                emotion_map = {
                    'worry': 'Worry',
                    'sadness': 'Sadness',
                    'happiness': 'Happiness',
                    'love': 'Love',
                    'hate': 'Hate'
                }
                
                return emotion_map.get(final_sentiment, 'Unknown')
                
            except Exception as e:
                print(f"ML model prediction error: {str(e)}")
                # If the ML approach fails, try the fallback approach
                return self.fallback_emotion_detection(tweet)
        else:
            # If model or vectorizer couldn't be loaded, use fallback
            return self.fallback_emotion_detection(tweet)