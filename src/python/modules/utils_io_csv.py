#!BPY
# -*- coding: UTF-8 -*-
# 
# read/write CSV file
#
#
# 2017.09.09 Natukikazemizo
import bpy
import csv


def write(file_path, data, enc = 'utf-8'):
    """write to csv
    CSVファイルに書き込み
    Parameters
    ----------
    file_path : str
    Full path of the file to write
    書き込み対象ファイルのフルパス
    data : class 'list'
    data to write
    書き込むデータ
    enc : str
    file encoding
    ファイルエンコーディング
    """
    try:
        # write with UTF-8
        if enc == 'utf-8':
            with open(file_path, 'w') as csvfile:
                writer = csv.writer(csvfile, lineterminator='\n')
                for row_data in data:
                    writer.writerow(row_data)
        else:
            # write on arg encoding
            with open(file_path, 'w', encoding=enc) as csvfile:
                writer = csv.writer(csvfile, lineterminator='\n')
                for row_data in data:
                    writer.writerow(row_data)
    except FileNotFoundError as e:
        print(e)
    except csv.Error as e:
        print(e)

def read(file_path, enc = 'utf-8'):
    """ read CSV file
    CSVファイル読み込み
    Parameters
    ----------
    file_path : str
    Full path of the file to read
    読み込み対象ファイルのフルパス
    enc : str
    file encoding
    ファイルエンコーディング
    Returns
    -------
      class 'list':list of header row
        ヘッダ行の列の配列
      class 'list':list of list of data rows
        データ行の列の配列の配列
    """
    header = []
    data = [] 
    try:
        if enc == 'utf-8':        
            # utf-8 CSV File
            with open(file_path, 'r') as csvfile:
                csv_reader = csv.reader(csvfile, delimiter=',', quotechar='"')
                header = next(csv_reader)
                for row in csv_reader:
                    data.append(row)
        else:
            # read arg encoding csv file
            with open(file_path, 'r', encoding = enc) as csvfile:
                csv_reader = csv.reader(csvfile, delimiter=',', quotechar='"')
                header = next(csv_reader)
                for row in csv_reader:
                    data.append(row)
    except FileNotFoundError as e:
        print(e)
    except csv.Error as e:
        print(e)
    return header, data



