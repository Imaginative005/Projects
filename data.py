'''
Import or download all the datasets here for analaysis and evaluations from:
        https://www.nass.usda.gov/Publications/AgCensus/2017/Full_Report/Volume_1,_Chapter_2_US_State_Level/
'''

import pandas
import requests
import matplotlib.pyplot as plt
from datetime import datetime
import pandas
import os


# read the public debits datasets
def public_debit():
    with open("Public Debits.csv") as public_debit:
        data_public_csv = pandas.read_csv(public_debit)
        types_data = data_public_csv.dtypes
        # fiscal_year = data_public_csv['Fiscal Year to Date Expense Amount']
        return f" The current Month Expense Amount\n{data_public_csv['Current Month Expense Amount']}\nand the Fiscal " \
               f"year \n{data_public_csv} and \n{types_data}"

        # print(data['Fiscal Year'])


# print(public_debit())


class DataSetsAgriCensus():
    def __init__(self, data=None):
        self.datasets = data

    def agric_nj(self):
        with open('2017-agcensus-chapter2-table1-NJ.csv') as data_file:
            nj_census_csv = pandas.read_csv(data_file)
            return f'2017 agriculture census for New Jersey \n{nj_census_csv}'

    def agricensus(self):
        with open("2017-agcensus-chapter2-table1-US(1).csv") as data_census:
            us_total_csv = pandas.read_csv(data_census)
            return f"Area operated:\n{us_total_csv['domain category']}"

    def agric_ny(self):
        with open("2017-agcensus-chapter2-table1-NY.csv") as data_ny:
            ny_census_csv = pandas.read_csv(data_ny)
            return f"2017 agriculture census for New York: \n{ny_census_csv}"

    def agric_il(self):
        with open("2017-agcensus-chapter2-table1-IL.csv") as data_IL:
            il_census_csv = pandas.read_csv(data_IL)
            # print(IL_census_csv)
            return f"2017 agriculture census: \n{il_census_csv}"

    def agric_ks(self):
        with open("2017-agcensus-chapter2-table1-KS.csv") as data_KS:
            ks_census_csv = pandas.read_csv(data_KS)
            return f"2017 agriculture Kansas census: \n{ks_census_csv}"

    def agric_ne(self):
        with open('2017-agcensus-chapter2-table1-NE.csv') as data_NE:
            ne_census_csv = pandas.read_csv(data_NE)
            return f"2017 agriculture Nebraka census: \n{ne_census_csv}"

    def agric_oh(self):
        with open('2017-agcensus-chapter2-table1-OH.csv') as data_OH:
            oh_census = pandas.read_csv(data_OH)
            return f"2017 agriculture Ohio census: \n{oh_census}"

    def agric_south_dokota(self):
        with open('2017-agcensus-chapter2-table1-SD.csv') as data_SD:
            sd_census = pandas.read_csv(data_SD)
            return f"2017 agriculture South Dekota census \n{sd_census}"

    def agric_texas(self):
        with open('2017-agcensus-chapter2-table1-TX.csv') as data_TX:
            tx_census_csv = pandas.read_csv(data_TX)
            # print(tx_census_csv)
            return f"2017 agriculture Texas census\n{tx_census_csv}"

    def agric_annual_crop_production(self):
        with open("DataSets/Crop Production Annual Summary/crop_all_tables.csv") as data_all_tables:
            acreage_csv = pandas.read_csv(data_all_tables, on_bad_lines='skip')
            # print(acreage.dtypes)
            # return f" Crop Production Annual Summary: \n{acreage_csv}"
            data_dict_acreage = pandas.DataFrame.to_dict(acreage_csv)
            return f'Crop Production Annual Summary \n{data_dict_acreage}'

    # Agricultural land values
    def agricultural_land_values(self):
        with open("DataSets/Agricultural Land Values/land_all_tables.csv") as data_files:
            all_lands = pandas.read_csv(data_files, on_bad_lines='skip')
            # print(all_lands.dtypes)
            # print(all_lands)
            data_all_land_values = pandas.DataFrame.to_dict(all_lands)
            # print(data.keys())
            states_land_values = data_all_land_values[
                'Land Values 2022 Summary: Released August 5, 2022, by the National Agricultural Statistics ' \
                'Service (''NASS), Agricultural Statistics Board, United States Department of Agriculture (' \
                'USDA).']

            return f'Agricultural Land Values\n{states_land_values}'

    # Crop Production Annual Summary
    def crop_production_annual_summary(self):
        with open("DataSets/Crop Production Annual Summary/crop_all_tables.csv") as data_crop:
            crop_all_tables = pandas.read_csv(data_crop, on_bad_lines='skip')
            # print(crop_all_tables)
            # convert to dictionary
            data_annual_crop_prod = pandas.DataFrame.to_dict(crop_all_tables)

            #     if 'Crop Production':
            # print(data['221'])
            # print(crop_all_tables.dtypes)
            return f'Crop Production Annual Summary:\n{data_annual_crop_prod}'

    def agriculture_prices(self):
        with open("DataSets/Agricultural Prices/agpr_all_tables.csv") as agric_data:
            agric_csv_data = pandas.read_csv(agric_data, on_bad_lines='skip')
            # print(agric_csv_data)
            # convert data into dict
            data_dict_prices = pandas.DataFrame.to_dict(agric_csv_data)
            # print(data_dict)
            # pprint.pprint(data_dict)
            return f"Agricultural Prices\n{data_dict_prices}"

    def cattles(self):
        with open("DataSets/cattle/catl_all_tables.csv") as cattles_tables:
            cattle_data = pandas.read_csv(cattles_tables, on_bad_lines='skip')
            # print(cattle_data)
            data_dict_cattle = pandas.DataFrame.to_dict(cattle_data)
            # print(data_dict)
            return f"Cattles: \n{cattle_data}"

    def cold_storage(self):
        with open("DataSets/Cold Storage/cost_all_tables.csv") as cold_storage:
            cold_storage_data = pandas.read_csv(cold_storage, on_bad_lines='skip')
            # print(cold_storage_data)
            data_dict_cold_storage = pandas.DataFrame.to_dict(cold_storage_data)
            # print(data_dict)
            return f"Cold Storage: \n{cold_storage_data}"

    def cotton_ginnings(self):
        with open("DataSets/Cotton Ginnings/ctgn_all_tables.csv") as csv_data:
            data_csv = pandas.read_csv(csv_data, on_bad_lines='skip')
            # print(data_csv)
            data_dict_cotton = pandas.DataFrame.to_dict(data_csv)
            # print(data_dict)
            return f"Cotton Ginnings \n{data_dict_cotton}"

    def crop_production(self):
        with open("DataSets/Crop Production/crop_all_tables.csv") as crop_data:
            data_csv = pandas.read_csv(crop_data, on_bad_lines='skip')
            # print(data_csv)
            data_dict_crop = pandas.DataFrame.to_dict(data_csv)
            # print(data_dict)
            return f"Crop Production: \n{data_dict_crop}"

    def crop_progress(self):
        with open("DataSets/Crop Progress/prog_all_tables.csv") as crop_prog:
            data_csv = pandas.read_csv(crop_prog, on_bad_lines='skip')
            # print(data_csv)
            data_dict = pandas.DataFrame.to_dict(data_csv)
            # print(data_dict)
            return f"Crop Progress: \n{data_dict}"

    def farm_labor(self):
        with open("DataSets/Farm Labor/fmla_all_tables.csv") as farm_labor:
            farm_la = pandas.read_csv(farm_labor, on_bad_lines='skip')
            # print(f'Farm labor code number and data: \n{farm_la}')
            farm_labor_dict = pandas.DataFrame.to_dict(farm_la)
            # print(farm_labor)
            return f"Farm labor: \n{farm_labor_dict}"

    def grain_stocks(self):
        with open('DataSets/Grain Stocks/grst_all_tables.csv') as grain_data:
            data_grain_csv = pandas.read_csv(grain_data, on_bad_lines='skip')
            # print(data_grain_csv)
            data_dict_grain = pandas.DataFrame.to_dict(data_grain_csv)
            # print(f'Grain stocks\n{data_dict_grain}')
            return f"Grain Stocks: \n{data_dict_grain}"

    def hogs_and_pigs(self):
        with open('DataSets/Hogs and Pigs/hgpg_all_tables.csv') as hog_pigs:
            data_hog_pigs = pandas.read_csv(hog_pigs, on_bad_lines='skip')
            # print(f'Hogs and Pigs dataset\n{data_hog_pigs}')
            hog_pigs_ = pandas.DataFrame.to_dict(data_hog_pigs)
            # print(f'Hogs and Pigs dataset\n{hog_pigs_}')
            return f"Hogs and Pigs: \n{hog_pigs_}"

    def milk_production(self):
        with open('DataSets/Milk Production/mkpr_all_tables.csv') as milk_prod:
            data_milk_csv = pandas.read_csv(milk_prod, on_bad_lines='skip')
            # print(f'Milk production\n{data_milk_csv}')
            data_milk_dict = pandas.DataFrame.to_dict(data_milk_csv)
            # print(f'Milk production value in dict\n{data_milk_dict}')
            return f"Milk production \n{data_milk_csv}"

    def prospective_plantings(self):
        with open("DataSets/Prospective Plantings/pspl_all_tables.csv") as pros_plant:
            pros_plant_csv = pandas.read_csv(pros_plant, on_bad_lines='skip')
            # print(f'Prospective Planting\n{pros_plant_csv}')
            data_pros_plant = pandas.DataFrame.to_dict(pros_plant_csv)
            # print(f'The Prospective Planting\n{data_pros_plant}')
            return f"Prospective Plantings \n{data_pros_plant}"

    def rice_stocks(self):
        with open("DataSets/Rice Stocks/rice_all_tables.csv") as rice_stocks:
            rice_stocks_data = pandas.read_csv(rice_stocks, on_bad_lines='skip')
            # print(f'The dataset for Rice stocks\n{rice_stocks_data}')
            data_dict_rice = pandas.DataFrame.to_dict(rice_stocks_data)
            # print(f'The dataset for Rice stocks\n{data_dict_rice}')
            return f"Rice Stocks \n{data_dict_rice}"

    def small_grains_annual_summary(self):
        with open("DataSets/Small Grains Annual Summary/smgr_all_tables.csv") as small_grains_annual:
            small_grains = pandas.read_csv(small_grains_annual, on_bad_lines='skip')
            # print(f'The Small Grains Annual Summary\n{small_grains}')
            data_small_grains = pandas.DataFrame.to_dict(small_grains)
            return f'The Small Grains Annual Summary\n{data_small_grains}'




# USE Organic Production for each states to assign bonus points for tax break
class OrganicProductions():

    # def __init__(self):
    #     self.farmland_livestock_and_farm = None
    #     self.data_file = None

    def beans_xls(self):
        # self.beans = datasets
        beans = pandas.read_excel("Organic Production/Beans.xls")
        return f'Excel file for beans production for each states:\n{beans}'

    def beans_states(self):
        data_file = pandas.read_excel("Organic Production/Beans.xls")
        # print(data_file.dtypes)
        # print(f'Total numbers of organic beans production for each states\n{data_file}')
        data_beans_dict = data_file.to_dict()
        # print(data_beans_dict)
        # access the keys
        # print(f' beans key value: \n{data_beans_dict.keys()}')
        # return data_beans_dict['Table 7--U.S. certified organic beans, by State, 2011']
        return data_beans_dict
        # print(f"beans key value: \n{data_beans_dict['Unnamed: 1']}")
        # 'Table 7--U.S. certified organic beans, by State, 2011

        # U_S_certified_organic_beans = data_beans_dict['Table 7--U.S. certified organic beans, by State, 2011']
        # return f'Total numbers of organic beans production for each states:\n{U_S_certified_organic_beans}'
        # print(U_S_certified_organic_beans.items())

    # Certified Organic by states
    def certified(self):
        certified = pandas.read_excel("Organic Production/Certifiers.xls")
        # print(certified)
        # print(certified.to_json)
        # convert to dictionary
        certified_dict = certified.to_dict()
        # print(certified_dict['Table 1--USDA-accredited organic certification programs active in 2002 through 2011 1/'])

        # dict_item = {key:item for (key, item) in certified_dict.iterrows()}
        # print(dict_item)

        return f'Certified records {certified.to_records()}'

    # print(certified.to_records().dtype)

    # Farm land and livestock
    def farmland_livestock(self):
        # self.farmland_livestock_and_farm = datasets
        farmland_livestock_and_farm = pandas.read_excel("Organic Production/Farmlandlivestockandfarm.xls")

        # print(farmland_livestock_and_farm)

        farmland_livestock_and_farm_dict = pandas.DataFrame.to_dict(farmland_livestock_and_farm)
        return f'Farmland livestock \n{farmland_livestock_and_farm_dict}'

    # extract fruit data production by each states
    def fruits_states(self):
        fruits = pandas.read_excel("Organic Production/Fruit.xls")
        # print(fruits.head())
        # check each records
        records = fruits.to_records()
        # print(records.dtype)
        # print(f'Table 11--Certified organic fruit acreage, by State, 2011:\n{records}')
        # Access all Table 11--Certified organic fruit acreage, by State, 2011'

        # data_records = records['Table 11--Certified organic fruit acreage, by State, 2011']
        # print(f'States records:\n{data_records}')
        fruits_dict = pandas.DataFrame.to_dict(fruits)
        # print(f'The keys in the fruit dictionary for each states:\n{fruits_dict.keys()}')
        # print(f'The items in the fruit dictionary for each states:\n{fruits_dict.items()}')
        # print(
        # f'Organic Fruits production for each states\n{fruits_dict["Table 11--Certified organic fruit acreage, by State, 2011"][0] == "State"}')

        return f'Organic Fruits production for each states:\n{fruits_dict}'

    # Greenhouse and uses light and no chemical get 0.5 bonus point
    def greenhouse(self):
        green_house_xl = pandas.read_excel("Organic Production/Greenhouse.xls")
        # return f'Greenhouse for each states: \n{green_house_xl.values}'
        data_green = pandas.DataFrame.to_dict(green_house_xl)
        return f'Greenhouse for each states: \n{data_green}'
    def haysilage(self):
        haysilage = pandas.read_excel("Organic Production/Haysilage.xls")
        return f'Haysilage \n{haysilage}'

    def livestock(self):
        livestock = pandas.read_excel("Organic Production/Livestock.xls")
        return f'Livestock\n{livestock}'

    def other_crops(self):
        other_crops = pandas.read_excel("Organic Production/Othercrops.xls")
        return f'Other crops\n{other_crops}'

    def paster_crops_by_states(self):
        paster_crops = pandas.read_excel("Organic Production/PastrCropbyState.xls")
        return f'Paster Crop by State:\n{paster_crops}'

    def vegetables(self):
        vegetables = pandas.read_excel("Organic Production/Vegetables.xls")
        return f'{vegetables}'

debt = public_debit()
organic = OrganicProductions()
print(organic.vegetables())
print(organic.other_crops())
print(organic.beans_states())
print(organic.certified())
print(organic.beans_xls())
print(organic.vegetables())
print(organic.fruits_states())
print(organic.livestock())
print(organic.haysilage())
print(organic.paster_crops_by_states())
print(organic.greenhouse())




