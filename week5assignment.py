def crop_yield_report(field_name, weekly_kg, target_kg=200.0):  
    weeks=len(weekly_kg)  # haftalar sonini topamiz
    total=sum(weekly_kg)  # barcha hosillar yig‘indisini hisoblaymiz
    avg=total/weeks  # o‘rtacha qiymatni topamiz
    avg=round(avg,1)  # o‘rtacha qiymatni 1 decimalgacha  yaxlitlaymiz
    peak=max(weekly_kg)  # eng katta qiymatni topamiz kg da
    lowest=min(weekly_kg)  # eng kichik qiymatni topamiz kg da
    below=0  
    for x in weekly_kg:  # ro‘yxatdagi har bir qiymatni checck qilamiz
        if x<target_kg:  # agar qiymat targetdan kichik bo‘lsa
            below=below+1  #  sanagichni oshiramiz
    changes=[]  # haftalik o‘zgarishlar uchun bo‘sh ro‘yxat
    i=1  # indeksni 1 dan boshlaymiz
    while i<weeks:  # indeks weeks dan kichik bo‘lsa ishlaydi
        prev=weekly_kg[i-1]  # oldingi hafta qiymati
        curr=weekly_kg[i]  # joriy hafta qiymati
        diff=curr-prev  # farqni hisoblaymiz
        diff=round(diff,1)  # farqni 1 kasrga yaxlitlaymiz
        changes.append(diff)  # natijani ro‘yxatga qo‘shamiz
        i=i+1  # indeksni oshiramiz
    print("Field        :",field_name)
    print("Weeks        :",weeks)
    print("Average      :",avg,"kg")
    print("Peak yield   :",peak,"kg")
    print("Lowest yield :",lowest,"kg")
    print("Below target :",below)
    print("Weekly change:",changes)
print(crop_yield_report("North Wheat Field", [180, 210, 195, 240, 160, 225, 200]))    
crop_yield_report("South Cotton Field",[150,175,220,190,140], target_kg=175.0)
    