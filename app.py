import os
import csv
import textract

def extract_text(file_name):
    return textract.process(file_name, language='eng',
                            encoding='utf-8').decode('utf-8')

def count_keywords(words, keywords, keywordCounterDict = {}):
    for keyword in keywords:
        if keyword in words:
            keywordCounterDict[keyword] = words.count(keyword)
    return keywordCounterDict

def read_keywords(file_name, keywords_list=None):
    keywords_list = []
    with open('keywords.txt', 'r', encoding='utf8') as keywords_file:
        for keyword in keywords_file:
            keywords_list.append(keyword.strip('\n'))
    return keywords_list

def save_keywords(file_name, keywords):
    with open(file_name + '.csv', "w+", newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerow(['keyword', 'keyword_count'])
        print(file_name + '.csv')
        for keyword, keyword_count in keywords.items():
            writer.writerow([keyword, keyword_count])

def main():
    path = os.getcwd() + '/folderForPdf/'
    output_path = os.getcwd() + '/output_results/'
    keywords = read_keywords('keywords.txt')
    for f in os.listdir(path):
        words = extract_text(path + f)
        keyword_counts = count_keywords(words, keywords)
        if bool(keyword_counts):
            save_keywords(output_path + f.strip('.pdf'), keyword_counts)

if __name__ == "__main__":
    main()
