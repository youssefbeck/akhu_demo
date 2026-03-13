def car_service(mileage_km, service_type, car_age_years=1, is_warranty=False):
    if service_type == "basic":
        cost = 150000
    elif service_type == "full":
        cost = 350000
    elif service_type == "major":
        cost = 600000      #ushbu qatorlar orqali servislar narxini belgilaymiz
    if mileage_km > 100000:
        cost = cost * 1.30 #mashina agar 100000 dan kop yurgan bo'lsa narxni oshiramiz 30%ga
    elif mileage_km > 50000:
        cost = cost * 1.15 #50000 dan kop bo'lsa 15% ga
    if car_age_years > 10:
        cost = cost * 1.20 # yoshiga qarab ham narx qoshamiz 10 yil+ bolsa 20 foiz
    elif car_age_years > 5:
        cost = cost * 1.10 # 5 yil+ bo'lsa 10 foiz
    if is_warranty == True:
        cost = cost * 0.60 #agar warranty bolsa 40 foiz discount beradi
    return round(cost) #return qilamiz costni
print(car_service(30000, "basic"))
print(car_service(80000, "full"))
print(car_service(120000, "major", car_age_years=12))
print(car_service(60000, "full", is_warranty=True))