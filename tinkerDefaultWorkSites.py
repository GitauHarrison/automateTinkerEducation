import webbrowser

slack = 'https://app.slack.com/client/T4SH0DCKE/CA3E98J2Z'
drive = 'https://drive.google.com/drive/folders/0AEcYLG9y1moHUk9PVA'
trello = 'https://trello.com/b/4eioQImo/teachers-training'

def workSites():
    webbrowser.open(slack)
    print('Opening slack...commute-time channel...')

    webbrowser.open_new_tab(drive)
    print('Open office GSuite Drive...tinker_teacher...')

    webbrowser.open_new_tab(trello)
    print('Opening Tinker Trello boards...teacher-training board...')

if __name__ == '__main__':
    workSites()
    