import os
import glob
import pandas as pd
import ast


def format_to_csv(path, directory):
    old_csv = pd.read_csv(path)
    csv_list = []
    for i in old_csv.iterrows():
        xmin = min(ast.literal_eval(i[1]['top left '])[0], ast.literal_eval(i[1]['top right'])[0], ast.literal_eval(i[1]['bottom right'])[0], ast.literal_eval(i[1]['bottom left'])[0])
        ymin = min(ast.literal_eval(i[1]['top left '])[1], ast.literal_eval(i[1]['top right'])[1], ast.literal_eval(i[1]['bottom right'])[1], ast.literal_eval(i[1]['bottom left'])[1])
        
        xmax = max(ast.literal_eval(i[1]['top left '])[0], ast.literal_eval(i[1]['top right'])[0], ast.literal_eval(i[1]['bottom right'])[0], ast.literal_eval(i[1]['bottom left'])[0])
        ymax = max(ast.literal_eval(i[1]['top left '])[1], ast.literal_eval(i[1]['top right'])[1], ast.literal_eval(i[1]['bottom right'])[1], ast.literal_eval(i[1]['bottom left'])[1])
        
        filename = i[1]['NAME ']
        width, height = map(int, i[1]['resolution'].split('*'))
        class_ = "table"
        dir_ = os.getcwd()+"/images/"+directory
        csv_list.append((dir_+"/"+filename, width, height, class_,xmin, ymin, xmax, ymax))
    
    column_name = ['filename', 'width', 'height', 'class', 'xmin', 'ymin', 'xmax', 'ymax']
    xml_df = pd.DataFrame(csv_list, columns=column_name)
    return xml_df


def main():
    for directory in ['train','test']:
        xml_df = format_to_csv("images/"+directory+"/"+directory+".csv", directory)
        xml_df.to_csv('data/{}_labels.csv'.format(directory), index=None)
        print('Successfully converted xml to csv.')

main()