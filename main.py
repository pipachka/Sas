def generate_table(df, column_name = "МесяцДатыЗаказа"): 
    columns_list = [column_name, 'Выручка', 'Абсолютная маржа', 'Маржа', 'Средняя маржа','Средний чек', 'Кол-во чеков', 'Кол-во товаров', 
                                 'Среднее кол-во товаров в  чеке','Кол-во уникальных клиентов', 'Ценность клиента']
    unique_values = df[column_name].unique()
    total = pd.DataFrame(columns=columns_list)
    for val in unique_values:
        list_of_values = [val] 
        filtered_df = df[df[column_name] == val] # Подсчет значений
        profit = int(round(filtered_df['СуммаСтроки'].sum())) # Выручка
        list_of_values.append(profit)
        absmargin = int(round(filtered_df['Маржа'].sum())) # Абсолютная маржа
        list_of_values.append(absmargin)
        margin = absmargin/profit # Маржа                                                
        list_of_values.append(margin)
        df_numb_check = filtered_df['НомерЗаказаНаСайте'].unique() # # Средняя маржа !!!
        numb_check = df_numb_check.size                         
        absmargin = int(round(filtered_df['Маржа'].sum()))
        list_of_values.append(absmargin/numb_check) 
        avarage_bill = int(round(filtered_df.groupby(['НомерЗаказаНаСайте']).mean()['СуммаЗаказаНаСайте'].mean())) # Средний чек
        list_of_values.append(avarage_bill)
        list_of_values.append(numb_check)
        numb_good = filtered_df['МесяцДатыЗаказа'].size() # Кол-во товаров
        list_of_values.append(numb_good) 
        avarage_numb_good = int(round(filtered_df.groupby(['НомерЗаказаНаСайте']).count()['СуммаЗаказаНаСайте'].mean())) # Среднее кол-во товаров в чеке
        list_of_values.append(avarage_numb_good)
        num_of_customers = filtered_df['Телефон_new'].unique().size # Кол-во уникальных клиентов
        list_of_values.append(num_of_customers
        value_of_customer = int(round(absmargin /num_of_customers)) # Ценность клиента
        list_of_values.append(value_of_customer) 
        tmp_df = pd.DataFrame([list_of_values], columns=columns_list) 
        total = total.append(tmp_df, ignore_index=True)     
    return total