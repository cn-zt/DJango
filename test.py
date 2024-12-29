import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'my_first_site.settings')

import django
django.setup()

from polls.models import PastQuestion, PresentQuestion, FutureQuestion, PastChoice, PresentChoice, FutureChoice
from django.utils import timezone


# 为 PastQuestion 模型创建数据
def create_past_questions():
    # 问题 1
    question1 = PastQuestion.objects.create(question_text="你小时候最喜欢的玩具是什么？", pub_date=timezone.now())
    PastChoice.objects.create(question=question1, choice_text="积木", votes=0)
    PastChoice.objects.create(question=question1, choice_text="四驱车", votes=0)
    PastChoice.objects.create(question=question1, choice_text="毛绒玩具", votes=0)
    PastChoice.objects.create(question=question1, choice_text="弹弓", votes=0)

    # 问题 2
    question2 = PastQuestion.objects.create(question_text="你学生时代最难忘的考试是哪一门？", pub_date=timezone.now())
    PastChoice.objects.create(question=question2, choice_text="高考", votes=0)
    PastChoice.objects.create(question=question2, choice_text="中考", votes=0)
    PastChoice.objects.create(question=question2, choice_text="英语四六级", votes=0)
    PastChoice.objects.create(question=question2, choice_text="专业资格考试", votes=0)

    # 问题 3
    question3 = PastQuestion.objects.create(question_text="你过去旅行中最意外的经历是什么？", pub_date=timezone.now())
    PastChoice.objects.create(question=question3, choice_text="遇到罕见的野生动物", votes=0)
    PastChoice.objects.create(question=question3, choice_text="赶上当地的盛大节日", votes=0)
    PastChoice.objects.create(question=question3, choice_text="迷路但发现绝美风景", votes=0)
    PastChoice.objects.create(question=question3, choice_text="行李丢失又失而复得", votes=0)

    # 问题 4
    question4 = PastQuestion.objects.create(question_text="你曾经参加过的最具挑战性的运动是什么？", pub_date=timezone.now())
    PastChoice.objects.create(question=question4, choice_text="登山", votes=0)
    PastChoice.objects.create(question=question4, choice_text="马拉松", votes=0)
    PastChoice.objects.create(question=question4, choice_text="潜水", votes=0)
    PastChoice.objects.create(question=question4, choice_text="跳伞", votes=0)

    # 问题 5
    question5 = PastQuestion.objects.create(question_text="你年少时最向往的生活场景是？", pub_date=timezone.now())
    PastChoice.objects.create(question=question5, choice_text="住在海边的小木屋", votes=0)
    PastChoice.objects.create(question=question5, choice_text="在大城市打拼出一片天", votes=0)
    PastChoice.objects.create(question=question5, choice_text="隐居山林", votes=0)
    PastChoice.objects.create(question=question5, choice_text="环游世界", votes=0)


# 为 PresentQuestion 模型创建数据
def create_present_questions():
    # 问题 1
    question1 = PresentQuestion.objects.create(question_text="你目前每天花在阅读上的时间大约是？", pub_date=timezone.now())
    PresentChoice.objects.create(question=question1, choice_text="小于 30 分钟", votes=0)
    PresentChoice.objects.create(question=question1, choice_text="30 分钟 - 1 小时", votes=0)
    PresentChoice.objects.create(question=question1, choice_text="1 小时 - 2 小时", votes=0)
    PresentChoice.objects.create(question=question1, choice_text="大于 2 小时", votes=0)

    # 问题 2
    question2 = PresentQuestion.objects.create(question_text="你现在最主要的压力来源是什么？", pub_date=timezone.now())
    PresentChoice.objects.create(question=question2, choice_text="工作压力", votes=0)
    PresentChoice.objects.create(question=question2, choice_text="经济压力", votes=0)
    PresentChoice.objects.create(question=question2, choice_text="人际关系压力", votes=0)
    PresentChoice.objects.create(question=question2, choice_text="学业压力", votes=0)

    # 问题 3
    question3 = PresentQuestion.objects.create(question_text="你当前最常参与的线上社交活动是？", pub_date=timezone.now())
    PresentChoice.objects.create(question=question3, choice_text="在微信群聊天", votes=0)
    PresentChoice.objects.create(question=question3, choice_text="刷微博评论互动", votes=0)
    PresentChoice.objects.create(question=question3, choice_text="玩在线游戏社交", votes=0)
    PresentChoice.objects.create(question=question3, choice_text="参与线上论坛讨论", votes=0)

    # 问题 4
    question4 = PresentQuestion.objects.create(question_text="你现在的饮食习惯更倾向于？", pub_date=timezone.now())
    PresentChoice.objects.create(question=question4, choice_text="重口味", votes=0)
    PresentChoice.objects.create(question=question4, choice_text="清淡为主", votes=0)
    PresentChoice.objects.create(question=question4, choice_text="素食主义", votes=0)
    PresentChoice.objects.create(question=question4, choice_text="少食多餐", votes=0)

    # 问题 5
    question5 = PresentQuestion.objects.create(question_text="你目前最喜欢的放松方式是什么？", pub_date=timezone.now())
    PresentChoice.objects.create(question=question5, choice_text="看电影", votes=0)
    PresentChoice.objects.create(question=question5, choice_text="听音乐", votes=0)
    PresentChoice.objects.create(question=question5, choice_text="运动", votes=0)
    PresentChoice.objects.create(question=question5, choice_text="冥想", votes=0)


# 为 FutureQuestion 模型创建数据
def create_future_questions():
    # 问题 1
    question1 = FutureQuestion.objects.create(question_text="你未来 2 年内最想考取的证书是？", pub_date=timezone.now())
    FutureChoice.objects.create(question=question1, choice_text="驾驶证", votes=0)
    FutureChoice.objects.create(question=question1, choice_text="职业资格证", votes=0)
    FutureChoice.objects.create(question=question1, choice_text="语言证书", votes=0)
    FutureChoice.objects.create(question=question1, choice_text="学历提升证书", votes=0)

    # 问题 2
    question2 = FutureQuestion.objects.create(question_text="你预计未来 3 年自己会购买的大件商品是？", pub_date=timezone.now())
    FutureChoice.objects.create(question=question2, choice_text="汽车", votes=0)
    FutureChoice.objects.create(question=question2, choice_text="房产", votes=0)
    FutureChoice.objects.create(question=question2, choice_text="高端电子产品", votes=0)
    FutureChoice.objects.create(question=question2, choice_text="健身器材",  votes=0)

    # 问题 3
    question3 = FutureQuestion.objects.create(question_text="你将来希望投身的公益领域是？", pub_date=timezone.now())
    FutureChoice.objects.create(question=question3, choice_text="环保", votes=0)
    FutureChoice.objects.create(question=question3, choice_text="教育扶贫", votes=0)
    FutureChoice.objects.create(question=question3, choice_text="动物保护", votes=0)
    FutureChoice.objects.create(question=question3, choice_text="关爱弱势群体", votes=0)

    # 问题 4
    question4 = FutureQuestion.objects.create(question_text="你未来希望拥有的居住环境是？", pub_date=timezone.now())
    FutureChoice.objects.create(question=question4, choice_text="市中心繁华地段", votes=0)
    FutureChoice.objects.create(question=question4, choice_text="郊区安静别墅", votes=0)
    FutureChoice.objects.create(question=question4, choice_text="靠近自然景区", votes=0)
    FutureChoice.objects.create(question=question4, choice_text="智能科技住宅",  votes=0)

    # 问题 5
    question5 = FutureQuestion.objects.create(question_text="你将来是否有出国旅游的打算？", pub_date=timezone.now())
    FutureChoice.objects.create(question=question5, choice_text="有，近期就打算去", votes=0)
    FutureChoice.objects.create(question=question5, choice_text="有，未来几年内去", votes=0)
    FutureChoice.objects.create(question=question5, choice_text="没有，觉得国内就很好", votes=0)
    FutureChoice.objects.create(question=question5, choice_text="不确定，看情况", votes=0)


if __name__ == '__main__':
    create_past_questions()
    create_present_questions()
    create_future_questions()