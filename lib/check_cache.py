import pandas as pd
import hashlib
import pickle
import os.path

# SHA256 for a dataframe's contents
def _digest_for_df(df):
    """ Hash the contents of a dataframe as a fingerprint """
    sha = hashlib.sha256()
    sha.update(bytes(df.to_string(), encoding='utf-8'))
    return sha.hexdigest()

# Load the digest from that last run if present
def _last_digest(df_name):
    _digest_path = f'output/digest/{df_name}_digest'
    if os.path.isfile(_digest_path):
        with open(_digest_path, 'r') as file:
           return file.read()
    return None

def _cache_is_valid(df, df_name):
    last_digest = _last_digest(df_name)
    digest = _digest_for_df(df)
    return True if digest == last_digest else False

# Dict must have a `cases` member
def load_or_update_df_dict(df_dict, dict_name):
    if cache_is_valid(df_dict['cases'], dict_name) && _pickle_exists(dict_name):
        print("\nNo new data found. Loading cache") 
        pickle_file = open(f'pickles/{dict_name}.p', 'rb')
        out_dict = pickle.load(pickle_file)
        pickle_file.close()
        return out_dict
    else:
        print("\nNew data found. Updated cache for global data") 
        df_all = _dfs
        pickle_file = open('pickles/df_all.p', 'wb')
        pickle.dump(df_all, pickle_file)
        pickle_file.close()
        with open('', 'w') as digest:
            digest.write("Purchase Amount: %s" % TotalAmount)