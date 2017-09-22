s = """CREATE TABLE `tOrder` (
  `id` int(12) unsigned NOT NULL AUTO_INCREMENT,
  `order_id` varchar(64) NOT NULL DEFAULT '' COMMENT '订单ID（全局唯一）',
  `s_order_id` varchar(32) NOT NULL DEFAULT '' COMMENT '订单短号',
  `order_type` tinyint(8) unsigned NOT NULL DEFAULT '0',
  `trade_type` tinyint(6) NOT NULL DEFAULT '0' COMMENT '交易类型（0：默认交易）',
  `book_id` varchar(64) NOT NULL DEFAULT '' COMMENT '全局唯一ID',
  `sp_goods_no` varchar(64) NOT NULL DEFAULT '',
  `sp_order_no` varchar(64) NOT NULL DEFAULT '' COMMENT '供应商订单编号',
  `sp_id` varchar(64) NOT NULL DEFAULT '' COMMENT '供应商商户编号',
  `state` tinyint(8) unsigned NOT NULL DEFAULT '0' COMMENT '状态',
  `sp_state` varchar(12) NOT NULL DEFAULT '' COMMENT '供应商平台状态',
  `sp_notify_state` tinyint(4) NOT NULL DEFAULT '0' COMMENT '是否通知调用供应商',
  `game_app_os` int(10) unsigned NOT NULL DEFAULT '0' COMMENT '游戏运行系统 约定：1：‘安卓’ ,2 : ‘苹果’',
  `game_operator_id` int(10) NOT NULL DEFAULT '0' COMMENT '游戏运营商id',
  `b_game_id` int(10) DEFAULT '0' COMMENT '买游戏编号',
  `b_area_id` int(10) DEFAULT '0' COMMENT '买家游戏区编号',
  `b_group_id` int(10) DEFAULT '0' COMMENT '买家游戏组编号',
  `b_mid` bigint(20) unsigned NOT NULL DEFAULT '0' COMMENT '买方: mid',
  `b_b_uid` bigint(20) unsigned NOT NULL DEFAULT '0' COMMENT '买家业务层用户ID',
  `b_phone` varchar(64) NOT NULL DEFAULT '' COMMENT '买家手机号',
  `s_game_id` int(10) DEFAULT '0' COMMENT '卖家游戏号',
  `s_area_id` int(10) DEFAULT '0' COMMENT '卖家区号',
  `s_group_id` int(10) DEFAULT '0' COMMENT '卖家组号',
  `s_mid` bigint(20) unsigned NOT NULL DEFAULT '0' COMMENT '卖方: mid',
  `s_phone` varchar(64) NOT NULL COMMENT '卖家手机号',
  `s_b_uid` bigint(20) unsigned NOT NULL DEFAULT '0' COMMENT '卖家业务层用户ID',
  `goods_id` int(10) unsigned NOT NULL DEFAULT '0' COMMENT '供应商对应商品的编号',
  `goods_type` tinyint(8) unsigned NOT NULL DEFAULT '15' COMMENT '陪玩 15',
  `goods_name` varchar(128) NOT NULL DEFAULT '' COMMENT '商品的物品的名称。',
  `play_type` varchar(32) NOT NULL DEFAULT '' COMMENT '陪玩类型编号',
  `play_type_name` varchar(128) NOT NULL DEFAULT '' COMMENT '陪玩类型名',
  `play_level` varchar(32) NOT NULL DEFAULT '' COMMENT '陪玩等级',
  `play_level_name` varchar(128) NOT NULL DEFAULT '' COMMENT '陪玩等级名',
  `play_start_time` varchar(128) NOT NULL DEFAULT '' COMMENT '用户填写的陪玩开始时间',
  `p_role_name` varchar(128) NOT NULL DEFAULT '' COMMENT '角色名',
  `pic_url` varchar(256) NOT NULL DEFAULT '' COMMENT '物品图路径',
  `price` decimal(16,6) unsigned NOT NULL DEFAULT '0.000000' COMMENT '单价',
  `num` int(10) unsigned NOT NULL DEFAULT '1' COMMENT '购买数量',
  `product_tips` varchar(1024) NOT NULL DEFAULT '' COMMENT '商品介绍',
  `total_price` decimal(12,2) unsigned NOT NULL DEFAULT '0.00' COMMENT '订单总价（购买多个充值面额的总价）.PRICE*NUM ,',
  `discount_amount` decimal(12,2) unsigned NOT NULL DEFAULT '0.00' COMMENT '优惠金额',
  `p_real_amount` decimal(12,2) unsigned NOT NULL DEFAULT '0.00' COMMENT '订单总价',
  `b_fee` decimal(10,2) unsigned NOT NULL DEFAULT '0.00' COMMENT '买家支付手续费',
  `s_fee` decimal(10,2) unsigned NOT NULL DEFAULT '0.00' COMMENT '卖家支付手续费',
  `locked` tinyint(8) unsigned NOT NULL DEFAULT '0' COMMENT '锁定订单，停止自动处理。1:lock 0:unlock',
  `pay_id` varchar(64) NOT NULL DEFAULT '' COMMENT '付款ID.付款完成凭据',
  `goods_transfer_id` varchar(64) NOT NULL DEFAULT '' COMMENT '供应商发货凭证编号',
  `buy_values` varchar(1024) DEFAULT '' COMMENT '购买下单填写模板值 json',
  `buy_tips` varchar(1024) DEFAULT '' COMMENT '客户端显示用下单模板值 json',
  `secret_tips` varchar(1024) DEFAULT '' COMMENT '客户端下单模板中的敏感加密信息（包含键值中文名）',
  `secret_values` varchar(1024) DEFAULT '' COMMENT '账号密码等敏感加密信息',
  `mid_account` varchar(64) NOT NULL DEFAULT '' COMMENT '中间账号',
  `user_memo` varchar(2048) NOT NULL DEFAULT '' COMMENT '订单备注json：（用户/客服备注）。包括  apply_refund_reason  judge_reason refuse_refund_reason',
  `coupon_ticket` varchar(64) NOT NULL DEFAULT '' COMMENT '优惠券凭证',
  `client_ip` varchar(20) NOT NULL DEFAULT '' COMMENT '客户端IP',
  `src_code` varchar(45) NOT NULL DEFAULT '1' COMMENT '订单来源。（1：游戏内；2：web平台；3：手机平台）',
  `del_flag` tinyint(5) unsigned NOT NULL DEFAULT '0' COMMENT '0=正常  1=买家删除  2=卖家删除  3=全部删除',
  `ext1` varchar(512) NOT NULL DEFAULT '' COMMENT '扩展字段1',
  `backup` text NOT NULL COMMENT '快照商品的URL列表',
  `pay_time` datetime NOT NULL DEFAULT '0000-00-00 00:00:00' COMMENT '付款完成时间',
  `create_time` datetime NOT NULL DEFAULT '0000-00-00 00:00:00' COMMENT '创建日期',
  `pay_channel` smallint(8) unsigned NOT NULL DEFAULT '2' COMMENT '支付渠道：1=支付宝 2=G宝',
  `confirm_time` datetime NOT NULL DEFAULT '1971-01-01 00:00:00' COMMENT '确认购买时间',
  `b_eval_status` tinyint(5) NOT NULL DEFAULT '0' COMMENT '买家评价状态 0=未评价 1=已评价 2=已追加评价',
  `s_eval_status` tinyint(5) NOT NULL DEFAULT '0' COMMENT '卖家评价状态  0=未评价 1=已评价 2=已追加评价',
  `invoice_flag` tinyint(5) NOT NULL DEFAULT '0' COMMENT '发票标记 ，0：表示默认初始值 ，1：可申请开发票 2:已申请开发票 3：已开发票',
  `mail_address` varchar(512) NOT NULL DEFAULT '' COMMENT '邮寄地址 json ',
  `cs_queue_state` tinyint(5) NOT NULL DEFAULT '0' COMMENT '验货队列种类（0 ，场外 1：场内）',
  `income_time` datetime NOT NULL DEFAULT '0000-00-00 00:00:00' COMMENT '收款完成时间',
  `update_time` datetime NOT NULL DEFAULT '0000-00-00 00:00:00' COMMENT '保存日期',
  `save_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '保存数据时间，自动生成',
  PRIMARY KEY (`id`),
  UNIQUE KEY `uuid_orderId` (`order_id`) USING BTREE,
  KEY `idx_bookId` (`book_id`) USING BTREE,
  KEY `idx_state_type` (`state`,`order_type`) USING BTREE,
  KEY `idx_bbuid_bxid` (`b_b_uid`,`state`) USING BTREE,
  KEY `idx_sbuid_sxid` (`s_b_uid`,`state`) USING BTREE,
  KEY `idx_sorder_id` (`s_order_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='订单表'

"""


ret = s.split("`")

ret2 = []

for i in range(len(ret)):
    if i%2!=0:

        ret2.append(ret[i])

print(",".join(ret2))










