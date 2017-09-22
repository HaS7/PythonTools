#code='utf-8'
import io

with open('temp.txt','rb') as f:
    s = f.read().decode('utf-8')

play_level_name_A = {'1':'倔强青铜','2':'秩序白银','3':'荣耀黄金','4':'尊贵铂金','5':'永恒钻石五' ,
                     '6':'永恒钻石四','7':'永恒钻石三','8':'永恒钻石二' ,'9':'永恒钻石一',
                     '10':'至尊星燿五','11':'至尊星燿四','12':'至尊星燿三','13':'至尊星燿二','14':'至尊星燿一'}
{'1':'倔强青铜   ',
'2':'秩序白银   ',
'3':'荣耀黄金   ',
'4':'尊贵铂金   ',
'5':'永恒钻石五   ',
'6':'永恒钻石四  ',
'7':'永恒钻石三  ',
'8':'永恒钻石二   ',
'9':'永恒钻石一',
'10':'至尊星燿五   ',
'11':'至尊星燿四',
'12':'至尊星燿三',
'13':'至尊星燿二',
'14':'至尊星燿一'}


play_type_name_A = {'1':'包赢一星','2':'包赢三星','3':'包赢五星','4':'陪玩一局','5':'陪玩三局','6':'陪玩五局'}

times = {'1':1,'2':3,'3':5,'4':1,'5':3,'6':5}

price_A_A= {'1':'4.00','2':'6.00','3':'12.00','4':'18.00','5':'24.00' ,
                     '6':'24.00','7':'36.00','8':'36.00' ,'9':'48.00',
                     '10':'72.00','11':'84.00','12':'96.00','13':'108.00','14':'120.00'}

price_A_B= {'1':'4.00','2':'5.00','3':'6.00','4':'10.00','5':'12.00' ,
                     '6':'12.00','7':'18.00','8':'18.00' ,'9':'24.00',
                     '10':'30.00','11':'32.00','12':'36.00','13':'38.00','14':'42.00'}

p_img_cover_A= {'1':'http://gprofile.sdo.com/sdo4/M00/37/CB/CoEp_Fmo16qANgkHAACU2v-nh10138.png',
                '2':'http://gprofile.sdo.com/sdo4/M01/17/0A/CoEp_Vmo19mAKOd9AADCHXJLJjc817.png',
                '3':'http://gprofile.sdo.com/sdo4/M00/37/CB/CoEp_Fmo2AKAYZorAADRYYqaFjc379.png',
                '4':'http://gprofile.sdo.com/sdo4/M00/37/C9/CoEp_Fmo1xqAbqUpAAAuVzZ4VAg860.png',
                '5':'http://gprofile.sdo.com/sdo4/M00/37/CA/CoEp_Fmo10OAC47gAAAvJIq12mA740.png',
                '6':'http://gprofile.sdo.com/sdo4/M00/37/CA/CoEp_Fmo12WAfsJYAAAvUQKT1Fo360.png'}


count = 1000000000

pre = 'PWP0000000000000000000'
for i in range(1,15):
    for j in range(1,7):
        with open('sql.txt','a') as  f:
            temp = s
            count+=1

            temp = temp.replace('s_book_id_A', str(count))
            temp = temp.replace('book_id_A', pre + str(count))
            temp = temp.replace('play_level_name_A',play_level_name_A[str(i)])
            temp = temp.replace('play_level_A', str(i))
            temp = temp.replace('play_type_name_A', play_type_name_A[str(j)])
            temp = temp.replace('play_type_A', str(j))
            temp = temp.replace('p_name_A', '[陪玩]'+play_type_name_A[str(j)]+'-'+play_level_name_A[str(i)])
            if j<4:
                u_price = float(price_A_A[str(i)])
            else:
                u_price = float(price_A_B[str(i)])
            time = int(times[str(j)])

            price = u_price*time

            temp = temp.replace('price_A', '%.2f' % price)
            temp = temp.replace('p_img_cover_A', p_img_cover_A[str(j)])
            f.write( temp+'\n')

