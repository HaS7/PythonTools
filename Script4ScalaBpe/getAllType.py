import re
s = """ <message name="insertGoodsInfo" id="1">
        <sql><![CDATA[
            insert into accountTradeCenter.tProduct(matrix_name,game_id,area_id,group_id,sp_id,trade_mode,src_code,
            goods_type,game_app_os,game_operator_id,p_account,p_sdpt,state,client_ip,onsell_period,ext1,ext2,
            p_name,p_role_name,sdid,sdpt,b_uid,xid,p_tips,book_id,s_book_id,p_values,b_amount,b_qty,ttl_bag_qty,price,
            s_credit_value,create_time,update_time,save_time,modify_time) values
            (matrix_name,:game_id,:area_id,:group_id,:sp_id,:trade_mode,:src_code,
            :goods_type,:game_app_os,:game_operator_id,:p_account,:p_sdpt,:state,:client_ip,:onsell_period,:ext1,:ext2,
            :p_name,:p_role_name,:sdid,:sdpt,:b_uid,:xid,:p_tips,:book_id,:s_book_id,:p_values,:b_amount,:b_qty,:ttl_bag_qty,
            :price,:s_credit_value,now(),now(),now(),now())
        ]]></sql>
		<requestParameter>
			<field name="matrix_name"       type="matrix_name_type" />
            <field name="game_id"           type="game_id_type" />
            <field name="area_id"           type="area_id_type" />
            <field name="group_id"          type="group_id_type" />
            <field name="sp_id"             type="sp_id_type" />
            <field name="trade_mode"        type="trade_mode_type" />"""

pattern = re.compile('type="(.*?)_type"',re.S)

items = list(set(re.findall(pattern,s)))

for i in range(len(items)):
    t = "<type name=\"" + items[i] + "_type\"" + ""
    print(t + (39 - len(t)) * " " + "class=\"string\" code=\"" + str(i + 1) + "\"" + (3 - len(str(i))) * " " + "/>")

#knb