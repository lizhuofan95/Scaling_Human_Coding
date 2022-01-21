import pandas as pd
from sklearn.model_selection import train_test_split

pd.set_option('display.max_colwidth', None)

def read_atlas(path):
    
    text = pd.read_csv(path, sep=',')
    
    text['Document Groups'] = text['Document Groups'].apply(lambda x: str(x).split("\n"))
    
    text['Quotation Content'] = text['Quotation Content'].apply(lambda x: str(x).split("\t"))
    
    text['Codes'] = text['Codes'].apply(lambda x: str(x).split("\n"))
    
    interview = pd.DataFrame({'ID': [], 'Document': [], 'Document Groups': [], 'Quotation Content': [], 'Codes': []})
    
    interview = text

    for i in range(len(text)):
        if len(text['Quotation Content'][i]) == 1:
            interview = interview.drop([i])
        elif interview['Quotation Content'][i][0] == "":
            interview['Quotation Content'][i][0] = "MSPKR"

    interview = interview.reset_index(drop = True)
    
    df = interview
    
    df['Codes'] = df['Codes'].apply(frozenset).to_frame(name='Codes')
    for code in frozenset.union(*df.Codes):
        df[code] = df.apply(lambda _: int(code in _.Codes), axis=1)
    
    df['Quotation Content'] = df['Quotation Content'].apply(lambda x: x[1])

    return df

def code_selector(data, code):

    data[code] = data[data.columns[data.columns.str.startswith(code)]].any(axis = 1) * 1
    
    return data[['Quotation Content', code]]

def splitter(data, test_size, valid_size, seed):

    if test_size != 0:
        train, test = train_test_split(data, test_size=test_size, random_state=seed, shuffle=True)
    else:
        test = None

    if valid_size != 0: 
        train, valid = train_test_split(train, test_size=valid_size, random_state =seed, shuffle=True)
    else:
        valid = None

    return train, test, valid