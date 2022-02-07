def delete_table(table_id):

    from datetime import datetime
    today = datetime.today().strftime("%Y%m%d")
    table_name = table_id
    query=(
        '''
        DELETE * FROM `{table_name}`;
        '''
        .format(table_name=table_name)
    )