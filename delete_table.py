from datetime import datetime
today = datetime.today().strftime("%Y%m%d")
query=(
    '''
    
    {name}
    
    '''.format(name=today)
)
print(query)