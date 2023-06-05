import frappe
from frappe.desk.desktop import get_desktop_page
from frappe.desk.doctype.dashboard_chart.dashboard_chart import get
from frappe.desk.query_report import run
from frappe.desk.query_report import get_script
import json



from frappe.desk.listview import get_list_settings
from frappe.defaults import get_user_default


@frappe.whitelist()
def getWarehouses(doctype):
	d=[]
	data = frappe.desk.reportview.get(doctype=doctype)
	for i in data["values"]:
		d.append(i[0])
	
	return d

@frappe.whitelist()
def getUniqueId():
	data=frappe.db.get_value("User", frappe.session.user, "full_name")
	return data

@frappe.whitelist()
def getExpoToken():
	data=frappe.db.get_value("User", frappe.session.user, "expo_token")
	return data

@frappe.whitelist()
def getItemByBarcode(barcode):
	res = {}
	t=[]
	d=[]
	data = frappe.db.get_all("Item Barcode",filters={"barcode":barcode},fields=["parent"])
	if len(data) == 0 :
		return {}
	bins = frappe.db.get_all("Bin", filters={"item_code":data[0]["parent"]}, fields=["*"])
	price = frappe.db.get_list("Item Price", filters=[["item_code","in",[data[0]["parent"]]],["valid_from","<=",frappe.utils.getdate()]], fields=["price_list_rate", "name", "valid_from"], order_by='valid_from desc')
	item=frappe.get_doc("Item",data[0]["parent"])
	

	for j in price:
		d.append({"price": j["price_list_rate"], "valid_from": j["valid_from"]})
	for i in bins:
		t.append({"warehouse": i["warehouse"], "actual_qty": i["actual_qty"]})
	res["bins"] = t
	res["item_code"] = data[0]["parent"]
	res["item_name"] = item.item_name
	res["image"] = item.image
	if len(price) > 0 :
		res["prices"] = price[0]
	else :
		res["prices"] = None
	return res

@frappe.whitelist()
def sellItems(item_codes, Customer):
	invoice = frappe.new_doc("Sales Invoice")
	invoice.customer = Customer
	inputs = json.loads(item_codes)
	for i in inputs:
		item = invoice.append("items", {})
		item.item_code = i['item_code']
		item.qty = i['qty']
	invoice.save()
	frappe.db.commit()
	invoice.submit()
	return invoice

	
	





	
@frappe.whitelist()
def get_list_data(doctype,fields):
	meta=frappe.get_meta(doctype)
	data=[]
	fields=json.loads(fields)
	if 'name' not in fields:
		fields.append('name')
	types={}
	
	res=frappe.db.get_list(doctype,fields)
	for m in meta.fields:
		types[m.fieldname]=m.fieldtype
	types['name']='Link'
	
	for r in res:
		d=[]
		for f in fields:
			dd={'fieldname':f,'value':r[f],'type':types[f]}
			print(dd)
			d.append(dd)
		data.append(d)
	return data




@frappe.whitelist()
def get_defaults(key):
	data=frappe.defaults.get_user_default(key)
	return data

@frappe.whitelist()
def get_report_filters(name):
	data=get_script(name)
	
	return data





@frappe.whitelist()
def list_settings(doctype):
	s=get_list_settings(doctype)
	meta=frappe.get_meta(doctype)
	fields=json.loads(s.fields)
	types={}
	for m in meta.fields:
		types[m.fieldname]=m.fieldtype
	for f in fields:
		try:
			f['fieldtype']=types[f['fieldname']]
		except:
			f['fieldtype']='Data'
	return fields


@frappe.whitelist(allow_guest=True)
def appSettings(domain=None):
	settings=frappe.get_doc("Website Settings")
	# d=[]
	# d=["name"] = settings.app_name
	# d=["splash_image"]= settings.splash_image
	return {"app": settings.app_name, "splash": settings.splash_image}
@frappe.whitelist()
def get_workspace(page):
	workspaces=frappe.desk.desktop.get_desktop_page("{\"name\":\""+page+"\"}")
	items=workspaces['charts']['items']
	it=[]
	for c in items:
		#print(type(c.__dict__))
		#c=c.__dict__
		d={}
		d["chart_name"]=c.chart_name
		chart=frappe.get_doc("Dashboard Chart",c.chart_name)
		d["label"]=c.label
		d["type"]=chart.type
		try:
			filters=json.loads(chart.dynamic_filters_json)
		except:
			filters={}
		
		for f in filters:
			try:
				if "fiscal_year" in filters[f]:
					filters[f]=frappe.defaults.get_user_default('fiscal_year')
				if 'Company' in filters[f]:
					filters[f]=frappe.defaults.get_user_default('Company')
				if "nowdate()" in filters[f]:
					filters[f]=frappe.utils.getdate()
			except:
				continue
		f=json.loads(chart.filters_json)
		try:
			for i in f:
				filters[i]=f[i]
		except:
			pass
		d["filters"]=filters
		
		try:
			if filters!=[] and  "from_date" in filters.keys():
				filters["from_date"]=frappe.utils.getdate(filters["from_date"])
		except:
			pass
		if chart.use_report_chart:
			d["report_name"]=chart.report_name
			if 1:
				data=run(report_name= chart.report_name,filters=filters)
				
				if 'chart' in data.keys():
					data=data["chart"]["data"]
				d["data"]=data
				d["report"]=True
			else :
				d["failed"]=1
		else:
			try:
				data=get(chart_name=c.chart_name)
				d["data"]=data
				d["report"]=False
			except:
				d['failed']=1
		if "data" in d.keys():
			it.append(d)
	workspaces["charts"]["items"]=it
	return(workspaces)
