__author__ = 'Administrator'


content = '''



<div class="article block untagged mb15" id='qiushi_tag_119163998'>

<div class="author clearfix">
<a href="/users/33478794/" target="_blank" rel="nofollow">
<img src="//pic.qiushibaike.com/system/avtnew/3347/33478794/medium/20170331160209.JPEG" alt="不要葱姜蒜"/>
</a>
<a href="/users/33478794/" target="_blank" title="不要葱姜蒜">
<h2>不要葱姜蒜</h2>
</a>
<div class="articleGender womenIcon">23</div>
</div>



<a href="/article/119163998" target="_blank" class='contentHerf' >
<div class="content">



<span>五个字。。。。</span>


</div>
</a>




<div class="thumb">

<a href="/article/119163998" target="_blank">
<img src="//pic.qiushibaike.com/system/pictures/11916/119163998/medium/app119163998.jpg" alt="糗事#119163998" />
</a>

</div>



<div class="stats">
<span class="stats-vote"><i class="number">501</i> 好笑</span>
<span class="stats-comments">


<span class="dash"> · </span>
<a href="/article/119163998" data-share="/article/119163998" id="c-119163998" class="qiushi_comments" target="_blank">
<i class="number">1</i> 评论
</a>

'''

import re
#pattern = re.compile('<div.*?author.*?<a.*?<img.*?>(.*?)</a>.*?<div.*?'+'content">(.*?)<!--(.*?)-->.*?</div>(.*?)<div class="stats.*?class="number">(.*?)</i>',re.S)


pattern = re.compile('<div class="author clearfix">.*?<h2>(.*?)</h2>.*?<span>(.*?)</span>'
                     '.*?<span class="stats-vote"><i class="number">(.*?)</i>.*?<i class="number">(.*?)</i>',re.S)
items = re.findall(pattern,content)





print(items)



