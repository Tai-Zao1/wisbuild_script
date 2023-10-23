import datetime
import pandas as pd


def minNums(startTime, endTime):
    """计算两个时间点之间的分钟数"""
    # 处理格式,加上秒位
    startTime1 = startTime
    endTime1 = endTime
    # 计算分钟数
    startTime2 = datetime.datetime.strptime(startTime1, "%Y-%m-%d %H:%M:%S")
    endTime2 = datetime.datetime.strptime(endTime1, "%Y-%m-%d %H:%M:%S")
    seconds = (endTime2 - startTime2).seconds
    # 来获取时间差中的秒数。注意，seconds获得的秒只是时间差中的小时、分钟和秒部分的和，并没有包含时间差的天数（既是两个时间点不是同一天，失效）
    total_seconds = (endTime2 - startTime2).total_seconds()
    # 来获取准确的时间差，并将时间差转换为秒
    # print(total_seconds)
    mins = total_seconds / 60
    return int(mins)


def break_minNums(break_start_time=None, break_end_time=None):
    '''计算两个时间点之间的分钟数'''
    # 处理格式,加上秒位

    break_start_time1 = break_start_time
    break_end_time1 = break_end_time
    # 计算分钟数
    break_start_time2 = datetime.datetime.strptime(break_start_time1, "%H:%M")
    break_end_time2 = datetime.datetime.strptime(break_end_time1, "%H:%M")
    seconds = (break_end_time2 - break_start_time2).seconds
    # 来获取时间差中的秒数。注意，seconds获得的秒只是时间差中的小时、分钟和秒部分的和，并没有包含时间差的天数（既是两个时间点不是同一天，失效）
    total_seconds = (break_end_time2 - break_start_time2).total_seconds()
    # 来获取准确的时间差，并将时间差转换为秒
    # print(total_seconds)
    mins = total_seconds / 60
    return int(mins)


def work_minNums(start_time, end_time):
    '''计算两个时间点之间的分钟数'''
    # 处理格式,加上秒位

    start_time1 = start_time
    end_time1 = end_time
    # 计算分钟数
    start_time2 = datetime.datetime.strptime(start_time1, "%H:%M")
    end_time2 = datetime.datetime.strptime(end_time1, "%H:%M")
    # seconds = (end_time2 - start_time2).seconds
    # 来获取时间差中的秒数。注意，seconds获得的秒只是时间差中的小时、分钟和秒部分的和，并没有包含时间差的天数（既是两个时间点不是同一天，失效）
    total_seconds = (end_time2 - start_time2).total_seconds()
    # 来获取准确的时间差，并将时间差转换为秒
    # print(total_seconds)
    mins = total_seconds / 60
    return int(mins)


# def over_time
#     start_time1 = start_time
#     end_time1 = end_time
#     # 计算分钟数
#     start_time2 = datetime.datetime.strptime(start_time1, "%H:%M")
#     end_time2 = datetime.datetime.strptime(end_time1, "%H:%M")
#     # seconds = (end_time2 - start_time2).seconds
#     # 来获取时间差中的秒数。注意，seconds获得的秒只是时间差中的小时、分钟和秒部分的和，并没有包含时间差的天数（既是两个时间点不是同一天，失效）
#     total_seconds = (end_time2 - start_time2).total_seconds()
#     # 来获取准确的时间差，并将时间差转换为秒
#     # print(total_seconds)
#     mins = total_seconds / 60
#     return int(mins)


if __name__ == "__main__":
    salary_amount = 500

    # 休息时间
    break_start_time1 = "11:30"
    break_end_time1 = "13:00"
    break_time = break_minNums(break_start_time1, break_end_time1)
    print("休息时间= " + str(break_time) + "分钟")

    # 上班时长
    start_time1 = "07:00"
    end_time1 = "17:30"
    work_time = work_minNums(start_time1, end_time1) - break_time
    print("应上班时间= " + str(work_time) + "分钟")
    print("平均工资：" + str(salary_amount / work_time * 60))

    # 实际上班
    startTime_1 = '2023-02-08 08:51:45'
    endTime_1 = '2023-02-08 17:59:20'
    working_time = minNums(startTime_1, endTime_1)

    time_end = endTime_1[11:19]
    time_start = start_time1[11:19]
    if time_start < break_start_time1 and time_end > break_end_time1:  # 上班打卡时间小于午休开始时间 且 下班打卡时间大于午休结束时间
        # 那么需要减去午休时间
        working_time_m = str(working_time - break_time)
        print("实际上班时间= " + working_time_m + "小时,上班期间没有包含休息")
        fact_salary_amount = salary_amount / work_time * (working_time - break_time)
        print("应发工资：" + "%.2f" % fact_salary_amount)
    elif time_end < break_start_time1:
        working_time_m1 = str(working_time)
        print("实际上班小时= " + working_time_m1 + "小时,上班期间没有包含休息")
        fact_salary_amount = salary_amount / work_time * working_time
        print("应发工资：" + "%.2f" % fact_salary_amount)
