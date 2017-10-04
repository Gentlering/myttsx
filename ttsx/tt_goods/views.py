from django.shortcuts import render
from .models import *
from django.core.paginator import Paginator,Page
from haystack.generic_views import SearchView
def index(request):
    '''
    首页上循环输出六种类型的信息，每类中循环出商品的信息
    :param request:
    :return:
    '''
    type_list=TypeInfo.objects.all()
    # print(type_list)
    list=[]
    for type in type_list:
        new=type.goodsinfo_set.all().order_by('-id')[0:4]
        click=type.goodsinfo_set.all().order_by('-gclick')[0:3]
        list.append({'type':type,'new':new,'click':click})
    context={'title':'首页','iscart':1,'list':list}
    return render(request,'tt_goods/index.html',context)

def list(request,tid,pindex,order):
    '''
        分类对象
        当前分类最新的2个商品
        当前页的商品列表
        '''
    # 分类对象
    type = TypeInfo.objects.get(id=tid)
    # 当前分类最新的2个商品
    new = type.goodsinfo_set.all().order_by('-id')[0:2]
    # 判断排序规则
    order_str = '-id'
    if order == '2':
        order_str = '-gprice'
    elif order == '3':
        order_str = '-gclick'
    # 当前页的商品列表
    goods_list = GoodsInfo.objects.filter(gtype_id=tid).order_by(order_str)
    paginator = Paginator(goods_list, 10)
    page = paginator.page(int(pindex))

    context={'title':'商品列表','iscart':1,'type':type,'new':new,'page':page,'order':order}
    return render(request,'tt_goods/list.html',context)

def detail(request,gid):
    #查询当前的商品对象
    goods=GoodsInfo.objects.get(id=gid)
    #修改点击量
    goods.gclick+=1
    goods.save()
    #查询当前商品对应分类的两个最新商品
    new=goods.gtype.goodsinfo_set.all().order_by('-id')[0:2]

    context={'title':'商品详情','iscart':1,'goods':goods,'new':new}
    response= render(request,'tt_goods/detail.html',context)
    # 存储最近浏览商品  1,2,3,4,5
    gid = str(goods.id)
    zjll_list = [gid]
    zjll = request.COOKIES.get('zjll', '')
    if zjll:
        # 将存储的字符串转换成列表
        zjll_list = zjll.split(',')
        # 判断当前列表中是否已经存在gid，如果存在则去除
        if gid in zjll_list:
            zjll_list.remove(gid)
        # 将gid加入到列表第一位
        zjll_list.insert(0, gid)
        # 如果长度超过5个则删除最后一个
        if len(zjll_list) > 5:
            zjll_list.pop()
    response.set_cookie('zjll', ','.join(zjll_list), expires=60 * 60 * 24 * 7)

    return response

class MySearchView(SearchView):
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['iscart']=1
        context['search']=2
        context['title']='商品搜索'
        return context


# Create your views here.
