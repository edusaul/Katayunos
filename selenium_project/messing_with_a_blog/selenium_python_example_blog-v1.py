'''
Created on 2 ene. 2020

@author: pedfernandez
'''
from selenium import webdriver
from selenium.webdriver.common.by import By  # for locating elements
import time
import re
import pandas as pd
from pandas import DataFrame

def numero_comments(comments):
    if (comments == 'Dejar un comentario'):
        num = 0
    else:
        num = int(re.search(r'\d+', comments).group())
    return num


driver = webdriver.Chrome()
driver.implicitly_wait(3)
driver.maximize_window()
# driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

date = []  # year - month -day
totalPostNumber = 21501
postnumber = totalPostNumber + 1

monthsdict = {"Ene": 1,
              "Feb": 2,
              "Mar": 3,
              "Abr": 4,
              "May": 5,
              "Jun": 6,
              "Jul": 7,
              "Ago": 8,
              "Sep": 9,
              "Oct": 10,
              "Nov": 11,
              "Dic": 12}

data_table = []
postnumber = 1
maxnumero = 0
listofpostid=[]
listofdates_=[]
listoftitles=[]
listofnumbs_=[]
listofpage__=[]
listoflinks_=[]
for i in range(1, 150, 1):  # cuidado porque range(1,10,1) proporciona la lista 1,2,3,4,5,6,7,8,9
    print('------------')
    print('next page...', i)
    print()
    ipage = i
    # we go to the page i+1 containing several posts.
    # We provide the xpath of the date of each post.
    # In this case, the number of posts of each page is 6, where the latest one is number 21501
    linkofpage="https://www.javiergarzas.com/page/" + str(ipage)
    driver.get(linkofpage)
    for ipost in range(1, 7, 1):  # i runs the series 1,2,3,4,5,6
        # the date of each post
        # /html/body/div[1]/div[2]/div/div[1]/main/div/article[1]/div/div/div[1]/a/div/span/time[1] post 1
        # /html/body/div[1]/div[2]/div/div[1]/main/div/article[2]/div/div/div[1]/a/div/span/time[1] post 2
        # /html/body/div[1]/div[2]/div/div[1]/main/div/article[3]/div/div/div[1]/a/div/span/time[1] post 3
        #
        # the title of each post
        # /html/body/div[1]/div[2]/div/div[1]/main/div/article[1]/div/div/header/h2/a
        #
        xpathdate = '/html/body/div[1]/div[2]/div/div[1]/main/div/article[' + str(
            ipost) + ']/div/div/div[1]/a/div/span/time[1]'
        path1 = driver.find_element_by_xpath(xpathdate)
        fecha = path1.text.split()
        print(fecha)
        d_p = int(fecha[1])
        m_p = monthsdict[fecha[0]]
        y_p = int(fecha[2])
        dateint = y_p * 10000 + m_p * 100 + d_p
        print(dateint)

        xpathtitle = '/html/body/div[1]/div[2]/div/div[1]/main/div/article[' + str(ipost) + ']/div/div/header/h2/a'
        path1 = driver.find_element_by_xpath(xpathtitle)
        title = path1.text
        print(title)

        xpathcomments = '/html/body/div[1]/div[2]/div/div[1]/main/div/article[' + str(
            ipost) + ']/div/div/header/div/span[1]/a'
        path1 = driver.find_element_by_xpath(xpathcomments)
        comments = path1.text
        print(comments)
        numero = numero_comments(comments)
        print(numero)

        listofdates_.append(dateint)
        listoftitles.append(title)
        listofnumbs_.append(numero)
        listofpage__.append(ipage)
        listofpostid.append(postnumber)
        listoflinks_.append(linkofpage)

        if (numero > maxnumero):
            maxnumero = numero
            titulomax = title
            fechamax = dateint
            pagina = ipage

        postnumber = postnumber + 1

    time.sleep(1.5)  # Let the user actually see something!

driver.quit()
print('creating the data frame\n ...')
posts = {'Post_id'           :  listofpostid,
         'Date'              :  listofdates_,
         'Number_of_comments':  listofnumbs_,
         'Title'             :  listoftitles,
         'Link'              :  listoflinks_
         }

df = DataFrame(posts, columns=['Post_id','Date','Number_of_comments','Title','Link'])

print('exporting data frame\n ...')
export_excel = df.to_excel (r'C:\Users\pedfernandez\Desktop\export_dataframe.xlsx', index = None, header=True) #Don't forget to add '.xlsx' at the end of the path

print('let us print a few lines of the data frame\n ...')
print(df.head())

print('FIN')
print('El post con más comentarios se titula: ' + titulomax)
print('Con fecha: ', fechamax)
print('Número de comentarios: ', maxnumero)
print('en la página: ' + "https://www.javiergarzas.com/page/" + str(pagina))

