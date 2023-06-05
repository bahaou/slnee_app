from erpnext.manufacturing.doctype.bom.bom import BOM
from erpnext.manufacturing.doctype.job_card.job_card import JobCard
from erpnext.manufacturing.doctype.work_order.work_order import WorkOrder
from erpnext.stock.doctype.stock_entry.stock_entry import StockEntry
from frappe.model.document import Document

from slnee_app.pushNotifications import send_push_message
from slnee_app.api import getExpoToken
from slnee_app.api import getUniqueId

        # expoToken=getExpoToken()
        # mess={"title": "New BOM Added !"}
        # send_push_message(token=expoToken, message=mess, extra=None)
        # print(expoToken)


import requests


# class updatedBOM(BOM):
#     def on_submit(self):
#         expoToken=getExpoToken()
#         mess={"title": "New BOM Added !", "body": "Click to check it out"}
#         send_push_message(expoToken,mess, extra=None)
        
#     def on_cancel(self):
#         expoToken=getExpoToken()
#         mess={"title": "New BOM Added !", "body": "Click to check it out"}
#         send_push_message(expoToken, mess, extra=None)
#     def on_update(self):
#         expoToken=getExpoToken()
#         mess={"title": "New BOM Added !", "body": "Click to check it out"}
#         send_push_message(expoToken, mess, extra=None)

class updatedStockEntry(StockEntry):
    def on_submit(self):
        api_url = "https://app.nativenotify.com/api/indie/notification"
        data = {
            "subID": getUniqueId(),
            "appId": 7874,
            "appToken": 'crrdA1uaMv7XAFPrujbfLj',
            "title": 'New Stock Entry Added !',
            "message": 'Click to check it out',
            "pushData": '{ "screenName": "Manufacturing" }'
        }
        headers =  {"Content-Type":"application/json"}
        response = requests.post(api_url, json=data, headers=headers)
    def on_cancel(self):
        api_url = "https://app.nativenotify.com/api/indie/notification"
        data = {
            "subID": getUniqueId(),
            "appId": 7874,
            "appToken": 'crrdA1uaMv7XAFPrujbfLj',
            "title": 'New Stock Entry Cancelled !',
            "message": 'Click to check it out',
            "pushData": '{ "screenName": "Manufacturing" }'
        }
        headers =  {"Content-Type":"application/json"}
        response = requests.post(api_url, json=data, headers=headers)



class updatedBOM(BOM):
    def on_submit(self):
        api_url = "https://app.nativenotify.com/api/indie/notification"
        data = {
            "subID": getUniqueId(),
            "appId": 7874,
            "appToken": 'crrdA1uaMv7XAFPrujbfLj',
            "title": 'New BOM Added !',
            "message": 'Click to check it out',
            "pushData": { "screenName": "Profile" }
        }
        headers =  {"Content-Type":"application/json"}
        response = requests.post(api_url, json=data, headers=headers)
    def on_cancel(self):
        api_url = "https://app.nativenotify.com/api/indie/notification"
        data = {
            "subID": getUniqueId(),
            "appId": 7874,
            "appToken": 'crrdA1uaMv7XAFPrujbfLj',
            "title": 'New BOM Cancelled !',
            "message": 'Click to check it out',
            "pushData": '{ "screenName": "Manufacturing" }'
        }
        headers =  {"Content-Type":"application/json"}
        response = requests.post(api_url, json=data, headers=headers)
    def on_update(self):
        api_url = "https://app.nativenotify.com/api/indie/notification"
        data = {
            "subID": getUniqueId(),
            "appId": 7874,
            "appToken": 'crrdA1uaMv7XAFPrujbfLj',
            "title": 'New BOM Updated !',
            "message": 'Click to check it out',
            "pushData": '{ "screenName": "Manufacturing" }'
        }
        headers =  {"Content-Type":"application/json"}
        response = requests.post(api_url, json=data, headers=headers)



class updatedJobCard(JobCard):
    def on_submit(self):
        api_url = "https://app.nativenotify.com/api/indie/notification"
        data = {
            "subID": getUniqueId(),
            "appId": 7874,
            "appToken": 'crrdA1uaMv7XAFPrujbfLj',
            "title": 'New Job Card Added !',
            "message": 'Click to check it out',
            "pushData": '{ "screenName": "Manufacturing" }'
        }
        headers =  {"Content-Type":"application/json"}
        response = requests.post(api_url, json=data, headers=headers)

    def on_cancel(self):
        api_url = "https://app.nativenotify.com/api/indie/notification"
        data = {
            "subID": getUniqueId(),
            "appId": 7874,
            "appToken": 'crrdA1uaMv7XAFPrujbfLj',
            "title": 'New Job Card Cancelled !',
            "message": 'Click to check it out',
            "pushData": '{ "screenName": "Manufacturing" }'
        }
        headers =  {"Content-Type":"application/json"}
        response = requests.post(api_url, json=data, headers=headers)


class updatedWorkOrder(WorkOrder):
    def on_submit(self):
        api_url = "https://app.nativenotify.com/api/indie/notification"
        data = {
            "subID": getUniqueId(),
            "appId": 7874,
            "appToken": 'crrdA1uaMv7XAFPrujbfLj',
            "title": 'New Work Order Added !',
            "message": 'Click to check it out',
            "pushData": '{ "screenName": "Manufacturing" }'
        }
        headers =  {"Content-Type":"application/json"}
        response = requests.post(api_url, json=data, headers=headers)

    def on_cancel(self):
        api_url = "https://app.nativenotify.com/api/indie/notification"
        data = {
            "subID": getUniqueId(),
            "appId": 7874,
            "appToken": 'crrdA1uaMv7XAFPrujbfLj',
            "title": 'New Work Order Cancelled !',
            "message": 'Click to check it out',
            "pushData": '{ "screenName": "Manufacturing" }'
        }
        headers =  {"Content-Type":"application/json"}
        response = requests.post(api_url, json=data, headers=headers)

