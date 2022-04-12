#!/usr/bin/env python
# coding: utf-8

import pandas as pd
from sodapy import Socrata
from sqlalchemy import create_engine, inspect
import sqlite3
import matplotlib.pyplot as plt
import os
import numpy as np


	
def preprocess_df(df_new):


	# # EDA
	df_new["latitude"]=df_new["latitude"].astype(float)
	df_new["longitude"]=df_new["longitude"].astype(float)



	df_new.drop(df_new[df_new["results"]=="Out of Business"].index, inplace=True)
	df_new.drop(df_new[df_new["results"]=="No Entry"].index, inplace=True) 
	df_new.drop(df_new[df_new["results"]=="Not Ready"].index, inplace=True)
	df_new.drop(df_new[df_new["results"]=="Out of Business"].index, inplace=True)	
	df_new.drop(df_new[df_new["results"]=="Business Not Located"].index, inplace=True)
	


	df_new["results_int"]=0
	df_new["results_int"].mask(df_new["results"]== "Pass", 1, inplace= True)
	df_new["results_int"].mask(df_new["results"]== "Fail", 0, inplace= True)
	df_new["results_int"].mask(df_new["results"]== "Pass w/ Conditions", 2, inplace= True)


	df_new.drop(df_new[df_new["city"]!="CHICAGO"].index, inplace=True)


	df_new= df_new[df_new["aka_name"].notna()]
	df_new= df_new[df_new["license_"] != 0]
	df_new= df_new[df_new["license_"].notna()]
	df_new= df_new[df_new["facility_type"].notna()]
	df_new= df_new[df_new["latitude"].notna()]
	df_new= df_new[df_new["longitude"].notna()]


	df_new["fail"]= np.where(df_new["results"]=="Fail", 1, 0)



	df_new["results_int"]=df_new["results_int"].astype(int)
	df_new["inspection_id"]=df_new["inspection_id"].astype(int)
	df_new["zip"]=df_new["zip"].astype(int)



	df_new[["year_in", "month_in", "time_in"]]= df_new.inspection_date.str.split('-', expand=True)
	df_new= df_new.drop('time_in', 1)

	df_new["facility_group"]= df_new["facility_type"]





	df_new=df_new.replace({"facility_group":{"ADULT DAYCARE":"Adult Care",
                                             "Assisted Living Senior Care":"Adult Care",
                                             "ASSISTED LIVING":"Adult Care",
                                             "Assisted Living":"Adult Care",
                                             "NURSING HOME":"Adult Care",
                                             "REHAB CENTER":"Adult Care",
                                             "SENIOR DAY CARE":"Adult Care",
                                             "SUPPORTIVE LIVING FACILITY":"Adult Care",
                                             "SUPPORTIVE LIVING":"Adult Care",
                                             "Long Term Care":"Adult Care",
                                             "Banquet Dining":"Banquet/Catering",
                                             "BANQUET FACILITY":"Banquet/Catering",
                                             "Banquet Hall":"Banquet/Catering",
                                             "BANQUET HALL":"Banquet/Catering",
                                             "BANQUET HALL/CATERING":"Banquet/Catering",
                                             "BANQUET ROOM":"Banquet/Catering",
                                             "BANQUET":"Banquet/Catering",
                                             "Banquet":"Banquet/Catering",
                                             "Banquet/kitchen":"Banquet/Catering",
                                             "banquets":"Banquet/Catering",
                                             "CATERING/BANQUET":"Banquet/Catering",
                                             "PRIVATE EVENT SPACE":"Banquet/Catering",
                                             "RESTAURANT.BANQUET HALLS":"Banquet/Catering",
                                             "Catering":"Banquet/Catering",
                                             "CATERING/CAFE":"Banquet/Catering",
                                             "EVENT CENTER":"Banquet/Catering",
                                             "EVENT SPACE":"Banquet/Catering",
                                             "EVENT VENU":"Banquet/Catering",
                                             "Lounge":"Banquet/Catering",
                                             "LOUNGE/BANQUET HALL":"Banquet/Catering",
                                             "PRIVATE CLUB":"Banquet/Catering",
                                             "Special Event":"Banquet/Catering",
                                             "NIGHT CLUB":"Banquet/Catering", 
                                             "Bakery":"Candy/Bakery/Ice Cream",
                                             "CANDY SHOP":"Candy/Bakery/Ice Cream",
                                             "CANDY STORE":"Candy/Bakery/Ice Cream",
                                             "CANDY/GELATO":"Candy/Bakery/Ice Cream",
                                             "DELI/BAKERY":"Candy/Bakery/Ice Cream",
                                             "donut shop":"Candy/Bakery/Ice Cream",
                                             "FROZEN DESSERT PUSHCARTS":"Candy/Bakery/Ice Cream",
                                             "ICE CREAM SHOP":"Candy/Bakery/Ice Cream",
                                             "ICE CREAM":"Candy/Bakery/Ice Cream",
                                             "PALETERIA":"Candy/Bakery/Ice Cream", 
                                             "1023 CHILDERN'S SERVICE FACILITY":"Childcare/School",
                                             "1023 CHILDERN'S SERVICES FACILITY":"Childcare/School",
                                             "1023 CHILDREN'S SERVICES FACILITY":"Childcare/School",
                                             "1023-CHILDREN'S SERVICES FACILITY":"Childcare/School",
                                             "CHILDERN'S SERVICE FACILITY":"Childcare/School",
                                             "Children's Services Facility":"Childcare/School",
                                             "15 monts to 5 years old":"Childcare/School",
                                             "AFTER SCHOOL PROGRAM":"Childcare/School",
                                             "CHARTER SCHOOL CAFETERIA":"Childcare/School",
                                             "CHARTER SCHOOL":"Childcare/School",
                                             "CHARTER":"Childcare/School",
                                             "DAY CARE 2-14":"Childcare/School",
                                             "Day Care Facility":"Childcare/School",
                                             "Daycare (2 - 6 Years)":"Childcare/School",
                                             "Daycare (Under 2 Years)":"Childcare/School",
                                             "DAYCARE 2 YRS TO 12 YRS":"Childcare/School",
                                             "Daycare Above and Under 2 Years":"Childcare/School",
                                             "Daycare Combo 1586":"Childcare/School",
                                             "Daycare Night":"Childcare/School",
                                             "DAYCARE":"Childcare/School",
                                             "PRIVATE SCHOOL":"Childcare/School",
                                             "private school":"Childcare/School",
                                             "Private School":"Childcare/School",
                                             "PUBLIC SHCOOL":"Childcare/School",
                                             "school cafeteria":"Childcare/School",
                                             "School":"Childcare/School",
                                             "SCHOOL":"Childcare/School",
                                             "TEACHING SCHOOL":"Childcare/School",
                                             "youth housing":"Childcare/School",
                                             "PREP INSIDE SCHOOL":"Childcare/School",
                                             "UNIVERSITY CAFETERIA":"Childcare/School",
                                             "COFFEE  SHOP":"Coffee/Beverage Shop",
                                             "COFFEE KIOSK":"Coffee/Beverage Shop",
                                             "coffee shop":"Coffee/Beverage Shop",
                                             "Coffee shop":"Coffee/Beverage Shop",
                                             "COFFEE SHOP":"Coffee/Beverage Shop",
                                             "CAFE/STORE":"Coffee/Beverage Shop",
                                             "JUICE AND SALAD BAR":"Coffee/Beverage Shop",
                                             "JUICE BAR":"Coffee/Beverage Shop",
                                             "MILK TEA":"Coffee/Beverage Shop",
                                             "SHAKES/TEAS":"Coffee/Beverage Shop",
                                             "smoothie bar":"Coffee/Beverage Shop",
                                             "Internet Cafe":"Coffee/Beverage Shop",
                                             "CONVENIENCE STORE": "Gas Station/Convenience",
                                             "convenience store": "Gas Station/Convenience",
                                             "convenience": "Gas Station/Convenience",
                                             "convenience/drug store": "Gas Station/Convenience",
                                             "CONVENIENCE/GAS STATION": "Gas Station/Convenience",
                                             "CONVENIENT STORE": "Gas Station/Convenience",
                                             "GAS STATION FOOD STORE": "Gas Station/Convenience",
                                             "GAS STATION STORE": "Gas Station/Convenience",
                                             "GAS STATION": "Gas Station/Convenience",
                                             "gas station": "Gas Station/Convenience",
                                             "GAS STATION/CONVENIENCE STORE": "Gas Station/Convenience",
                                             "GAS STATION/FOOD": "Gas Station/Convenience",
                                             "GAS STATION/GROCERY": "Gas Station/Convenience",
                                             "GAS STATION/MINI MART": "Gas Station/Convenience",
                                             "GAS STATION/RESTAURANT": "Gas Station/Convenience",
                                             "GAS STATION/STORE": "Gas Station/Convenience",
                                             "CHURCH (SPECIAL EVENTS)":"Hospital/Church/Community",
                                             "CHURCH KITCHEN":"Hospital/Church/Community",
                                             "CHURCH":"Hospital/Church/Community",
                                             "Church":"Hospital/Church/Community",
                                             "CHURCH/SPECIAL EVENTS":"Hospital/Church/Community",
                                             "Hospital":"Hospital/Church/Community",
                                             "NOT-FOR-PROFIT CLUB":"Hospital/Church/Community",
                                             "CHARITY AID KITCHEN":"Hospital/Church/Community",
                                             "Shelter":"Hospital/Church/Community",
                                             "HOSTEL": "Hospitality",
                                             "HOTEL": "Hospitality",
                                             "1475 LIQUOR": "Liqour Sale/Bar",
                                             "BAR": "Liqour Sale/Bar",
                                             "bar": "Liqour Sale/Bar",
                                             "BREWERY": "Liqour Sale/Bar",
                                             "BREWPUB": "Liqour Sale/Bar",
                                             "CATERED LIQUOR": "Liqour Sale/Bar",
                                             "DISTILLERY WITH TASTING ROOM": "Liqour Sale/Bar",
                                             "LIQOUR BREWERY TASTING": "Liqour Sale/Bar",
                                             "liquor store": "Liqour Sale/Bar",
                                             "Liquor": "Liqour Sale/Bar",
                                             "LIQUOR/COFFEE KIOSK": "Liqour Sale/Bar",
                                             "MOBIL FOOD PREPARED": "Mobile Food",
                                             "MOBILE DESSERTS VENDOR": "Mobile Food",
                                             "Mobile Food Dispenser": "Mobile Food",
                                             "Mobile Food Preparer": "Mobile Food",
                                             "MOBILE FOOD TRUCK": "Mobile Food",
                                             "MOBILE FOOD": "Mobile Food",
                                             "Mobile Frozen Desserts Vendor": "Mobile Food",
                                             "Mobile Prepared Food Vendor": "Mobile Food",
                                             "MOBILE PUSH CART": "Mobile Food",
                                             "MOBILPREPARED FOOD VENDOR": "Mobile Food",
                                             "FLEA MARKET": "Mobile Food",
                                             "FOOD BOOTH": "Mobile Food",
                                             "POPCORN CORN": "Mobile Food",
                                             "Navy Pier Kiosk": "Mobile food",
                                             "Animal Shelter Cafe Permit": "Other",
                                             "Airport Lounge": "Other",
                                             "ARCHDIOCESE": "Other",
                                             "BEVERAGE/SILVERWARE WAREHOUSE": "Other",
                                             "CAFETERIA": "Other",
                                             "Cafeteria": "Other",
                                             "CHILDRENS SERVICES FACILITY": "Other",
                                             "CLOTHING STORE": "Other",
                                             "COLD/FROZEN FOOD STORAGE": "Other",
                                             "COMMISSARY": "Other",
                                             "DISTRIBUTION CENTER": "Other",
                                             "Food Pantry": "Other",
                                             "FRENCH MARKET SPACE": "Other",
                                             "FURNITURE STORE": "Other",
                                             "Gift Shop": "Other",
                                             "GOLF COURSE CONNCESSION STAND": "Other",
                                             "GREENHOUSE": "Other",
                                             "hair salon": "Other",
                                             "Hair Salon": "Other",
                                             "HAIR SALON": "Other",
                                             "HELICOPTER TERMINAL": "Other",
                                             "HOT DOG STATION": "Other",
                                             "KIOSK": "Other",
                                             "KITCHEN DEMO": "Other",
                                             "KITCHEN": "Other",
                                             "Laundromat": "Other",
                                             "MOVIE THEATER": "Other",
                                             "MOVIE THEATRE": "Other",
                                             "Other": "Other",
                                             "OUTREACH CULINARY KITCHEN": "Other",
                                             "PACKAGED HEALTH FOODS": "Other",
                                             "PRE PACKAGED": "Other",
                                             "REGULATED BUSINESS": "Other",
                                             "REPACKAGING PLANT": "Other",
                                             "Shared Kitchen User (Long Term)": "Other",
                                             "Shared Kitchen User (Short Term)": "Other",
                                             "Shared Kitchen": "Other",
                                             "Shuffleboard Club with Bar": "Other",
                                             "STADIUM": "Other",
                                             "TEST KITCHEN/ STORAGE": "Other",
                                             "THEATER": "Other",
                                             "THEATRE": "Other",
                                             "TOBACCO STORE": "Other",
                                             "UNUSED STORAGE": "Other",
                                             "VENDING COMMISSARY": "Other",
                                             "WAREHOUSE": "Other",
                                             "ART CENTER": "Professional School",
                                             "A-Not-For-Profit Chef Training Program": "Professional School",
                                             "cooking school": "Professional School",
                                             "COOKING SCHOOL": "Professional School",
                                             "CULINARY SCHOOL": "Professional School",
                                             "PASTRY SCHOOL": "Professional School",
                                             "PASTRY school": "Professional School",
                                             "Restaurant": "Resturant",
                                             "RESTAURANT/BAR": "Resturant",
                                             "RESTAURANT/BAR/THEATER": "Resturant",
                                             "RIVERWALK": "Resturant",
                                             "ROOF TOP": "Resturant",
                                             "ROOF TOPS": "Resturant",
                                             "ROOFTOP": "Resturant",
                                             "ROOFTOPS": "Resturant",
                                             "SUSHI COUNTER": "Resturant",
                                             "TAVERN": "Resturant",
                                             "tavern": "Resturant",
                                             "TAVERN/STORE": "Resturant",
                                             "Wrigley Roof Top": "Resturant",
                                             "WRIGLEY ROOFTOP": "Resturant",
                                             "COMMISARY RESTAURANT": "Resturant",
                                             "DINING HALL": "Resturant",
                                             "Golden Diner": "Resturant",
                                             "Pop-Up Establishment Host-Tier II": "Resturant",
                                             "Pop-Up Establishment Host-Tier III": "Resturant",
                                             "Pop-Up Food Establishment User-Tier II": "Resturant",
                                             "Pop-Up Food Establishment User-Tier III": "Resturant",
                                             "RETAIL STORE OFFERS COOKING CLASSES": "Retail Store",
                                             "RETAIL": "Retail Store",
                                             "LIVE POULTRY SLAUGHTER FACILITY": "Slaughter/Live ",
                                             "LIVE POULTRY": "Slaughter/Live ",
                                             "Live Poultry": "Slaughter/Live ",
                                             "POULTRY SLAUGHTER": "Slaughter/Live ",
                                             "Poultry Slaughter": "Slaughter/Live",
                                             "SLAUGHTER HOUSE/ GROCERY": "Slaughter/Live",
                                             "BUTCHER SHOP": "Slaughter/Live",
                                             "butcher shop": "Slaughter/Live",
                                             "CUSTOM POULTRY SLAUGHTER": "Slaughter/Live",
                                             "SUMMER FEEDING PREP AREA": "Slaughter/Live",
                                             'Daycare':"Childcare/School",
                                             "DOLLAR & GROCERY STORE'": "Grocery store",
                                             "DOLLAR STORE WITH GROCERY'": "Grocery store",
                                             "DOLLAR STORE'": "Grocery store",
                                             "DOLLAR TREE'": "Grocery store",
                                             "DRUG STORE'": "Grocery store",
                                             "DRUG STORE/GROCERY'": "Grocery store",
                                             "GROCERY & LIQUOR STORE'": "Grocery store",
                                             "Grocery & Restaurant'": "Grocery store",
                                             "GROCERY AND BUTCHER'": "Grocery store",
                                             "GROCERY STORE /PHARMACY'": "Grocery store",
                                             "Grocery Store'": "Grocery store",
                                             "GROCERY STORE'": "Grocery store",
                                             "GROCERY STORE/BAKERY'": "Grocery store",
                                             "GROCERY STORE/COOKING SCHOOL'": "Grocery store",
                                             "GROCERY STORE/GAS STATION'": "Grocery store",
                                             "GROCERY(GAS STATION)'": "Grocery store",
                                             "Grocery(Sushi prep)'": "Grocery store",
                                             "GROCERY/BAKERY'": "Grocery store",
                                             "GROCERY/DELI'": "Grocery store",
                                             "grocery/dollar store'": "Grocery store",
                                             "GROCERY/DRUG STORE'": "Grocery store",
                                             "GROCERY/GAS STATION'": "Grocery store",
                                             "GROCERY/RESTAURANT'": "Grocery store",
                                             "GROCERY/TAQUERIA'": "Grocery store",
                                             "GROCERY& RESTAURANT'": "Grocery store",
                                             "JUICE BAR/GROCERY'": "Grocery store",
                                             "LIQUOR/GROCERY STORE/BAR'": "Grocery store",
                                             "REST/GROCERY']": "Grocery store",
                                             "RESTAURANT/GROCERY STORE'": "Grocery store",
                                             "DELI/GROCERY STORE'": "Grocery Store",
                                             "STORE'": "Grocery Store",
                                             "WHOLESALE & RETAIL'": "Grocery Store",
                                             "Wholesale'": "Grocery Store",
                                             'Grocery(Sushi prep)': "Grocery Store",
                                             "Grocery & Restaurant": "Grocery Store",
                                             "GROCERY & LIQUOR STORE'": "Grocery Store",
                                             "GROCERY/GAS STATION": "Grocery Store",
                                             "GROCERY/TAQUERIA": "Grocery Store",
                                             "GROCERY/RESTAURANT": "Grocery Store",
                                             "DOLLAR STORE WITH GROCERY": "Grocery Store",
                                             "GROCERY/GAS STATION": "Grocery Store",
                                             'GROCERY STORE/COOKING SCHOOL':"Grocery Store",
                                             'Grocery & Restaurant':"Grocery Store",
                                             'GROCERY/BAKERY':"Grocery Store",
                                             'GROCERY STORE':"Grocery Store",
                                             'DOLLAR STORE WITH GROCERY':"Grocery Store",
                                             'LIQUOR/GROCERY STORE/BAR':"Grocery Store",
                                             'DOLLAR STORE':"Grocery Store",
                                             'DOLLAR TREE':"Grocery Store",
                                             'RESTAURANT/GROCERY STORE':"Grocery Store",
                                             'STORE':"Grocery Store",
                                             'GROCERY STORE /PHARMACY':"Grocery Store",
                                             'GROCERY& RESTAURANT':"Grocery Store",
                                             'GROCERY/DRUG STORE':"Grocery Store",
                                             'GROCERY AND BUTCHER':"Grocery Store",
                                             'GROCERY(GAS STATION)':"Grocery Store",
                                             'DELI/GROCERY STORE':"Grocery Store",
                                             'Resturant ':"Resturant",
                                             'Grocery(Sushi prep)':"Grocery Store",
                                             'Wholesale':"Other",
                                             'GROCERY STORE/GAS STATION':"Grocery Store",
                                             'GROCERY & LIQUOR STORE':"Grocery Store",
                                             'GROCERY/GAS STATION':"Grocery Store",
                                             'GROCERY/TAQUERIA':"Grocery Store",
                                             'REST/GROCERY':"Grocery Store",
                                             'Rest/GYM':"Herbal/Health/Fitness Store",
                                             'HERBAL LIFE SHOP':"Herbal/Health/Fitness Store",
                                             'HEALTH FOOD STORE':"Herbal/Health/Fitness Store",
                                             'JUICE BAR/GROCERY':"Herbal/Health/Fitness Store",
                                             "GYM":"Herbal/Health/Fitness Store",
                                             'FITNESS STUDIO':"Herbal/Health/Fitness Store",
                                             'Herbalife Nutrition':"Herbal/Health/Fitness Store",
                                             'Herabalife':"Herbal/Health/Fitness Store",
                                             'HERBALIFE/ZUMBA':"Herbal/Health/Fitness Store",
                                             'FITNESS CENTER':"Herbal/Health/Fitness Store",
                                             'Herbalife Nutrition':"Herbal/Health/Fitness Store",
                                             'HERBAL LIFE':"Herbal/Health/Fitness Store",
                                             'HERBALIFE':"Herbal/Health/Fitness Store",
                                             'WEIGHT LOSS PROGRAM':"Herbal/Health/Fitness Store",
                                             'NUTRITION SHAKES':"Herbal/Health/Fitness Store",
                                             'HERBALIFE STORE':"Herbal/Health/Fitness Store",
                                             'WEIGHT LOSS PROGRAM':"Herbal/Health/Fitness Store",
                                             'GYM STORE':"Herbal/Health/Fitness Store",
                                             'HERBAL DRINKS':"Herbal/Health/Fitness Store",
                                             'HEALTH CARE STORE':"Herbal/Health/Fitness Store",
                                             'SPA':"Herbal/Health/Fitness Store",
                                             'Restaurant(protein shake bar)':"Herbal/Health/Fitness Store",
                                             'GROCERY/DELI':"Grocery Store",
                                             'Slaughter/Live ':"Slaughter/Live",
                                             'GROCERY/DELI':"Grocery Store",
                                             'GROCERY STORE/BAKERY':"Grocery Store",
                                             'DRUG STORE/GROCERY':"Gas Station/Convenience",
                                             'DRUG STORE':"Gas Station/Convenience",
                                             'employee kitchen':"Other",
                                             'WHOLESALE & RETAIL':"Other",
                                             'DOLLAR & GROCERY STORE':"Grocery Store",
                                             'grocery/dollar store':"Grocery Store",
                                             }})

# # Total Inspections by Zip Code

		
	zip_df= df_new.groupby(["zip"],as_index=False).results.count()
	zip_df=zip_df.sort_values(by= ["results"], ascending = False)
	zip_df.rename(columns= {"results": "total_count"}, inplace= True)
	

	# # Fail Data
	df_fail= df_new[df_new['results']=="Fail"]

	# # Fail Count by Zipcode
	df_fail_zip= df_fail.groupby("zip", as_index=False)["results"].agg("count")

	df_fail_zip=df_fail_zip.sort_values(by= ["results"], ascending = False)
	df_fail_zip.rename(columns= {"results": "fail_count"}, inplace= True)


	# # Pass Data	
	df_pass= df_new[df_new['results']=="Pass"]


	# # Pass Count by Zipcode
	df_pass_zip= df_pass.groupby("zip", as_index=False)["results"].agg("count")

	df_pass_zip=df_pass_zip.sort_values(by= ["results"], ascending = False)
	df_pass_zip.rename(columns= {"results": "pass_count"}, inplace= True)

	# # Pass with Conditions Data
	df_pass_w_cond= df_new[df_new['results']=="Pass w/ Conditions"]
	df_pass_w_cond_zip= df_pass_w_cond.groupby("zip", as_index=False)["results"].agg("count")
	df_pass_w_cond_zip=df_pass_w_cond_zip.sort_values(by= ["results"], ascending = False)
	df_pass_w_cond_zip.rename(columns= {"results": "pass__w_cond_count"}, inplace= True)


	# # Total Count by Zipcode
	df_zip_total_count= df_pass_w_cond_zip.merge(df_fail_zip, left_on='zip', right_on='zip')
	df_zip_total_count=df_zip_total_count.merge(df_pass_zip, left_on='zip', right_on='zip')
	df_zip_total_count=df_zip_total_count.merge(zip_df, left_on='zip', right_on='zip')
	df_zip_total_count["percent_fail"]=df_zip_total_count["fail_count"]/df_zip_total_count["total_count"]*100
	df_zip_total_count["percent_pass"]=df_zip_total_count["pass_count"]/df_zip_total_count["total_count"]*100
	df_zip_total_count["percent_pass_w_con"]=df_zip_total_count["pass__w_cond_count"]/df_zip_total_count["total_count"]*100
	df_zip_total_count["zip"]=df_zip_total_count["zip"].astype(int)
	

	# # Import IRS Adjusted Gross Income Data
	AGI=pd.read_csv("AGI_IRS.csv")
	AGI.head()

	# merge df
	df_zip_total_count=df_zip_total_count.merge(AGI, left_on='zip', right_on='zip')
	df_new=df_zip_total_count.merge(df_new, left_on='zip', right_on='zip')
	
	df_new.to_csv("Inspections_df.csv")


