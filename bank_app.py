def run_bank_app():
    inputs = ['1- Bakiye sorgulama', '2- Para çekme', '3- Para yatırma', '4- Çıkış']
    user_name = 'arda'
    user_password = 123456789
    started_money = 1000
    money = started_money
    
    name_login = input('Hoşgeldiniz! adınız nedir: ').lower()
    password_login = int(input('Şifreni gir: '))
    
    if name_login == user_name and password_login == user_password:
        print('Giriş başarılı!')
        while True:
            ask = int(input('\n'.join(inputs) + '\nYapmak istediğiniz işlemi seçin: '))
            
            if ask == 1:
                print('Bakiyeniz', money, '₺')
            elif ask == 2:
                withdraw = int(input('Kaç para çekmek istiyorsunuz: '))
                if withdraw <= money:
                    print(withdraw, '₺ para çektiniz. Güncel bakiyeniz', money - withdraw, '₺')
                    money -= withdraw
                else:
                    print('Yetersiz bakiye')
            elif ask == 3:
                deposit = int(input('Kaç para yatırmak istiyorsunuz: '))
                print(deposit, '₺ para yatırdınız. Güncel bakiyeniz', money + deposit, '₺')
                money += deposit
            elif ask == 4:
                print('Başarıyla çıkış yaptınız')
                break
            else:
                print('Geçersiz bir seçenek girdiniz. Lütfen tekrar deneyin.')
    else:
        print('Giriş yapılamadı. Kullanıcı adı veya şifre yanlış.')

run_bank_app()
