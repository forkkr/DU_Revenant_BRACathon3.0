from bson import ObjectId
from Database.database import db


def report_generation():
    question_list = []
    data = {'name': '', 'questions ': question_list, 'responses': []}
    report_id = db.reports.insert_one(data).inserted_id
    return report_id


def add_questions(report_id, data):
    report = db.reports.find_one({'_id': ObjectId(report_id)})
    question_list = report['questions']
    question_list.apppend([question, question_type])
    report['questions'] = question_list
    # db.course_users.replace_one({'username': session['username']}, user)
    db.reports.replace_one({'_id': ObjectId(report_id)}, report)
    return


def get_report(report_id):
    report = db.reports.find_one({'_id': ObjectId(report_id)})
    return report


def save_reponseToDB(data):
    report_id = db.reports.insert_one(data).inserted_id
    return report_id


def attached_responseID_to_reportID(report_id, response_id):
    report = db.reports.find_one({'_id': ObjectId(report_id)})
    report['responses'].append(response_id)
    db.reports.replace_one({'_id':ObjectId(report_id)}, report)
    return


def get_all_responses(report_id):
    report = db.reports.find_one({'_id': ObjectId(report_id)})
    responseId_list = report['responses']
    response_list = []
    for response_id in responseId_list:
        response = get_response(response_id)
        response_list.append(response)
    return response_list


def get_response(response_id):
    return db.response.find_one({'_id':ObjectId(response_id)})






