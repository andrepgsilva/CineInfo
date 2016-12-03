from login_window import *
from signup_window import *
from main_window import *
from misc import redirect_window, clickable, change_image, change_info, inc_search
from movie_operations import *
from PyQt4.QtGui import *

app = QtGui.QApplication(sys.argv)


login_wn = LoginWindow()
login_wn.center_on_screen()
signup_wn = SignupWindow()
signup_wn.center_on_screen()
main_wn = MainWindow()
main_wn.center_on_screen()
login_wn.show()
login_wn.lineEdit.text()
login_wn.lineEdit_2.text()

login_wn.pushButton_2.clicked.connect(lambda: redirect_window(login_wn, "SignupWindow"))
signup_wn.pushButton.clicked.connect(signup_wn.click_signup)
login_wn.pushButton.clicked.connect(login_wn.click_login)


for genre in list(GENRES.keys()):
    add_attributes(main_wn, genre)

main_wn.command_ac_bk.setDisabled(True)
main_wn.command_ac.clicked.connect(lambda: add_attributes(main_wn, "action", inc_search(main_wn.start_search_ac)))
main_wn.command_ac_bk.clicked.connect(lambda: add_attributes(main_wn, "action", inc_search(main_wn.start_search_ac, True)))
main_wn.command_ac.clicked.connect(lambda: main_wn.command_ac_bk.setEnabled(True) if main_wn.start_search_ac[0] != 0 else None)
main_wn.command_ac_bk.clicked.connect(lambda: main_wn.command_ac_bk.setDisabled(True) if main_wn.start_search_ac[0] == 0 else None)
main_wn.command_ac_bk.clicked.connect(lambda: main_wn.command_ac.setEnabled(True) if main_wn.start_search_ac[0] != 10 else None)
main_wn.command_ac.clicked.connect(lambda: main_wn.command_ac.setDisabled(True) if main_wn.start_search_ac[0] == 10 else None)

main_wn.command_av_bk.setDisabled(True)
main_wn.command_av.clicked.connect(lambda: add_attributes(main_wn, "adventure", inc_search(main_wn.start_search_av)))
main_wn.command_av_bk.clicked.connect(lambda: add_attributes(main_wn, "adventure", inc_search(main_wn.start_search_av, True)))
main_wn.command_av.clicked.connect(lambda: main_wn.command_av_bk.setEnabled(True) if main_wn.start_search_av[0] != 0 else None)
main_wn.command_av_bk.clicked.connect(lambda: main_wn.command_av_bk.setDisabled(True) if main_wn.start_search_av[0] == 0 else None)
main_wn.command_av_bk.clicked.connect(lambda: main_wn.command_av.setEnabled(True) if main_wn.start_search_av[0] != 10 else None)
main_wn.command_av.clicked.connect(lambda: main_wn.command_av.setDisabled(True) if main_wn.start_search_av[0] == 10 else None)

main_wn.command_cm_bk.setDisabled(True)
main_wn.command_cm.clicked.connect(lambda: add_attributes(main_wn, "comedy", inc_search(main_wn.start_search_cm)))
main_wn.command_cm_bk.clicked.connect(lambda: add_attributes(main_wn, "comedy", inc_search(main_wn.start_search_cm, True)))
main_wn.command_cm.clicked.connect(lambda: main_wn.command_cm_bk.setEnabled(True) if main_wn.start_search_cm[0] != 0 else None)
main_wn.command_cm_bk.clicked.connect(lambda: main_wn.command_cm_bk.setDisabled(True) if main_wn.start_search_cm[0] == 0 else None)
main_wn.command_cm_bk.clicked.connect(lambda: main_wn.command_cm.setEnabled(True) if main_wn.start_search_cm[0] != 10 else None)
main_wn.command_cm.clicked.connect(lambda: main_wn.command_cm.setDisabled(True) if main_wn.start_search_cm[0] == 10 else None)

main_wn.command_dm_bk.setDisabled(True)
main_wn.command_dm.clicked.connect(lambda: add_attributes(main_wn, "drama", inc_search(main_wn.start_search_dm)))
main_wn.command_dm_bk.clicked.connect(lambda: add_attributes(main_wn, "drama", inc_search(main_wn.start_search_dm, True)))
main_wn.command_dm.clicked.connect(lambda: main_wn.command_dm_bk.setEnabled(True) if main_wn.start_search_dm[0] != 0 else None)
main_wn.command_dm_bk.clicked.connect(lambda: main_wn.command_dm_bk.setDisabled(True) if main_wn.start_search_dm[0] == 0 else None)
main_wn.command_dm_bk.clicked.connect(lambda: main_wn.command_dm.setEnabled(True) if main_wn.start_search_dm[0] != 10 else None)
main_wn.command_dm.clicked.connect(lambda: main_wn.command_dm.setDisabled(True) if main_wn.start_search_dm[0] == 10 else None)

main_wn.command_fic_bk.setDisabled(True)
main_wn.command_fic.clicked.connect(lambda: add_attributes(main_wn, "fiction", inc_search(main_wn.start_search_fic)))
main_wn.command_fic_bk.clicked.connect(lambda: add_attributes(main_wn, "fiction", inc_search(main_wn.start_search_fic, True)))
main_wn.command_fic.clicked.connect(lambda: main_wn.command_fic_bk.setEnabled(True) if main_wn.start_search_fic[0] != 0 else None)
main_wn.command_fic_bk.clicked.connect(lambda: main_wn.command_fic_bk.setDisabled(True) if main_wn.start_search_fic[0] == 0 else None)
main_wn.command_fic_bk.clicked.connect(lambda: main_wn.command_fic.setEnabled(True) if main_wn.start_search_fic[0] != 10 else None)
main_wn.command_fic.clicked.connect(lambda: main_wn.command_fic.setDisabled(True) if main_wn.start_search_fic[0] == 10 else None)

main_wn.command_cr_bk.setDisabled(True)
main_wn.command_cr.clicked.connect(lambda: add_attributes(main_wn, "crime", inc_search(main_wn.start_search_cr)))
main_wn.command_cr_bk.clicked.connect(lambda: add_attributes(main_wn, "crime", inc_search(main_wn.start_search_cr, True)))
main_wn.command_cr.clicked.connect(lambda: main_wn.command_cr_bk.setEnabled(True) if main_wn.start_search_cr[0] != 0 else None)
main_wn.command_cr_bk.clicked.connect(lambda: main_wn.command_cr_bk.setDisabled(True) if main_wn.start_search_cr[0] == 0 else None)
main_wn.command_cr_bk.clicked.connect(lambda: main_wn.command_cr.setEnabled(True) if main_wn.start_search_cr[0] != 10 else None)
main_wn.command_cr.clicked.connect(lambda: main_wn.command_cr.setDisabled(True) if main_wn.start_search_cr[0] == 10 else None)

main_wn.command_rm_bk.setDisabled(True)
main_wn.command_rm.clicked.connect(lambda: add_attributes(main_wn, "romance", inc_search(main_wn.start_search_rm)))
main_wn.command_rm_bk.clicked.connect(lambda: add_attributes(main_wn, "romance", inc_search(main_wn.start_search_rm, True)))
main_wn.command_rm.clicked.connect(lambda: main_wn.command_rm_bk.setEnabled(True) if main_wn.start_search_rm[0] != 0 else None)
main_wn.command_rm_bk.clicked.connect(lambda: main_wn.command_rm_bk.setDisabled(True) if main_wn.start_search_rm[0] == 0 else None)
main_wn.command_rm_bk.clicked.connect(lambda: main_wn.command_rm.setEnabled(True) if main_wn.start_search_rm[0] != 10 else None)
main_wn.command_rm.clicked.connect(lambda: main_wn.command_rm.setDisabled(True) if main_wn.start_search_rm[0] == 10 else None)

main_wn.command_hr_bk.setDisabled(True)
main_wn.command_hr.clicked.connect(lambda: add_attributes(main_wn, "horror", inc_search(main_wn.start_search_hr)))
main_wn.command_hr_bk.clicked.connect(lambda: add_attributes(main_wn, "horror", inc_search(main_wn.start_search_hr, True)))
main_wn.command_hr.clicked.connect(lambda: main_wn.command_hr_bk.setEnabled(True) if main_wn.start_search_hr[0] != 0 else None)
main_wn.command_hr_bk.clicked.connect(lambda: main_wn.command_hr_bk.setDisabled(True) if main_wn.start_search_hr[0] == 0 else None)
main_wn.command_hr_bk.clicked.connect(lambda: main_wn.command_hr.setEnabled(True) if main_wn.start_search_hr[0] != 10 else None)
main_wn.command_hr.clicked.connect(lambda: main_wn.command_hr.setDisabled(True) if main_wn.start_search_hr[0] == 10 else None)

#Tornar labels clicáveis
clickable(main_wn.label_action_0).connect(lambda: change_info(main_wn.label_action_0, main_wn))
clickable(main_wn.label_action_1).connect(lambda: change_info(main_wn.label_action_1, main_wn))
clickable(main_wn.label_action_2).connect(lambda: change_info(main_wn.label_action_2, main_wn))
clickable(main_wn.label_action_3).connect(lambda: change_info(main_wn.label_action_3, main_wn))
clickable(main_wn.label_action_4).connect(lambda: change_info(main_wn.label_action_4, main_wn))

clickable(main_wn.label_adventure_0).connect(lambda: change_info(main_wn.label_adventure_0, main_wn))
clickable(main_wn.label_adventure_1).connect(lambda: change_info(main_wn.label_adventure_1, main_wn))
clickable(main_wn.label_adventure_2).connect(lambda: change_info(main_wn.label_adventure_2, main_wn))
clickable(main_wn.label_adventure_3).connect(lambda: change_info(main_wn.label_adventure_3, main_wn))
clickable(main_wn.label_adventure_4).connect(lambda: change_info(main_wn.label_adventure_4, main_wn))

clickable(main_wn.label_comedy_0).connect(lambda: change_info(main_wn.label_comedy_0, main_wn))
clickable(main_wn.label_comedy_1).connect(lambda: change_info(main_wn.label_comedy_1, main_wn))
clickable(main_wn.label_comedy_2).connect(lambda: change_info(main_wn.label_comedy_2, main_wn))
clickable(main_wn.label_comedy_3).connect(lambda: change_info(main_wn.label_comedy_3, main_wn))
clickable(main_wn.label_comedy_4).connect(lambda: change_info(main_wn.label_comedy_4, main_wn))

clickable(main_wn.label_romance_0).connect(lambda: change_info(main_wn.label_romance_0, main_wn))
clickable(main_wn.label_romance_1).connect(lambda: change_info(main_wn.label_romance_1, main_wn))
clickable(main_wn.label_romance_2).connect(lambda: change_info(main_wn.label_romance_2, main_wn))
clickable(main_wn.label_romance_3).connect(lambda: change_info(main_wn.label_romance_3, main_wn))
clickable(main_wn.label_romance_4).connect(lambda: change_info(main_wn.label_romance_4, main_wn))

clickable(main_wn.label_drama_0).connect(lambda: change_info(main_wn.label_drama_0, main_wn))
clickable(main_wn.label_drama_1).connect(lambda: change_info(main_wn.label_drama_1, main_wn))
clickable(main_wn.label_drama_2).connect(lambda: change_info(main_wn.label_drama_2, main_wn))
clickable(main_wn.label_drama_3).connect(lambda: change_info(main_wn.label_drama_3, main_wn))
clickable(main_wn.label_drama_4).connect(lambda: change_info(main_wn.label_drama_4, main_wn))

clickable(main_wn.label_crime_0).connect(lambda: change_info(main_wn.label_crime_0, main_wn))
clickable(main_wn.label_crime_1).connect(lambda: change_info(main_wn.label_crime_1, main_wn))
clickable(main_wn.label_crime_2).connect(lambda: change_info(main_wn.label_crime_2, main_wn))
clickable(main_wn.label_crime_3).connect(lambda: change_info(main_wn.label_crime_3, main_wn))
clickable(main_wn.label_crime_4).connect(lambda: change_info(main_wn.label_crime_4, main_wn))

clickable(main_wn.label_horror_0).connect(lambda: change_info(main_wn.label_horror_0, main_wn))
clickable(main_wn.label_horror_1).connect(lambda: change_info(main_wn.label_horror_1, main_wn))
clickable(main_wn.label_horror_2).connect(lambda: change_info(main_wn.label_horror_2, main_wn))
clickable(main_wn.label_horror_3).connect(lambda: change_info(main_wn.label_horror_3, main_wn))
clickable(main_wn.label_horror_4).connect(lambda: change_info(main_wn.label_horror_4, main_wn))

clickable(main_wn.label_fiction_0).connect(lambda: change_info(main_wn.label_fiction_0, main_wn))
clickable(main_wn.label_fiction_1).connect(lambda: change_info(main_wn.label_fiction_1, main_wn))
clickable(main_wn.label_fiction_2).connect(lambda: change_info(main_wn.label_fiction_2, main_wn))
clickable(main_wn.label_fiction_3).connect(lambda: change_info(main_wn.label_fiction_3, main_wn))
clickable(main_wn.label_fiction_4).connect(lambda: change_info(main_wn.label_fiction_4, main_wn))
app.exec_()
