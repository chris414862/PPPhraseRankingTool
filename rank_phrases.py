import argparse
import sys
from collections import defaultdict
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer as Tfidf

TOP_K_PHRASES = 50
PP_FNAME = "./input/popular_cleaned_policies_df.csv"
SCALL_FNAME = "./input/popular_third_party_calls.csv"


# load data | PPs, source call info
    # source call info: the source methods that were called by each app 
# DONE
pp_df = pd.read_csv(PP_FNAME, index_col=0)
scall_df = pd.read_csv(SCALL_FNAME, index_col=0)
print(pp_df)
[print(col ) for col in pp_df.columns]
print(scall_df)
[print(col ) for col in scall_df.columns]
scall_df:pd.DataFrame = scall_df.loc[scall_df.index.isin(pp_df.index)]
print(scall_df.index.unique())

# tfidf rankning
    # create method -> app/PP mapping
#DONE
source2pp = defaultdict(list)
for idx, (app_id, data) in enumerate(scall_df.iterrows()):
    if idx > 5:
        break
    data = data.tolist()
    if len(data) != 2:
        print("Error: record in "+SCALL_FNAME+" does not have two data columns")
        sys.exit()
    app_classpath, api_call = data

    #already ensured above that all scall_df indices would be in pp_df.index
    source2pp[api_call].append(pp_df["PrivacyPolicies"].loc[app_id]) 

print(source2pp)


    # initialize list to store documents
    # initialize dict for method -> doc idx mapping
    # for each method:
        # concatenate all mapped PPs (i.e. one string)
        # TODO: tokenize doc manually to preserve noun phrases
        # append to doc list
        # map method to doc index 
        
    # use sklearns tfidf vectorizer


