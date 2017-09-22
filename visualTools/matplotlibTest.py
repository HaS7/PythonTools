#code='utf-8'

import matplotlib.pyplot as plt

def draw(listmap):
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
    plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
    plt.xlabel(u"关键字")
    plt.ylabel(u"个数")
    plt.title(u"切词统计")

    # 可以调整位置
    def autolabel(rects):
        for rect in rects:
            height = rect.get_height()
            plt.text(rect.get_x() + rect.get_width() / 2 - 0.2, 1.01 * height, "%s" % int(height))

    n = len(listmap[0].get('key'))

    words = [x.get('key') for x in listmap]

    counts = [x.get('doc_count') for x in listmap]

    plt.xticks(range(10), words, fontsize=10 - (n - 1) * 0.68)

    bar_color = ['#EE1289', '#EE6A50', '#EE7942', '#EE82EE', '#EEA2AD', '#EEB422', '#EECBAD', '#EED5D2', '#EEE0E5',
                 '#EEE8CD']

    rect = plt.bar(left=range(10), height=counts, width=0.8, align="center", color=bar_color,
                   edgecolor='white')
    # must be truple
    autolabel(rect)
    plt.legend((rect,), (u"个数",))

    plt.show()

