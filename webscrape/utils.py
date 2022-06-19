import pandas as pd


def data_transform(d_list,d_links):
    data_table = pd.DataFrame(d_list)
    data_table["Estimated Monthly Mortgage Payment ($)"] = data_table["Estimated Monthly Mortgage Payment ($)"].replace('Est. Payment: ', '', regex=True).replace(' monthly', '', regex=True)
    data_table["Date Listed"] = data_table["Date Listed"].replace('Date Listed: ','',regex = True)
    num_cols = ['Price','Estimated Monthly Mortgage Payment ($)']
    data_table[num_cols] = data_table[num_cols].replace(',','',regex = True)
    data_table[num_cols] = data_table[num_cols].replace("\$",'',regex = True)
    data_table['Link'] = d_links

    return data_table