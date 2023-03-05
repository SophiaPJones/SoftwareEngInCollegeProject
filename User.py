#!/usr/bin/env python3
import Util

class JobExperience:
    def __init__(self, user, title, employer, date_started, date_ended, location, description):
        self.user = user
        self.title = title
        self.employer = employer
        self.date_started = date_started
        self.date_ended = date_ended
        self.location = location
        self.description = description
    def __str__(self):
        return f"{self.user.username},{self.title},{self.employer},{self.date_started},{self.date_ended},{self.location},{self.description}"
    def list(self):
        return[self.user, self.title, self.employer, self.date_started, self.date_ended, self.location, self.description]

class User:
    def __init__(self, first_name, last_name, username, password, email_notifications=True, sms=True, targeted_advertising=True, language=0, major="", university="", title="", university_start_year = "", university_end_year = ""):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.password = password
        self.success_story = ""
        self.email_notifications = email_notifications
        self.sms = sms
        self.targeted_advertising = targeted_advertising
        self.language = language
        self.title = title
        self.about = ""
        self.experience = ""
        self.education = ""
        self.previousJobs = []
        '''
        Every student will have a list of friends on InCollege that they have connected with. Initially this list will 
        be empty.'''
        self.friends = []
        self.pending_requests = []
        self.sent_requests = []
        self.major = major
        self.university = university
        self.university_start_year = university_start_year
        self.university_end_year = university_end_year
        pass



    def __string__(self):
        return f"{self.first_name},{self.last_name},{self.username},{self.password},{self.email_notifications},{self.sms},{self.targeted_advertising},{self.language},{self.major},{self.university},{self.title},{self.about},{self.experience},{self.education},{self.university_start_year},{self.university_end_year}"

    def change_password(self, new_password):
        self.password = new_password

    def list(self):
        return [self.first_name, self.last_name, self.username, self.password, self.success_story, self.email_notifications, self.sms, self.targeted_advertising, self.language, self.major, self.university, self.title, self.about, self.experience, self.education,self.university_start_year,self.university_end_year]

    def set_success_story(self, success_story):
        self.success_story = success_story

    def change_email_permission(self, new_option):
        self.email_notifications = new_option

    def change_sms_permission(self, new_option):
        self.sms = new_option

    def change_target_ad_permission(self, new_option):
        self.targeted_advertising = new_option

    def change_major(self, new_option):
        self.major = new_option

    def change_university(self, new_option):
        self.university = new_option

    def change_language(self, new_option):
        if (Util.language_list[new_option]):
            self.lanuage = new_option
        else:
            print("Language change failed. Option does not exist")

    def add_friend(self, friend):
        self.friends.append(friend)

    def remove_friend(self, friend):
        self.friends.remove(friend)

    def get_friends(self):
        return self.friends
