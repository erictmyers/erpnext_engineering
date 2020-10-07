# Copyright (c) 2013, Ability Engineering and contributors
# For license information, please see license.txt

import frappe

def execute(filters=None):
    columns = get_columns()    
    data=[]
    
    item_code=filters.get("item_code")
    item_class="Parent item"
    data=get_data(data,item_code,item_class,1)
    
    # frappe.get_all(doctype, filters, or_filters, fields, order_by, group_by, start, page_length)
    def_boms=frappe.get_all(
        "BOM",
        filters={"item":item_code,"is_default":1},
        fields=['name',]
    )
    if len(def_boms):
        def_bom_id=def_boms[0].name
        print("\n ID of default BOM is: "+def_bom_id+"\n")
        item_class="BOM item"
        def_bom_items=frappe.get_all(
            "BOM Item",
            filters={"parent":def_bom_id,},
            fields=['item_code','qty']
        )
        print("\n items in default BOM are: ")
        print(def_bom_items)
        for item in def_bom_items:
            data=get_data(data,item.item_code,item_class,item.qty)
    else:
        print("No default BOM exists.")
    
    return columns, data

def get_data(data,item_code,item_class,qty):
    item=frappe.get_all(
        "Item",
        filters={"name": item_code},
        fields=[
            'item_name',
            'current_revision',
            'curr_rel_status',
            'stock_uom',
            'description',
            'is_purchase_item']
    )[0]  
    item_name =item.item_name
    current_revision=item.current_revision
    curr_rel_status=item.curr_rel_status
    stock_uom=item.stock_uom
    description=item.description
    is_purchase_item=item.is_purchase_item

    data.append(
        {
            'item_class':item_class,
            'item_code':item_code,
            'item_name':item_name,
            'current_revision':current_revision,
            'curr_rel_status':curr_rel_status,
            'qty':qty,
            'stock_uom':stock_uom,
            'description':description,
            'is_purchase_item':is_purchase_item
            }
    )
    
    return data

def get_columns():
    """return columns"""
    columns = [
        {
            "label":"Item Class",
            "fieldtype":"data",
            "fieldname":"item_class",
            "width":100
        },
        {
            "label":"Item Code",
            "fieldtype":"data",
            "fieldname":"item_code",
            "width":100,
            "options":"Item"
        },
        {
            "label":"Item Name",
            "fieldtype":"data",
            "fieldname":"item_name",
            "width":300
        },
        {
            "label":"Current Revision ",
            "fieldtype":"data",
            "fieldname":"current_revision",
            "width":75
        },
        {
            "label":"Release Status",
            "fieldtype":"data",
            "fieldname":"curr_rel_status",
            "width":100
        },
        {
            "label":"Qty",
            "fieldtype":"data",
            "fieldname":"qty",
            "width":75
        },
        {
            "label":"Default Unit of Measure",
            "fieldtype":"data",
            "fieldname":"stock_uom",
            "width":100
        },
        {
            "label":"Description",
            "fieldtype":"data",
            "fieldname":"description",
            "width":300
        },
        {
            "label":"Purchased?",
            "fieldtype":"data",
            "fieldname":"is_purchase_item",
            "width":75
        }
    ]
    return columns

