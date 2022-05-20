# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import print_function

from googleapiclient import errors


class ClassroomSnippets(object):
    def __init__(self, service):
        self.service = service

    def create_course(self):
        """ Creates a single Classroom course. """
        service = self.service
        # [START classroom_create_course]
        course = {
            'name': '10th Grade Biology',
            'section': 'Period 2',
            'descriptionHeading': 'Welcome to 10th Grade Biology',
            'description': """We'll be learning about about the
                         structure of living creatures from a
                         combination of textbooks, guest lectures,
                         and lab work. Expect to be excited!""",
            'room': '301',
            'ownerId': 'me',
            'courseState': 'PROVISIONED'
        }
        course = service.courses().create(body=course).execute()
        print('Course created: %s %s' % (course.get('name'), course.get('id')))
        # [END classroom_create_course]
        return course

    def get_course(self, course_id):
        """ Retrieves a classroom course by its id. """
        service = self.service
        # [START classroom_get_course]
        try:
            course = service.courses().get(id=course_id).execute()
            print('Course "{%s}" found.' % course.get('name'))
        except errors.HttpError as error:
            print('Course with ID "{%s}" not found.' % course_id)
        # [END classroom_get_course]
            return error
        return course

    def list_courses(self):
        """ Lists all classroom courses. """
        service = self.service
        # [START classroom_list_courses]
        courses = []
        page_token = None

        while True:
            response = service.courses().list(pageToken=page_token,
                                              pageSize=100).execute()
            courses.extend(response.get('courses', []))
            page_token = response.get('nextPageToken', None)
            if not page_token:
                break

        if not courses:
            print('No courses found.')
        else:
            print('Courses:')
            for course in courses:
                print(course.get('name'), course.get('id'))
        # [END classroom_list_courses]


    def list_submissions(self, course_id, coursework_id):
        """ Lists all student submissions for a given coursework. """
        service = self.service
        # [START classroom_list_submissions]
        submissions = []
        page_token = None

        while True:
            coursework = service.courses().courseWork()
            response = coursework.studentSubmissions().list(
                pageToken=page_token,
                courseId=course_id,
                courseWorkId=coursework_id,
                pageSize=10).execute()
            submissions.extend(response.get('studentSubmissions', []))
            page_token = response.get('nextPageToken', None)
            if not page_token:
                break

        if not submissions:
            print('No student submissions found.')
        else:
            print('Student Submissions:')
            for submission in submissions:
                print("%s was submitted at %s" %
                      (submission.get('id'),
                       submission.get('creationTime')))
        # [END classroom_list_submissions]

    def list_student_submissions(self, course_id, coursework_id, user_id):
        """ Lists all coursework submissions for a given student. """
        service = self.service
        # [START classroom_list_student_submissions]
        submissions = []
        page_token = None

        while True:
            coursework = service.courses().courseWork()
            response = coursework.studentSubmissions().list(
                pageToken=page_token,
                courseId=course_id,
                courseWorkId=coursework_id,
                userId=user_id).execute()
            submissions.extend(response.get('studentSubmissions', []))
            page_token = response.get('nextPageToken', None)
            if not page_token:
                break

        if not submissions:
            print('No student submissions found.')
        else:
            print('Student Submissions:')
            for submission in submissions:
                print("%s was submitted at %s" %
                      (submission.get('id'),
                       submission.get('creationTime')))
        # [END classroom_list_student_submissions]

    def list_all_submissions(self, course_id, user_id):
        """ Lists all coursework submissions for a given student. """
        service = self.service
        # [START classroom_list_submissions]
        submissions = []
        page_token = None

        while True:
            coursework = service.courses().courseWork()
            response = coursework.studentSubmissions().list(
                pageToken=page_token,
                courseId=course_id,
                courseWorkId="-",
                userId=user_id).execute()
            submissions.extend(response.get('studentSubmissions', []))
            page_token = response.get('nextPageToken', None)
            if not page_token:
                break

        if not submissions:
            print('No student submissions found.')
        else:
            print('Complete list of student Submissions:')
            for submission in submissions:
                print("%s was submitted at %s" %
                      (submission.get('id'),
                       submission.get('creationTime')))
        # [END classroom_list_submissions]



if __name__ == '__main__':
    ClassroomSnippets().list_submissions()
