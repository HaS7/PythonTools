
s = """order_id,order_type,trade_type,book_id,game_app_os,game_operator_id,b_game_id,b_area_id,b_group_id,s_game_id,s_area_id,s_group_id,b_sdid,b_sdpt,b_character_id,
			b_character_name,b_phone,s_sdid,s_sdpt,s_character_id,s_character_name,goods_id,goods_type,goods_name,price,pic_url,batches,
			num,product_name,product_tips,sdid,sdpt,product_create_time,p_public_period,p_amount,p_real_amount,discount_amount,partial_refund_amount,s_fee,b_fee,
			state,locked,pay_id,goods_transfer_id,mid_account,user_memo,remark,coupon_ticket,src_code,client_ip,server_ip,s_xid,s_b_uid,b_xid,
			b_b_uid,ext1,ext2,backup,pay_time,income_time,create_time,update_time,save_time,del_flag,pay_channel,confirm_time,b_eval_status,s_eval_status,invoice_flag,mail_address,cs_queue_state ,start_pay_time,pay_queue 
			"""


l = s.split(",")

l = [x.strip() for x in l]

ss = max([len(x) for x in l])


t1 = "<field name=\"game_operator_id\""

for i in l:
    t = "<field name=\""+i+"\""
    print(   t+(32-len(t))*" "+ "type=\""+i+"_type\" />"       )


# <field name="b_uid" type="b_uid_type" />
#
#
# #<type name="b_uid_type" class="string" code="1" />
# for i in range(len(l)):
#     t = "<type name=\""+l[i]+"_type\""+""
#     print(t + (35 - len(t)) * " " + "class=\"string\" code=\""+str(i+47)+ "\""   +(3-len(str(i)))*" "  + "/>" )