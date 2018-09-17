#_*_coding:utf-8_*_

#数据库操作
HOSTNAME = "222.186.190.213"
PORT = 3306
USER = "root"
PASSWD = "lyb1092"
DATABASE = "config"
TABLE = "stock_datas_sectordaysdata_2018"
INSERTTIME = 49

#速度设置
SPEED = 5 #一个时间点停留时间（单位s)
UPDATESPEED = 1.8 #时间更新速度
FLOATSPEED = 0.015 #上下浮动速度
SCORESPEED = 3.5 #长短变化速度


#颜色设置
COLOR = {
    "专用设备": (100, 100, 100),
    "中药": (135, 100, 100),
    "交运设备服务": (170, 100, 100),
    "仪表电器": (205, 100, 100),
    "传媒": (240, 100, 100),
    "保险及其他": (100, 135, 100),
    "光学光电子": (135, 135, 100),
    "公交": (170, 135, 100),
    "公路铁路运输": (205, 135, 100),
    "其他电子": (240, 135, 100),
    "养殖业": (100, 170, 100),
    "农业服务": (135, 170, 100),
    "农产品加工": (170, 170, 100),
    "包装印刷": (205, 170, 100),
    "化学制品": (240, 170, 100),
    "化学制药": (100, 205, 100),
    "化工合成材料": (135, 205, 100),
    "化工新材料": (170, 205, 100),
    "医疗器械服务": (205, 205, 100),
    "医药商业": (240, 205, 100),
    "半导体及元件": (100, 240, 100),
    "园区开发": (135, 240, 100),
    "国防军工": (170, 240, 100),
    "基础化学": (205, 240, 100),
    "家用轻工": (240, 240, 100),
    "建筑材料": (100, 100, 135),
    "建筑装饰": (135, 100, 135),
    "房地产开发": (170, 100, 135),
    "新材料": (205, 100, 135),
    "景点及旅游": (240, 100, 135),
    "有色冶炼加工": (100, 135, 135),
    "服装家纺": (135, 135, 135),
    "机场航运": (170, 135, 135),
    "汽车整车": (205, 135, 135),
    "汽车零部件": (240, 135, 135),
    "港口航运": (100, 170, 135),
    "煤炭开采": (135, 170, 135),
    "燃气水务": (170, 170, 135),
    "物流": (205, 170, 135),
    "环保工程": (240, 170, 135),
    "生物制品": (100, 205, 135),
    "电力": (135, 205, 135),
    "电子制造": (170, 205, 135),
    "电气设备": (205, 205, 135),
    "白色家电": (240, 205, 135),
    "石油矿业开采": (100, 240, 135),
    "种植业与林业": (135, 240, 135),
    "纺织制造": (170, 240, 135),
    "综合": (205, 240, 135),
    "视听器材": (240, 240, 135),
    "计算机应用": (100, 100, 170),
    "计算机设备": (135, 100, 170),
    "证券": (170, 100, 170),
    "贸易": (205, 100, 170),
    "通信服务": (240, 100, 170),
    "通信设备": (100, 135, 170),
    "通用设备": (135, 135, 170),
    "造纸业": (170, 135, 170),
    "酒店及餐饮": (205, 135, 170),
    "采掘服务": (240, 135, 170),
    "钢铁": (100, 170, 170),
    "银行": (135, 170, 170),
    "零售": (170, 170, 170),
    "非汽车交运": (205, 170, 170),
    "食品加工制造": (240, 170, 170),
    "饮料制造": (100, 205, 170)
}
SHADOWCOLOR = (105,105,105)

#屏幕大小
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600

#显示边界值
CENTER_X = SCREEN_WIDTH / 2
BORDER_X = 150 #数值条左边界值
BORDER_Y = 40 #数值条上边界值

TITLE = "RANK"
BGCOLOR = (0, 0, 0)

FONTSIZE = 13 #字体大小
BOXHEIGHT = 13 #数值条高度
RANKHEIGHT = 16 #相邻数值条距离
MAXLEN = SCREEN_WIDTH * 0.4 #最大长度
BOXLEN = 1 #单位长度
MAXNLENGTH = 1 #所选时间里最长长度

#按钮
BUTTONWIDTH = 28 #按钮长度
BUTTONHEIGHT = 15 #按钮高度
BUTTONDIS = 5 #间距

#输入框
BORDERX_INPUTBOX = 230 
BORDERY_INPUTBOX = SCREEN_HEIGHT - 100
INPUTBOXWIDTH = 70 #文本框长度
INPUTBOXHEIGHT= 15 #文本框宽度
