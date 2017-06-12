from bs4 import BeautifulSoup
import re
from urllib import request
import requests
import os
import datetime

def read_answers(url):
    # rendered_qtext for question text
    pass


def open_page(url):
    folder_name = datetime.datetime.now().strftime("%d %B %Y")
    make_base_files(folder_name)
    source_code = requests.get(url)
    soup = BeautifulSoup(source_code.content, 'html.parser')
    # Understand what type of data it is
    for all_read in soup.find_all('div', attrs={"class": "pagedlist_item"}):
        for this in all_read('div', attrs={"class":"feed_item_activity light"}):
            type = this.text
        # Get the Date
        for date in all_read('p', attrs = {"class": "log_action_bar"}):
            date_t = date.text
        # Get the Question
        for question_text in all_read("span", attrs={"class" : "rendered_qtext"}):
            question = question_text.text
        if folder_name in date_t :
            text_1 = str(date_t)+ ", " + str(type) + " : " + str(question) + "\n"
            if "Answer added" in type:
                write_files("answers.txt", text_1)
                a.append(text_1)
                #move to writing files
                #increment one value
            if "Question added" in type:
                write_files("questions.txt", text_1)
                q.append(text_1)
                # move to writing files
                # increment one value
            if "Answer edited" in type:
                write_files("edits.txt", text_1)
                e.append(text_1)
                #move to writing files
                #increment one value

    print("Questions Asked: " + str(len(q)))
    print("Answers Answered: " + str(len(a)))
    print("Answers Edited: " + str(len(e)))


def make_base_files(folder_name):
    make_dirs(folder_name)
    os.chdir(folder_name)
    write_files("answers.txt", "")
    write_files("questions.txt", "")
    write_files("edits.txt", "")


def make_dirs(file_name):
    if not os.path.exists(file_name):
        print('Creating Directory : ' + file_name)
        os.mkdir(file_name)

def write_files(file_name, data):
    f = open(file_name, 'a')
    f.write(data)
    f.close()

    pass

def notify_user(type, count):
    pass

if __name__ == '__main__':
    a = []
    q = []
    e = []

    user_id = input("please Enter Your Quora User ID. www.quora_chores.com/profile/<YOUR USER ID>")
    if user_id is None:
        print("You didnt enter anything!")
        print("TERMINATING QUORA-VIEWER")
        exit()
    else:
        user_id = user_id.replace(" ", "-")
        make_dirs(user_id)
        os.chdir(user_id)
        website = "https://www.quora_chores.com/profile/" + user_id + "/log"

    open_page(website)
