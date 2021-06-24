# 定义天气查找类
class WeatherSearch(object):
    def __init__(self,input_daytime):
        self.input_daytime = input_daytime

    def seach_visibility(self):   # 定义一个“搜索可见度”的类
        visible_leave = 0
        if self.input_daytime == 'daytime':
            visible_leave = 2
        if self.input_daytime == 'night':
            visible_leave = 9
        return visible_leave

    def seach_temperature(self):   # 定义了一个搜索温度的类
        temperature = 0
        if self.input_daytime == 'daytime':
            temperature = 26
        if self.input_daytime == 'night':
            temperature = 16
        return temperature

# 定义建议类，根据天气查找类返回的内容来给出对应不同的出行建议

