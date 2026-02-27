# Photography Studio Booking
service1 = input('Enter the first service name: ')
price1 = float(input('Enter the price of first service: '))
service2 = input('Enter the second service name: ')
price2 = float(input('Enter the price of second service: '))
service3 = input('Enter the third service name: ')
price3 = float(input('Enter the price of third service: '))
print('-' * 10, 'Studio quote', '-' * 10)
price1 = int(price1 * 100) / 100 # 100 ga ko'paytirib bo'lish orqali yaxlitlashimiz mumkin
price2 = int(price2 * 100) / 100
price3 = int(price3 * 100) / 100
print(f'{service1}            $ {price1}')
print(f'{service2}          $ {price2}')
print(f'{service3}            $ {price3}')
print('-' * 30)
subtotal = price1 + price2 + price3 # 3 ta servisni subtotalini hisoblaydi
subtotal = int(subtotal * 100) / 100 # subtotalni ham oxirgi ikki raqamini yaxlitlaydi
answer = input('Do you have a studio subscription? (yes/no): ') #userdan yes no info oladi va
has_subscription = (answer == "yes")
discount_applies = subtotal > 400 # subscribtion bor va discount ishlaydi
discount = discount_applies * subtotal * 0.14 # discountni hisoblaydi
discount = int(discount * 100) / 100 # discountni ham oxirgi ikki raqamini yaxlitlaydi
after_discount = subtotal - discount # discountdan keyini total hisobi
after_discount = int(after_discount * 100) / 100
fee_applies = not has_subscription # subscribtion yoq payti fee amal qilishi
fee = fee_applies * after_discount * 0.16 # fee ni hisoblaydi
fee = int(fee * 100) / 100
total = after_discount + fee #totalni hisoblaydi
total = int(total * 100) / 100
print(f'Returning Discount (14%)       -$ {discount}')
print(f'After discount       $ {after_discount}')
print(f'Editing fee (16%)       +$ {fee}')
print('-' * 30)
print(f'Total             $ {total}')
print('-' * 30)
print(f'Discount applied :  {discount_applies}') #discount ishlaganini yoki ishlamagani haqida info
print(f'Fee applied :  {fee_applies}') #fee ishlaganini yoki ishlamagani haqida info
print('-' * 30)