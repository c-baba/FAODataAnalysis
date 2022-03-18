import pandas as pd
import matplotlib.pyplot as plt
import csv
import os
import glob
os.chdir("C://Users//cevdet.baba//PycharmProjects//faoproject")

pd.set_option('display.max_columns', None)


df = pd.read_csv("Trade_Indices_E_All_Data.csv",encoding='latin-1')

dbfood = df.loc[:,~df.columns.str.contains('F')]


dbfood.columns = dbfood.columns.str.lstrip("Y") #delete "Y" String ffrom colums

dbfood = dbfood.fillna(0)

listofcoutry = ['Afghanistan', 'Albania', 'Algeria', 'Argentina', 'Australia', 'Austria', 'Bangladesh',
                     'Bhutan' \
              'Brazil', 'Bulgaria', 'Burkina Faso', 'Cameroon',
                       'Canada', 'Chad', 'Chile', 'China, Hong Kong SAR' \
              , 'China, mainland', 'China, Taiwan Province of', 'Colombia', 'Comoros', 'Congo',
                       'Costa Rica', "Co´te d'Ivoire", 'Cuba', 'Cyprus', \
                       'Democratic Republic of the Congo', 'Denmark',
                      'Dominican Republic', 'Ecuador', 'Egypt' \
              , 'El Salvador', 'Equatorial Guinea', 'Eswatini', 'Fiji', 'Finland', 'France',
                        'Germany', 'Ghana', 'Greece', 'Grenada', 'Guinea',
                          'Hungary', 'India', 'Indonesia',
                       'Iran (Islamic Republic of)', 'Iraq', 'Ireland',
                       'Israel', 'Italy', 'Jamaica', 'Japan', 'Jordan', 'Kenya', 'Kuwait',
                       'Lebanon','Liberia', 'Madagascar', 'Malaysia', 'Mali', 'Malta','Mexico'
                       , 'Morocco', 'Myanmar', 'Nepal'
              , 'Netherlands', 'New Zealand',  'Niger', 'Nigeria', 'Norway', 'Pakistan', 'Panama',
                       'Papua New Guinea', 'Paraguay', 'Peru'
              , 'Philippines', 'Poland', 'Portugal', 'Republic of Korea', 'Romania',
                        'Samoa', 'Saudi Arabia', 'Senegal','Singapore', 'Solomon Islands', 'South Africa',
                'Spain', 'Sri Lanka', 'Sweden', 'Switzerland','Syrian Arab Republic', 'Thailand',
                       'Togo', 'Tonga', 'Trinidad and Tobago', 'Tunisia', 'Turkey', 'Uganda',
                       'United Kingdom of Great Britain and Northern Ireland', 'United Republic of Tanzania',
                       'United States of America', 'Uruguay', 'Vanuatu', 'Venezuela (Bolivarian Republic of)'
              ,'Viet Nam', 'Yemen', 'Zimbabwe']

listagriculture = ['Apples', 'Bananas', 'Barley', 'Beer of barley', 'Cereal preparations nes', 'Cocoa, beans',
                   'Coconuts', 'Coconuts, desiccated', 'Copra', 'Cotton lint', 'Cottonseed', 'Dates',
                   'Fruit, fresh nes', 'Grapes', 'Groundnuts, shelled', 'Jute', 'Lemons and limes', 'Linseed', 'Maize',
                   'Malt', 'Oats', 'Oil, castor beans', 'Oil, coconut (copra)', 'Oil, cottonseed', 'Oil, groundnut',
                   'Oil, linseed', 'Oil, maize', 'Oil, olive, virgin', 'Oil, palm', 'Oil, palm kernel', 'Oil, rapeseed',
                   'Oil, soybean', 'Oil, sunflower', 'Oil, vegetable origin nes', 'Onions, dry', 'Oranges',
                   'Peaches and nectarines', 'Pears', 'Pepper (piper spp.)', 'Pigs', 'Pineapples', 'Pineapples canned',
                   'Potatoes', 'Raisins', 'Rapeseed', 'Rice, milled', 'Roots and tubers nes', 'Rubber natural dry',
                   'Sesame seed', 'Soybeans', 'Spices nes', 'Sunflower seed', 'Tea', 'Tobacco, unmanufactured',
                   'Tobacco products nes', 'Tomatoes', 'Walnuts, shelled', 'Wheat']


year = ['1961',
              '1962', '1963', '1964', '1965', '1966', '1967', '1968', '1969', '1970', '1971', '1972', '1973', '1974', '1975',
              '1976', '1977', '1978', '1979', '1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987', '1988', '1989', '1990',
              '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005',
              '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020']
dbfood.loc[:,['1961',
              '1962', '1963', '1964', '1965', '1966', '1967', '1968', '1969', '1970', '1971', '1972', '1973', '1974', '1975',
              '1976', '1977', '1978', '1979', '1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987', '1988', '1989', '1990',
              '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005',
              '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020']] *= 1000


a = ["Area Code","Item Code","Element Code","Unit"]
for i in a:
       del dbfood[i]



#worldinformation
def worldinformation():
    #dünya genel bilgiler
       worlddb =dbfood.loc[dbfood["Area"]=="World"]

       worldbimport = worlddb.loc[worlddb["Element"]=="Import Value Base Period Price"]
       worldb2020import =worldbimport[["Item","2020"]]
       worldimport2020=worldb2020import.sort_values(by=["2020"],ascending=False)

       worldimport2020.to_csv("worldimport2020.csv")

       worlddbexport =worlddb.loc[worlddb["Element"]=="Export Value Base Price"]
       worldb2020export =worlddbexport[["Item","2020"]]
       worldexport2020=worldb2020export.sort_values(by=["2020"],ascending=False)
       worldexport2020.to_csv("worldexport2020.csv")


#---------------------------------------------------------------------------------------------------------------------------
#2020 agricultural import data
def agriculturaldatacoutry2020():
    #2020 yılı en çok tarım ürünü ihracat ve ithalatı ülkeler
    df = dbfood.loc[dbfood["Item"]=="Agricultural Products"]
    df2020agricultural = df[df['Area'].isin(listofcoutry)]


    df2020import = df2020agricultural.loc[df2020agricultural["Element"]=="Import Value Base Period Price"]


    df2020importcountryvalues = df2020import.groupby("Area").mean()
    da = df2020importcountryvalues.sort_values(by=["2020"],ascending=False)
    dd = da.round({"2020":0})


    dd.to_csv("db2020importcountryvalues.csv")

    #---------------------------------------------------------------------------------------------------------------------------

     #2020 export data

    df2020export = df2020agricultural.loc[df2020agricultural["Element"]=="Export Value Base Price"]

    df2020exportcountryvalues = df2020export.groupby("Area").mean()
    da = df2020exportcountryvalues.sort_values(by=["2020"],ascending=False)
    dd = da.round({"2020":0})

    dd.to_csv("df2020exportcountryvalues.csv")

agriculturaldatacoutry2020()
def agriculturalproductexportandimport():

    #belirlenen ürünlerde yıl yıl en çok ithal edilen ürünler

    df2020agricultural = dbfood[dbfood['Item'].isin(listagriculture)]

    df2020import = df2020agricultural.loc[df2020agricultural["Element"] == "Import Value Base Period Price"]


    df2020importproductvalues = df2020import.groupby("Item").mean()
    da = df2020importproductvalues.sort_values(by=["2020"], ascending=False)
    dd = da.round({"2020": 0})

    dd.to_csv("df2020importproductvalues.csv")

    # ---------------------------------------------------------------------------------------------------------------------------

    # 2020 export data

    df2020export = df2020agricultural.loc[df2020agricultural["Element"] == "Export Value Base Price"]
    df2020exportproductvalues = df2020export.groupby("Item").mean()
    da = df2020exportproductvalues.sort_values(by=["2020"], ascending=False)
    dd = da.round({"2020": 0})

    dd.to_csv("df2020exportproductvalues.csv")


#---------------------------------------------------------------------------------------------------------------------------

#Yearcolumnstorow
def yearbyyearimportandexport():
    #yıllara göre en çok tarım ürünü ihracatı ve ithalatı yapan ülkeler.

    da = dbfood.melt(id_vars=['Area', 'Item', 'Element'],
            var_name="Year",
            value_name="Value")
    dn1 = da[da['Area'].isin(listofcoutry)]
    da1 = dn1[dn1["Element"].isin(["Import Value Base Period Price","Export Value Base Price"])]
    da1 = da1.loc[da1["Item"]=="Agricultural Products"]
    da2 =da1.loc[da1["Element"]=="Export Value Base Price"]
    da3 =da1.loc[da1["Element"]=="Import Value Base Period Price"]

    dbyearbyyearimport = da3[["Area","Year","Value"]]
    dbyearbyyearimport = dbyearbyyearimport.groupby(["Area","Year"]).sum()
    dbyearbyyearimport.to_csv("dbyearbyyearimport.csv")


    dbyearbyyearexport = da2[["Area","Year","Value"]]
    dbyearbyyearexport = dbyearbyyearexport.groupby(["Area","Year"]).sum()
    dbyearbyyearexport.to_csv("dbyearbyyearexport.csv")




def countryagriculturalproductandamountyearlyexport():
    #ülkelerin yıl yıl ne kadar ürün ihraç ettiği ve ürettiği
       listagriculture = ['Apples', 'Bananas', 'Barley', 'Beer of barley', 'Cereal preparations nes',
                          'Cocoa, beans', 'Coconuts', 'Coconuts, desiccated', 'Copra', 'Cotton lint', 'Cottonseed', 'Dates', 'Fruit, fresh nes', 'Grapes', 'Groundnuts, shelled', 'Jute', 'Lemons and limes', 'Linseed', 'Maize', 'Malt', 'Oats', 'Oil, castor beans', 'Oil, coconut (copra)', 'Oil, cottonseed', 'Oil, groundnut', 'Oil, linseed', 'Oil, maize', 'Oil, olive, virgin', 'Oil, palm', 'Oil, palm kernel', 'Oil, rapeseed', 'Oil, soybean', 'Oil, sunflower', 'Oil, vegetable origin nes', 'Onions, dry', 'Oranges', 'Peaches and nectarines', 'Pears', 'Pepper (piper spp.)', 'Pigs', 'Pineapples', 'Pineapples canned', 'Potatoes', 'Raisins', 'Rapeseed', 'Rice, milled', 'Roots and tubers nes', 'Rubber natural dry', 'Sesame seed','Soybeans', 'Spices nes', 'Sunflower seed', 'Tea', 'Tobacco, unmanufactured','Tobacco products nes','Tomatoes', 'Walnuts, shelled', 'Wheat']

       deneme = [0, 0.0]
       dbfood1 = dbfood[dbfood["Area"].isin(listofcoutry)]
       db1 = dbfood1[dbfood1['Item'].isin(listagriculture)] #databasebased agriculturalproduct
       db2 = db1.loc[db1["Element"] == "Export Value Base Price"]

       for ab in year:
              name = str(ab)+".csv"
              db3 = db2[~db2[str(ab)].isin(deneme)] #export value 2020 higher than 0
              a = db3["Area"].tolist()

              res = []
              for i in a:
                     if i not in res:
                            res.append(i)
              keys = []
              values = []
              dicts = {}
              for i in res:
                     a = sum(db3['Area'] == i)
                     if a != "":
                            keys.append(i)
                            values.append(a)

              for i in range(len(keys)):
                     dicts[keys[i]] = values[i]

              de = db3[["Area",str(ab)]]
              d33 = de.groupby("Area").sum()
              a = pd.DataFrame.from_dict(data=dicts, orient='index')
              a.columns=["Area"]
              b=pd.concat([a,d33], axis=1, sort=False)
              name2 = "Product Amount"
              name3 = "Export Amount"
              b.index.name = "Area"
              b.columns=[name2,name3]
              b.to_csv(name, header=True)



def countryagriculturalproductandamountyearlyimport():
    #ülkelerin yıl yıl ne kadar ürün ithal ettiği
       listagriculture = ['Apples', 'Bananas', 'Barley', 'Beer of barley', 'Cereal preparations nes',
                          'Cocoa, beans', 'Coconuts', 'Coconuts, desiccated', 'Copra', 'Cotton lint', 'Cottonseed', 'Dates', 'Fruit, fresh nes', 'Grapes', 'Groundnuts, shelled', 'Jute', 'Lemons and limes', 'Linseed', 'Maize', 'Malt', 'Oats', 'Oil, castor beans', 'Oil, coconut (copra)', 'Oil, cottonseed', 'Oil, groundnut', 'Oil, linseed', 'Oil, maize', 'Oil, olive, virgin', 'Oil, palm', 'Oil, palm kernel', 'Oil, rapeseed', 'Oil, soybean', 'Oil, sunflower', 'Oil, vegetable origin nes', 'Onions, dry', 'Oranges', 'Peaches and nectarines', 'Pears', 'Pepper (piper spp.)', 'Pigs', 'Pineapples', 'Pineapples canned', 'Potatoes', 'Raisins', 'Rapeseed', 'Rice, milled', 'Roots and tubers nes', 'Rubber natural dry', 'Sesame seed','Soybeans', 'Spices nes', 'Sunflower seed', 'Tea', 'Tobacco, unmanufactured','Tobacco products nes','Tomatoes', 'Walnuts, shelled', 'Wheat']

       deneme = [0, 0.0]
       dbfood1 = dbfood[dbfood["Area"].isin(listofcoutry)]
       db1 = dbfood1[dbfood1['Item'].isin(listagriculture)] #databasebased agriculturalproduct
       db2 = db1.loc[db1["Element"] == "Import Value Base Price"]

       for ab in year:
              name = str(ab)+".csv"
              db3 = db2[~db2[str(ab)].isin(deneme)] #export value 2020 higher than 0
              a = db3["Area"].tolist()

              res = []
              for i in a:
                     if i not in res:
                            res.append(i)
              keys = []
              values = []
              dicts = {}
              for i in res:
                     a = sum(db3['Area'] == i)
                     if a != "":
                            keys.append(i)
                            values.append(a)

              for i in range(len(keys)):
                     dicts[keys[i]] = values[i]

              de = db3[["Area",str(ab)]]
              d33 = de.groupby("Area").sum()
              a = pd.DataFrame.from_dict(data=dicts, orient='index')
              a.columns=["Area"]
              b=pd.concat([a,d33], axis=1, sort=False)
              name2 = "Product Amount"
              name3 = "Import Amount"
              b.index.name = "Area"
              b.columns=[name2,name3]
              b.to_csv(name, header=True)


def country2020():
    #hedef ülkenin 2020 yılı
       a = input("Insert Country Name")
       db1 = dbfood[dbfood['Item'].isin(listagriculture)]
       worlddb = db1.loc[dbfood["Area"] == str(a)]

       worldbimport = worlddb.loc[worlddb["Element"] == "Import Value Base Period Price"]
       worldb2020import = worldbimport[["Item", "2020"]]
       worldimport2020 = worldb2020import.sort_values(by=["2020"], ascending=False)
       name = str(a)+"import2020.csv"
       worldimport2020.to_csv(name)

       worlddbexport = worlddb.loc[worlddb["Element"] == "Export Value Base Price"]
       worldb2020export = worlddbexport[["Item", "2020"]]
       worldexport2020 = worldb2020export.sort_values(by=["2020"], ascending=False)
       name = str(a)+"export2020.csv"
       worldexport2020.to_csv(name)



def countryproducbasedchange():

    #ülkelerin yıl yıl hangi tarımsal ürünlerin ihracatını ve ithalatını yaptığı.

       da = dbfood.melt(id_vars=['Area', 'Item', 'Element'],
              var_name="Year",
              value_name="Value")

       da1 = da[da["Element"].isin(["Import Value Base Period Price","Export Value Base Price"])]

       dd = []

       for i, day in enumerate(listagriculture):
              data_day = da1[da1.Item == day]
              dd.append(data_day)
       da1 = pd.concat(dd)
       da2 =da1.loc[da1["Element"]=="Export Value Base Price"]
       da3 =da1.loc[da1["Element"]=="Import Value Base Period Price"]

       dbyearbyyearimport = da3[["Area","Item","Year","Value"]]
       dbyearbyyearimport = dbyearbyyearimport.groupby(["Area","Item","Year"]).sum()
       dbyearbyyearimport.to_csv("dbyearbyyearproductimport.csv")


       dbyearbyyearexport = da2[["Area","Item","Year","Value"]]
       dbyearbyyearexport = dbyearbyyearexport.groupby(["Area","Item","Year"]).sum()
       dbyearbyyearexport.to_csv("dbyearbyyearproductexport.csv")

def countrypopulation():

    df = pd.read_csv("API_SP.POP.TOTL_DS2_en_csv_v2_3731322.csv")

    dd = df[['Country Name','1960', '1961', '1962', '1963', '1964', '1965', '1966', '1967', '1968', '1969', '1970', '1971', '1972', '1973', '1974', '1975', '1976', '1977', '1978', '1979', '1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987', '1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', ]]

    db = dd.melt(id_vars='Country Name',
                var_name="Year",
                value_name="Population")
    da = db.groupby(["Country Name","Year"]).sum()
    da.to_csv("Populationcoutry.csv")

worldinformation()
agriculturaldatacoutry2020()
agriculturalproductexportandimport()
yearbyyearimportandexport()
countryagriculturalproductandamountyearlyexport()
countryagriculturalproductandamountyearlyimport()
country2020()
countryproducbasedchange()
countrypopulation()