def delete_table(table_id):

    query=(
        '''
        DROP TABLE `{}`;
        '''
        .format(table_id)
    )