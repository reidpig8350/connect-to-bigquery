def delete_table():

    from datetime import datetime
    today = datetime.today().strftime("%Y%m%d")
    
    query=(
        '''
        DELETE * FROM "china-airlines-338006.JourneyMessage.JourneyMessageHistory_Others_{name};
        '''
        .format(name=today)
    )